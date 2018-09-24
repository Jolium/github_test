#!/usr/bin/env python3

"""
Target Password Generator
Generates passwords with the target in mind!
"""

password_list = []
min_char = 8
max_char = 12
num_before = False
num_after = True
num_before_and_after = False
upper_and_lower = False
exp = 4


def print_header():
    print("")
    print("1100101001110100110011001000110001101011001101000110101001110110")
    print("  00100010101011011101011  TARGET-PASSGEN  01001011011000101110110")
    print("    0111001000010111001100110101100111011011001000101010011101001101")
    print("")


def yes_or_no():
    global nb
    global na
    global nba
    global ul

    if num_before:
        nb = "y"
    if not num_before:
        nb = "n"

    if num_after:
        na = "y"
    if not num_after:
        na = "n"

    if num_before_and_after:
        nba = "y"
    if not num_before_and_after:
        nba = "n"

    if upper_and_lower:
        ul = "y"
    if not upper_and_lower:
        ul = "n"


def settings():
    yes_or_no()
    print("\n\n====================================================================")
    print("                              Settings")
    print("====================================================================\n")
    print("[0] Exit settings")
    print("[1] Passwords minimum length (default = 8)                    [1]:%d" % min_char)
    print("[2] Passwords maximum length (default = 12)                   [2]:%d" % max_char)
    print("[3] Passwords with numbers before (default = n)               [3]:%s" % nb)
    print("[4] Passwords with numbers after (default = y)                [4]:%s" % na)
    print("[5] Passwords with numbers before and after (default = n)     [5]:%s" % nba)
    print("[6] Passwords with capital/small letters (default = n)        [6]:%s" % ul)
    print("[7] Length of numbers (default = 4)                           [7]:%d" % exp)
    print("\n====================================================================\n")
    user_settings = int(input("Choose settings number (0-7): "))
    if 0 > user_settings > 7:
        print("Invalid value!")
        settings()
    else:
        user_settings_choice(user_settings)
        return


def user_settings_choice(user_settings):
    global min_char
    global max_char
    global num_before
    global num_after
    global num_before_and_after
    global upper_and_lower
    global exp

    if user_settings == 0:
        print("[0] Exit settings\n")
        return

    elif user_settings == 1:
        while True:
            print("\n" + "[1] Passwords minimum length (default = 8)")
            value1 = int(input("    Set the new value (1 - 12): "))
            if value1 > max_char:
                print("Invalid value! Minimum length cannot be higher than maximum length.")
            elif 1 <= value1 <= 12:
                min_char = value1
                settings()
                return
            else:
                print("Invalid value!")

    elif user_settings == 2:
        while True:
            print("\n" + "[2] Passwords maximum length (default = 12)")
            value2 = int(input("    Set the new value (8 - 18): "))
            if value2 < min_char:
                print("Invalid value! Maximum length cannot be lower than minimum length.")
            elif 8 <= value2 <= 18:
                max_char = value2
                settings()
                return
            else:
                print("Invalid value!")

    elif user_settings == 3:
        while True:
            print("\n" + "[3] Passwords with numbers before (default = n)")
            value3 = str(input("    Set to 'y' (yes) or 'n' (no): ").lower())
            if value3 == "y":
                num_before = True
                settings()
                return
            elif value3 == "n":
                num_before = False
                settings()
                return
            else:
                print("Invalid input!")

    elif user_settings == 4:
        while True:
            print("\n" + "[4] Passwords with numbers after (default = y)")
            value4 = str(input("    Set to 'y' (yes) or 'n' (no): ").lower())
            if value4 == "y":
                num_after = True
                settings()
                return
            elif value4 == "n":
                num_after = False
                settings()
                return
            else:
                print("Invalid input!")

    elif user_settings == 5:
        while True:
            print("\n" + "[5] Passwords with numbers before and after (default = n)")
            value5 = str(input("    Set to 'y' (yes) or 'n' (no): ").lower())
            if value5 == "y":
                num_before_and_after = True
                settings()
                return
            elif value5 == "n":
                num_before_and_after = False
                settings()
                return
            else:
                print("Invalid input!")

    elif user_settings == 6:
        while True:
            print("\n" + "[6] Passwords with capital/small letters (default = n)")
            value6 = str(input("    Set to 'y' (yes) or 'n' (no): ").lower())
            if value6 == "y":
                upper_and_lower = True
                settings()
                return
            elif value6 == "n":
                upper_and_lower = False
                settings()
                return
            else:
                print("Invalid input!")

    elif user_settings == 7:
        while True:
            print("\n" + "[7] Length of numbers (default = 4)")
            value7 = int(input("    Set the new value (0 - 8): "))
            if 0 <= value7 <= 8:
                exp = value7
                settings()
                return
            else:
                print("Invalid value!")


def user_choice():
    choice = ""

    while choice != "d" and choice != "c":
        choice = str(input("Press 'd' to default settings or 'c' to change settings: ").lower())
        if choice == "d":
            break
        elif choice == "c":
            settings()
        else:
            print("Invalid option!")


def fun_x(password):
    e = exp

    for x in range(4, 0, -1):
        r = 10 ** e
        e -= 1

        for num in range(r):
            if num_before:
                password_list.append(str(num).zfill(x) + str(password))
                if upper_and_lower:
                    password_list.append(str(num).zfill(x) + str(password.lower()))
                    password_list.append(str(num).zfill(x) + str(password.upper()))

            if num_after:
                password_list.append(str(password) + str(num).zfill(x))
                if upper_and_lower:
                    password_list.append(str(password.lower()) + str(num).zfill(x))
                    password_list.append(str(password.upper()) + str(num).zfill(x))

            if num_before_and_after:
                password_list.append(str(num).zfill(x) + str(password) + str(num).zfill(x))
                if upper_and_lower:
                    password_list.append(str(num).zfill(x) + str(password.lower()) + str(num).zfill(x))
                    password_list.append(str(num).zfill(x) + str(password.upper()) + str(num).zfill(x))

    make_pass_list()
    enter_words()


def enter_words():
    user_input = str(input("Enter word ('//' to stop): "))

    if user_input != "" and user_input != "//":
        fun_x(user_input)
        return user_input
    elif user_input == "":
        print("No word entered!")
    else:
        return


def make_pass_list():
    global password_list
    password_list2 = []
    txt = password_list[:]

    for word in txt:
        if min_char <= len(word) <= max_char:
            password_list2.append(word)

    file = open("Passwords_list.txt", "a+")
    file.write("\n".join(map(str, password_list2)))
    password_list = []


print_header()
user_choice()
enter_words()

exit()
