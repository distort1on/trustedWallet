import sys
import hashlib
import base64
import shelve
import json
import grpc
import logging as log
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog
from PySide6 import QtCore, QtGui
from PyUI_Files.ui_MainWindow import Ui_MainWindow
from PyUI_Files.ui_ResponseWindow import Ui_Response
from PyUI_Files.ui_LoginWindow import Ui_login_window
from PyUI_Files.ui_RegisterWindow import Ui_register_window
from ecdsa import NIST256p, SigningKey
from ecdsa.util import sigencode_der
import grpcClient_pb2
import grpcClient_pb2_grpc


class Login_Window(QWidget):
    def __init__(self):
        super(Login_Window, self).__init__()
        self.ui = Ui_login_window()
        self.setFixedSize(530, 326)
        self.ui.setupUi(self)
        self.ui.register_button.clicked.connect(self.show_register_window)
        self.ui.login_button.clicked.connect(self.show_main_window)

    @QtCore.Slot()
    def show_register_window(self):
        self.register_window = Register_Window()
        self.register_window.show()

    @QtCore.Slot()
    def show_main_window(self):
        s = shelve.open('databases/wallets_accounts.db')
        try:
            if s[self.ui.login_input.text()] == hashlib.sha256(
                    bytes(self.ui.password_input.text(), 'utf-8')).digest().hex():
                self.main_window = MainWindow()
                self.close()
                self.main_window.show()
        except KeyError:
            msg = QMessageBox()
            msg.setText("Wrong login or password")
            msg.exec()
        finally:
            s.close()


class Register_Window(QWidget):
    def __init__(self):
        super(Register_Window, self).__init__()
        self.ui = Ui_register_window()
        self.setFixedSize(530, 326)
        self.ui.setupUi(self)
        self.ui.register_button.clicked.connect(self.create_wallet_action)

    @QtCore.Slot()
    def create_wallet_action(self):
        if self.ui.create_password_input.text() != self.ui.create_password_input_2.text():
            msg = QMessageBox()
            msg.setText("Passwords are not the same.")
            msg.exec()
        else:
            s = shelve.open('databases/wallets_accounts.db')
            try:
                s[self.ui.create_login_input.text()] = hashlib.sha256(
                    bytes(self.ui.create_password_input.text(), 'utf-8')).digest().hex()
            finally:
                s.close()
            msg = QMessageBox()
            msg.setText("Account created.")
            msg.exec()
            self.close()


class Response(QWidget):
    def __init__(self):
        super(Response, self).__init__()
        self.ui = Ui_Response()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.create_transaction_button.clicked.connect(self.create_transaction_action)
        self.ui.get_blockchain_button.clicked.connect(self.get_blockchain_action)
        self.ui.sign_transaction_button.clicked.connect(self.sign_transaction_action)
        self.ui.send_transaction_button.clicked.connect(self.send_transaction_action)
        self.ui.select_document_button.clicked.connect(self.select_document_action)
        self.ui.get_txHistory_button.clicked.connect(self.get_TxHistory_action)
        # self.ui.listWidget.addItem(":tx1")
        # self.ui.listWidget.addItem(":tx2")
        # self.ui.listWidget.addItem(":tx3")
        # self.ui.listWidget.addItem(":tx4")
        #
        # self.ui.listWidget.itemDoubleClicked.connect(self.double_clicked)

        # self.ui.textEdit.setText("MC5wIGd5dANsVXuiZ4fGI7awLPstDqsUOPLFMItJ05U=")

        # pubTest = base64.b64decode(str.encode(self.body["PubKey"]))
        # v_test = VerifyingKey.from_pem(pubTest.decode('utf-8'))
        #
        # sig_test = base64.b64decode(str.encode(self.body["Signature"]))
        # data_test = hashlib.sha256(b'hello').digest()
        #
        # print(sig_test)
        # print(v_test.verify(sig_test, data_test, hashfunc=hashlib.sha256, sigdecode=sigdecode_der))

        # sk_pem = sk.to_pem()
        # vk_pem = vk.to_pem()

    @QtCore.Slot()
    def double_clicked(self, item):
        QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())

    @QtCore.Slot()
    def create_transaction_action(self):
        self.sk = SigningKey.generate(curve=NIST256p, hashfunc=hashlib.sha256)
        self.vk = self.sk.get_verifying_key()
        self.sender_address = hashlib.sha256(self.vk.to_string()).digest()
        self.ui.user_address.setText(self.sender_address.hex())
        self.pubkey = self.vk.to_pem()

        self.body = {}
        # self.body["SenderAddress"] = self.sender_address.hex()
        self.body["SenderAddress"] = base64.b64encode(self.sender_address).decode('utf-8')
        self.body["Data"] = self.data.hex()
        self.body["PubKey"] = self.pubkey.hex()

        # self.body = {
        #     "SenderAddress": base64.b64encode(self.sender_address).decode('utf-8'),
        #     "Data": base64.b64encode(self.data).decode('utf-8'),
        #     "PubKey": base64.b64encode(self.pubkey).decode('utf-8'),
        #     "Signature": base64.b64encode(self.signature).decode('utf-8'),
        # }

        self.ui.tx_info_edit.setPlainText(json.dumps(self.body, indent=2))

    @QtCore.Slot()
    def get_blockchain_action(self):
        socket = 'localhost:8089'
        channel = grpc.insecure_channel(socket)
        client = grpcClient_pb2_grpc.InvoicerStub(channel)
        log.info(f"Connected to the Server : {socket}")

        empty = grpcClient_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        response = client.GetBlockchain(empty)

        self.ui.response_window = Response()
        self.ui.response_window.show()
        self.ui.response_window.ui.text_field.setPlainText(response.response)

        channel.close()
        # vk_pem = "-----BEGIN EC PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEiHLwzGZVS14sn9p6TnfAS9O8MvJD\nn181ONxzl2QlVcxM6cz2nbDfRX6q3raLXeCBHzbqh4PgpZt0OxcKgv/FKw==\n-----END EC PUBLIC KEY-----"
        # vk = VerifyingKey.from_pem(sk_pem, hashfunc=hashlib.sha256)

    @QtCore.Slot()
    def send_transaction_action(self):
        # url = 'http://localhost:8080/blockchain/'
        # x = requests.post(url, json=self.body)
        # print(x.status_code)

        socket = 'localhost:8089'
        channel = grpc.insecure_channel(socket)
        client = grpcClient_pb2_grpc.InvoicerStub(channel)
        log.info(f"Connected to the Server : {socket}")

        response = client.AddTxToBlockchain(grpcClient_pb2.CreateTx(
            senderAddress=self.sender_address,
            data=self.data,
            pubKey=self.pubkey,
            signature=self.signature,
            documentBytes=self.document_bytes,
        ))

        QMessageBox.information(self, "Response", response.response)

        channel.close()

    @QtCore.Slot()
    def sign_transaction_action(self):
        self.signature = self.sk.sign(b''.join([self.sender_address, self.data]), hashfunc=hashlib.sha256,
                                      sigencode=sigencode_der)
        self.body["Signature"] = self.signature.hex()
        self.ui.tx_info_edit.setPlainText(json.dumps(self.body, indent=2))

    @QtCore.Slot()
    def select_document_action(self):
        filename = QFileDialog.getOpenFileName(self, 'Select document', filter="*.pdf")
        path = filename[0]

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
    def get_TxHistory_action(self):
        socket = 'localhost:8089'
        channel = grpc.insecure_channel(socket)
        client = grpcClient_pb2_grpc.InvoicerStub(channel)
        log.info(f"Connected to the Server : {socket}")

        response = client.GetUserTxHistory(grpcClient_pb2.User(
            senderAddress=self.sender_address,
        ))

        self.ui.response_window = Response()
        self.ui.response_window.show()
        self.ui.response_window.ui.text_field.setPlainText(response.response)
        channel.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('resources/window_icon.png'))

    login = Login_Window()
    login.show()

    sys.exit(app.exec())
