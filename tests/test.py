from ecdsa import NIST256p, SigningKey
from ecdsa.util import sigencode_der, randrange_from_seed__trytryagain
import hashlib
from random import randbytes, randint
import random
import time
import math
import grpcClient_pb2
import grpcClient_pb2_grpc
import grpc
from tabulate import tabulate
from multiprocessing import Process


def generate_private_key(seed):
    secexp = randrange_from_seed__trytryagain(seed, NIST256p.order)
    return SigningKey.from_secret_exponent(secexp, curve=NIST256p, hashfunc=hashlib.sha256())


def generate_transactions(num_of_transactions, num_of_incorrect_transactions):
    tx_list = []
    random.seed()

    for i in range(num_of_transactions - num_of_incorrect_transactions):
        tx = {}
        sk = SigningKey.generate(curve=NIST256p, hashfunc=hashlib.sha256)
        vk = sk.get_verifying_key()

        sender_address = hashlib.sha256(vk.to_pem()).digest()
        pubkey = vk.to_pem()
        data = randbytes(32)
        signature = sk.sign(b''.join([sender_address, data]), hashfunc=hashlib.sha256,
                            sigencode=sigencode_der)
        nonce = math.trunc(time.time())
        doc_cid = randbytes(46)

        tx["SenderAddress"] = sender_address
        tx["Data"] = data
        tx["PubKey"] = pubkey
        tx["Signature"] = signature
        tx["Nonce"] = nonce
        tx["CID"] = doc_cid
        tx_list.append([tx, "None"])

    for i in range(num_of_incorrect_transactions):
        tx = {}
        sk = SigningKey.generate(curve=NIST256p, hashfunc=hashlib.sha256)
        vk = sk.get_verifying_key()

        sender_address = hashlib.sha256(vk.to_pem()).digest()
        pubkey = vk.to_pem()
        data = randbytes(32)
        signature = sk.sign(b''.join([sender_address, data]), hashfunc=hashlib.sha256,
                            sigencode=sigencode_der)
        nonce = math.trunc(time.time())
        doc_cid = randbytes(46)

        tx["SenderAddress"] = sender_address
        tx["Data"] = data
        tx["PubKey"] = pubkey
        tx["Signature"] = signature
        tx["Nonce"] = nonce
        tx["CID"] = doc_cid

        sk_wrong = SigningKey.generate(curve=NIST256p, hashfunc=hashlib.sha256)
        vk_wrong = sk_wrong.get_verifying_key()
        pubkey_wrong = vk_wrong.to_pem()
        signature_wrong = sk_wrong.sign(b''.join([sender_address, data]), hashfunc=hashlib.sha256,
                                        sigencode=sigencode_der)

        match i % 5:
            case 0:
                tx["SenderAddress"] = randbytes(32 + randint(10, 50))
                tx_list.append([tx, "SenderAddress"])
            case 1:
                tx["Data"] = randbytes(32 + randint(10, 50))
                tx_list.append([tx, "Data"])
            case 2:
                tx["PubKey"] = pubkey_wrong
                tx_list.append([tx, "PubKey"])
            case 3:
                tx["Signature"] = signature_wrong
                tx_list.append([tx, "Signature"])
            case 4:
                tx["Nonce"] = math.trunc(time.time()) + 10000000000
                tx_list.append([tx, "Nonce"])
            case 5:
                tx["CID"] = randbytes(46 + randint(10, 50))
                tx_list.append([tx, "CID"])

    return tx_list


def send_transaction(tx):
    socket = 'localhost:8083'
    channel = grpc.insecure_channel(socket)
    client = grpcClient_pb2_grpc.InvoicerStub(channel)

    response = client.AddTxToBlockchain(grpcClient_pb2.CreateTx(
        senderAddress=tx["SenderAddress"],
        data=tx["Data"],
        pubKey=tx["PubKey"],
        signature=tx["Signature"],
        nonce=tx["Nonce"],
        cid=tx["CID"],
    ))

    return response.response


if __name__ == '__main__':
    tx_list = generate_transactions(500, 250)
    random.shuffle(tx_list)
    data = []
    t_start = time.time()
    for i in range(len(tx_list)):
        response = str(send_transaction(tx_list[i][0])).splitlines()[1]

        if response.startswith("Tx hash"):
            data.append([i + 1, tx_list[i][1], "None"])
        else:
            data.append([i + 1, tx_list[i][1], response])

    t_finished = time.time()

    print(tabulate(data, headers=["tx_num", "problem", "received problem"]))
    print(t_finished - t_start)
    # process = []
    # print(multiprocessing.Pool())
    # for i in range(0, 0):
    #     p = Process(target=generate_transactions)
    #     process.append(p)
    #     p.start()
    #
    # for t in process:
    #     t.join()
    #
    # print("DONE")
