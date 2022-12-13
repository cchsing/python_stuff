import json
# Function to write to file


def write_File(file, text):
    with open(file, "w") as f:
        f.write(text)
        print("Written to " + file)


def append_File(file, text):
    with open(file, "a") as f:
        f.write(text)
        print("Append to " + file)


def read_File(file):
    with open(file, "r") as f:
        print("Read from " + file)
        return f.read()

# Function to output JSON to A New File


def dict2File(file, data):
    temp = json.dumps(data, indent=4)
    write_File(file, temp)


def file2Dict(file):
    temp = read_File(file)
    return json.loads(temp)
