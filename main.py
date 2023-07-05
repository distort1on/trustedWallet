import sys
import hashlib
import shelve
import time
import json
import grpc
import math
import ipfsApi
import logging as log
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog
from PySide6 import QtCore, QtGui
from PyUI_Files.ui_MainWindow import Ui_MainWindow
from PyUI_Files.ui_ResponseWindow import Ui_Response
from PyUI_Files.ui_LoginWindow import Ui_login_window
from PyUI_Files.ui_RegisterWindow import Ui_register_window
from PyUI_Files.ui_RestoreWindow import Ui_restore_window
from PyUI_Files.ui_FindTxByHashWindow import Ui_tx_hash_input_window
from PyUI_Files.ui_FindDocumentByHash import Ui_find_document_by_hash_window
from ecdsa import NIST256p, SigningKey
from ecdsa.util import sigencode_der, randrange_from_seed__trytryagain
import grpcClient_pb2
import grpcClient_pb2_grpc
from Cryptodome.Cipher import AES
from mnemonic import Mnemonic
import binascii
import base64

CURRENT_USER = ""
USER_PASSWORD = ""
SOCKET = "localhost:8083"


def generate_private_key(seed):
    secexp = randrange_from_seed__trytryagain(seed, NIST256p.order)
    return SigningKey.from_secret_exponent(secexp, curve=NIST256p, hashfunc=hashlib.sha256())


class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.register_window = None
        self.RestoreWindow = None
        self.main_window = None
        self.ui = Ui_login_window()
        self.setFixedSize(530, 326)
        self.ui.setupUi(self)
        self.ui.register_button.clicked.connect(self.show_register_window)
        self.ui.login_button.clicked.connect(self.show_main_window)
        self.ui.restore_wallet_button.clicked.connect(self.show_restore_wallet_window)

    @QtCore.Slot()
    def show_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()

    @QtCore.Slot()
    def show_restore_wallet_window(self):
        self.RestoreWindow = RestoreWindow()
        self.RestoreWindow.show()

    @QtCore.Slot()
    def show_main_window(self):
        s = shelve.open('databases/wallets_accounts.db')
        try:
            if s[self.ui.login_input.text()] == hashlib.sha256(
                    bytes(self.ui.password_input.text(), 'utf-8')).digest().hex():
                global CURRENT_USER, USER_PASSWORD
                CURRENT_USER = self.ui.login_input.text()
                USER_PASSWORD = self.ui.password_input.text()

                self.main_window = MainWindow()
                self.close()
                self.main_window.show()
            else:
                QMessageBox.information(self, "Error", "Wrong password")
        except KeyError:
            QMessageBox.information(self, "Error", "User does not exists")
        finally:
            s.close()


class FindTxWindow(QWidget):
    def __init__(self):
        super(FindTxWindow, self).__init__()
        self.ui = Ui_tx_hash_input_window()
        self.setFixedSize(540, 115)
        self.ui.setupUi(self)
        self.ui.get_tx_by_hash_button.clicked.connect(self.get_tx_by_hash_action)

    @QtCore.Slot()
    def get_tx_by_hash_action(self):
        channel = grpc.insecure_channel(SOCKET)
        client = grpcClient_pb2_grpc.InvoicerStub(channel)
        log.info(f"Connected to the Server : {SOCKET}")
        tx_hash = bytes.fromhex(self.ui.tx_hash_input.text())

        response = client.GetTxByHash(grpcClient_pb2.Transaction(
            txHash=tx_hash,
        ))

        self.ui.response_window = Response()
        self.ui.response_window.setFixedSize(1200, 300)
        self.ui.response_window.show()
        self.ui.response_window.ui.text_field.setPlainText(response.response)
        channel.close()


class FindDocumentWindow(QWidget):
    def __init__(self):
        super(FindDocumentWindow, self).__init__()
        self.document_bytes = None
        self.data = None
        self.path = None
        self.ui = Ui_find_document_by_hash_window()
        self.setFixedSize(630, 115)
        self.ui.setupUi(self)
        self.ui.select_document_button.clicked.connect(self.get_document_path_action)
        self.ui.search_document_by_hash_button.clicked.connect(self.find_document_by_hash_action)

    @QtCore.Slot()
    def get_document_path_action(self):
        filename = QFileDialog.getOpenFileName(self, 'Select document', filter="*.pdf")
        path = filename[0]
        self.path = path
        self.ui.document_path_line_edit.setText(self.path)

        h = hashlib.sha256()
        with open(path, 'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)

        file = open(path, "rb")
        self.document_bytes = file.read()
        file.close()

        self.data = h.digest()

    @QtCore.Slot()
    def find_document_by_hash_action(self):
        channel = grpc.insecure_channel(SOCKET)
        client = grpcClient_pb2_grpc.InvoicerStub(channel)
        log.info(f"Connected to the Server : {SOCKET}")

        response = client.FindDocumentByHash(grpcClient_pb2.Document(
            documentHash=self.data,
        ))

        self.ui.response_window = Response()
        self.ui.response_window.setFixedSize(1200, 300)
        self.ui.response_window.show()
        self.ui.response_window.ui.text_field.setPlainText(response.response)
        channel.close()


class RegisterWindow(QWidget):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.ui = Ui_register_window()
        self.setFixedSize(530, 326)
        self.ui.setupUi(self)
        self.ui.register_button.clicked.connect(self.create_wallet_action)

    @QtCore.Slot()
    def create_wallet_action(self):
        if self.ui.create_password_input.text() != self.ui.create_password_input_2.text():
            QMessageBox.information(self, "Error", "Passwords are not the same")
        else:
            s = shelve.open('databases/wallets_accounts.db')
            try:
                s[self.ui.create_login_input.text()] = hashlib.sha256(
                    bytes(self.ui.create_password_input.text(), 'utf-8')).digest().hex()
            finally:
                s.close()

            u = shelve.open('databases/' + self.ui.create_login_input.text() + '_keys.db')
            try:
                mnemo = Mnemonic("english")
                words = mnemo.generate(strength=256).encode('utf-8')
                sk_pem = generate_private_key(words + b'1').to_pem()

                cipher_seed = AES.new(pad(self.ui.create_password_input.text()).encode(), AES.MODE_EAX)
                ciphertext_seed, _ = cipher_seed.encrypt_and_digest(words)
                u['seed_phrase'] = ciphertext_seed + cipher_seed.nonce

                cipher = AES.new(pad(self.ui.create_password_input.text()).encode(), AES.MODE_EAX)
                ciphertext, _ = cipher.encrypt_and_digest(sk_pem)
                u[self.ui.create_login_input.text() + '1'] = ciphertext + cipher.nonce
            finally:
                u.close()

            QMessageBox.information(self, "Ok", "Account created\n\nYour seed phrase:\n\n" + words.decode('utf-8'))
            self.close()


class RestoreWindow(QWidget):
    def __init__(self):
        super(RestoreWindow, self).__init__()
        self.ui = Ui_restore_window()
        self.setFixedSize(530, 326)
        self.ui.setupUi(self)
        self.ui.restore_wallet_button.clicked.connect(self.restore_wallet_action)

    @QtCore.Slot()
    def restore_wallet_action(self):
        if self.ui.password_restore_input.text() != self.ui.password_restore_input_2.text():
            QMessageBox.information(self, "Error", "Passwords are not the same")
        else:
            s = shelve.open('databases/wallets_accounts.db')
            try:
                s[self.ui.login_restore_input.text()] = hashlib.sha256(
                    bytes(self.ui.password_restore_input.text(), 'utf-8')).digest().hex()
            finally:
                s.close()

            u = shelve.open('databases/' + self.ui.login_restore_input.text() + '_keys.db')
            try:

                words = self.ui.seed_phrase_input.text().encode('utf-8')
                sk_pem = generate_private_key(words + b'1').to_pem()
                # sk_pem = SigningKey.generate(curve=NIST256p, hashfunc=hashlib.sha256).to_pem()

                cipher_seed = AES.new(pad(self.ui.password_restore_input.text()).encode(), AES.MODE_EAX)
                ciphertext_seed, _ = cipher_seed.encrypt_and_digest(words)
                u['seed_phrase'] = ciphertext_seed + cipher_seed.nonce

                cipher = AES.new(pad(self.ui.password_restore_input.text()).encode(), AES.MODE_EAX)
                ciphertext, _ = cipher.encrypt_and_digest(sk_pem)
                u[self.ui.login_restore_input.text() + '1'] = ciphertext + cipher.nonce
            finally:
                u.close()

            QMessageBox.information(self, "Ok", "You've successfully restored your account")
            self.close()


class Response(QWidget):
    def __init__(self):
        super(Response, self).__init__()
        self.ui = Ui_Response()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.doc_cid = None
        self.signature = None
        self.nonce = None
        self.document_bytes = None
        self.data = None
        self.path = None
        self.sk = None
        self.find_document_window = None
        self.find_tx_window = None
        self.body = None
        self.sender_address = None
        self.vk = None
        self.pubkey = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.create_transaction_button.clicked.connect(self.create_transaction_action)
        self.ui.sign_transaction_button.clicked.connect(self.sign_transaction_action)
        self.ui.send_transaction_button.clicked.connect(self.send_transaction_action)
        self.ui.actionRequest_blocksHistory.triggered.connect(self.get_blockchain_action)
        self.ui.actionRequest_txHistory.triggered.connect(self.get_tx_history_action)
        self.ui.action_show_Find_tx_by_hash_window.triggered.connect(self.show_find_tx_window)
        self.ui.actionFind_document.triggered.connect(self.show_find_document_window)
        self.ui.actionAdd_KeyPair.triggered.connect(self.action_add_key_pair)
        self.ui.actionShow_my_seed_phrase.triggered.connect(self.show_my_seed_phrase_action)
        self.ui.comboBox.currentIndexChanged.connect(self.key_pair_changed)
        with shelve.open("databases/" + CURRENT_USER + "_keys.db") as db:
            for i in range(len(db.keys()) - 1):
                self.ui.comboBox.addItem(str(i + 1) + " pair")
        self.load_key_pair('1')

    @QtCore.Slot()
    def double_clicked(self, item):
        QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())

    @QtCore.Slot()
    def create_transaction_action(self):
        self.vk = self.sk.get_verifying_key()
        self.sender_address = hashlib.sha256(self.vk.to_pem()).digest()
        self.pubkey = self.vk.to_pem()
        self.ui.user_address.setText(self.sender_address.hex())

        self.select_document_action()

        self.body = {"SenderAddress": self.sender_address.hex(), "Data": self.data.hex(), "PubKey": self.pubkey.hex()}

        self.ui.tx_info_edit.setPlainText(json.dumps(self.body, indent=2))

    @QtCore.Slot()
    def show_find_tx_window(self):
        self.find_tx_window = FindTxWindow()
        self.find_tx_window.show()

    @QtCore.Slot()
    def show_find_document_window(self):
        self.find_document_window = FindDocumentWindow()
        self.find_document_window.show()

    @QtCore.Slot()
    def get_blockchain_action(self):
        channel = grpc.insecure_channel(SOCKET)
        client = grpcClient_pb2_grpc.InvoicerStub(channel)
        log.info(f"Connected to the Server : {SOCKET}")

        empty = grpcClient_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        response = client.GetBlockchain(empty)

        self.ui.response_window = Response()
        self.ui.response_window.show()
        self.ui.response_window.ui.text_field.setPlainText(response.response)

        channel.close()

    @QtCore.Slot()
    def send_transaction_action(self):
        try:
            api = ipfsApi.Client('127.0.0.1', 5001)
            doc_cid = api.add(self.path)[0]['Hash']
            self.doc_cid = str.encode(doc_cid)
            self.body['CID'] = doc_cid

            self.ui.tx_info_edit.setPlainText(json.dumps(self.body, indent=2))

            channel = grpc.insecure_channel(SOCKET)
            client = grpcClient_pb2_grpc.InvoicerStub(channel)
            log.info(f"Connected to the Server : {SOCKET}")

            response = client.AddTxToBlockchain(grpcClient_pb2.CreateTx(
                senderAddress=self.sender_address,
                data=self.data,
                pubKey=self.pubkey,
                signature=self.signature,
                nonce=self.nonce,
                cid=self.doc_cid,
            ))
            QMessageBox.information(self, "Response", response.response)
            channel.close()
        except Exception as e:
            QMessageBox.information(self, "Error", str(e))

    @QtCore.Slot()
    def sign_transaction_action(self):
        self.signature = self.sk.sign(b''.join([self.sender_address, self.data]), hashfunc=hashlib.sha256,
                                      sigencode=sigencode_der)

        self.nonce = math.trunc(time.time())
        self.body["Signature"] = self.signature.hex()
        self.body["Nonce"] = self.nonce
        self.ui.tx_info_edit.setPlainText(json.dumps(self.body, indent=2))

    @QtCore.Slot()
    def select_document_action(self):
        filename = QFileDialog.getOpenFileName(self, 'Select document', filter="*.pdf")
        path = filename[0]
        self.path = path

        h = hashlib.sha256()
        with open(path, 'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)

        file = open(path, "rb")
        self.document_bytes = file.read()
        file.close()

        self.data = h.digest()

    @QtCore.Slot()
    def get_tx_history_action(self):
        channel = grpc.insecure_channel(SOCKET)
        client = grpcClient_pb2_grpc.InvoicerStub(channel)
        log.info(f"Connected to the Server : {SOCKET}")

        response = client.GetUserTxHistory(grpcClient_pb2.User(
            senderAddress=self.sender_address,
        ))

        self.ui.response_window = Response()
        self.ui.response_window.show()
        self.ui.response_window.ui.text_field.setPlainText(response.response)
        channel.close()

    @QtCore.Slot()
    def show_my_seed_phrase_action(self):
        global CURRENT_USER, USER_PASSWORD

        with shelve.open("databases/" + CURRENT_USER + "_keys.db") as db:
            value = db['seed_phrase']

        nonce = value[len(value) - 16:]
        seed_encoded = value[:len(value) - 16]
        cipher = AES.new(pad(USER_PASSWORD).encode(), AES.MODE_EAX, nonce=nonce)
        seed_decoded = cipher.decrypt(seed_encoded)
        QMessageBox.information(self, "Ok", "Your seed phrase:\n\n" + seed_decoded.decode('utf-8'))

    @QtCore.Slot()
    def key_pair_changed(self, index):
        self.load_key_pair(index + 1)

    @QtCore.Slot()
    def action_add_key_pair(self):
        global CURRENT_USER, USER_PASSWORD

        with shelve.open("databases/" + CURRENT_USER + "_keys.db") as db:
            value = db['seed_phrase']

        nonce = value[len(value) - 16:]
        seed_encoded = value[:len(value) - 16]
        cipher = AES.new(pad(USER_PASSWORD).encode(), AES.MODE_EAX, nonce=nonce)
        seed_decoded = cipher.decrypt(seed_encoded)

        # sk_pem = SigningKey.generate(curve=NIST256p, hashfunc=hashlib.sha256).to_pem()
        sk_pem = generate_private_key(seed_decoded + str(self.ui.comboBox.count() + 1).encode('utf-8')).to_pem()

        cipher = AES.new(pad(USER_PASSWORD).encode(), AES.MODE_EAX)
        ciphertext, _ = cipher.encrypt_and_digest(sk_pem)

        with shelve.open("databases/" + CURRENT_USER + "_keys.db") as db:
            db[CURRENT_USER + str(self.ui.comboBox.count() + 1)] = ciphertext + cipher.nonce

        self.ui.comboBox.addItem(str(self.ui.comboBox.count() + 1) + " pair")
        QMessageBox.information(self, "Ok", "New key pair created")

    def load_key_pair(self, index):
        global CURRENT_USER, USER_PASSWORD
        with shelve.open("databases/" + CURRENT_USER + "_keys.db") as db:
            value = db[CURRENT_USER + str(index)]
            sk_encoded = value[:227]
            nonce = value[227:]
            cipher = AES.new(pad(USER_PASSWORD).encode(), AES.MODE_EAX, nonce=nonce)
            sk_decoded = cipher.decrypt(sk_encoded)
            self.sk = SigningKey.from_pem(sk_decoded.decode())
            self.vk = self.sk.get_verifying_key()
            self.sender_address = hashlib.sha256(self.vk.to_pem()).digest()
            self.pubkey = self.vk.to_pem()
            self.ui.user_address.setText(self.sender_address.hex())


def pad(s):
    block_size = 16
    remainder = len(s) % block_size
    padding_needed = block_size - remainder
    return s + padding_needed * ' '


def unpad(s):
    return s.rstrip()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('resources/window_icon.png'))

    login = LoginWindow()
    login.show()

    sys.exit(app.exec())
