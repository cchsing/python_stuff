
import re


def cond1(input_string):
    uppercase_count = 0
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
    if uppercase_count >= 2:
        return True
    else:
        return False


def cond2(input_string):
    digit_count = 0
    for char in input_string:
        if char.isdigit():
            digit_count += 1
    if digit_count >= 3:
        return True
    else:
        return False


def cond3(input_string):
    pattern = "[^a-zA-Z0-9]"
    match = re.search(pattern, input_string)
    if match is not None:
        return False
    else:
        return True


def cond4(input_string):
    x = []
    for char in input_string:
        if (char not in x) and (input_string.count(char) > 1):
            x.append(char)
    if len(x) > 0:
        return False
    else:
        return True


def cond5(input_string):
    if len(input_string) == 10:
        return True
    else:
        return False


def isValid(input_string):
    if cond1(input_string) and cond2(input_string) and cond3(input_string) and cond4(input_string) and cond5(input_string):
        return True
    else:
        return False


def main():
    uid_list = []
    for i in range(int(input())):
        uid_list.append(input())
    # print(uid_list)
    for uid in uid_list:
        if isValid(uid):
            print("Valid")
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
