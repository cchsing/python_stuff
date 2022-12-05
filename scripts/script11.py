## Converting the csv to list 

import csv

class csv_to_list_1:

    def __init__(self, filename, newline, encoding):
        self.filename = filename
        self.newline = newline
        self.encoding = encoding

    

    def convert(self):
        with open(self.filename, newline=self.newline, encoding=self.encoding) as f:
            reader = csv.reader(f)
            data = list(reader)
        return data

def main(*args):
    pass

if __name__ == "__main__":
    main()