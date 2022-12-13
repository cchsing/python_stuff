import script2 as handleFile
import json
import os
import sys
import time
import datetime


class block:
    def __init__(self, data, previous_block_hash):
        self.data = data
        self.previous_block_hash = previous_block_hash


def main():
    print("Script Run...")

    for i in range(0, 10, 1):
        timestamp = str(datetime.datetime.now())
        data = {
            "transaction": "I get RM" + str(i),
        }
        filename = "transactionData" + str(i)
        handleFile.dict2File(filename, data)


if __name__ == "__main__":
    main()
