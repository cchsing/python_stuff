import script2 as handleFile
import json
import os
import sys
import time
import datetime
import base64


class block:
    def __init__(self, data, previous_block_hash):
        self.data = data
        self.previous_block_hash = previous_block_hash


def main():
    print("Script Run...")

    for i in range(0, 10, 1):
        timestamp = str(datetime.datetime.now())
        data = {
            "transaction": "I get RM" + str(i) + f" {timestamp}",
        }
        filename = "./transactionData" + str(i)
        handleFile.dict2File(filename, data)
    
    username = "user1"
    password = "pwd123456"
    username_bytes = bytes(username, "utf-8")
    print(str(username_bytes))
    usr_encode64 = base64.b64encode(username_bytes)
    print(str(usr_encode64))
    usr_decodeascii = usr_encode64.decode("ascii")
    print(str(usr_decodeascii))

if __name__ == "__main__":
    main()
