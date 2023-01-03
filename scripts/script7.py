import re


def cond1(input_string):
    pattern = "^[456]{1}"
    match = re.search(pattern, input_string)
    if match is not None:
        return True
    else:
        return False


def cond2(input_string):
    digit_count = 0
    for char in input_string:
        if char.isdigit():
            digit_count += 1
    if digit_count == 16:
        return True
    else:
        return False


def cond3(input_string):
    pattern = "[^0-9\-]"
    match = re.search(pattern, input_string)
    if match is not None:
        return False
    else:
        return True


def cond4(input_string):
    string = input_string.replace("-", "")
    # print(string)
    pattern = r"(\d)\1{3}"
    match = re.search(pattern, string)
    if match is not None:
        return False
    else:
        return True


def cond5(input_string):
    if cond6(input_string):
        str_list = input_string.split("-")
        for item in str_list:
            # print(item)
            if len(item) != 4:
                return False
            else:
                return True
    else:
        return True


def cond6(input_string):
    hyphen_count = 0
    for char in input_string:
        if char == "-":
            hyphen_count += 1
    if hyphen_count == 3:
        return True
    else:
        return False


def cond7(input_string):
    hyphen_count = 0
    for char in input_string:
        if char == "-":
            hyphen_count += 1
    if hyphen_count < 4:
        return True
    else:
        return False


def isValid(input_string):
    if cond1(input_string) and cond2(input_string) and cond3(input_string) and cond4(input_string) and cond5(input_string) and cond7(input_string):
        return True
    else:
        return False


def main():
    cc_list = []
    for i in range(int(input())):
        cc_list.append(input())
    # print(cc_list)
    for cc in cc_list:
        if isValid(cc):
            print("Valid")
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
