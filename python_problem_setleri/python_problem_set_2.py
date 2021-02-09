import re


def check(extension_length, mail: str):
    global extension, extension_parts, user_name, extension_length_check

    length_check = 0
    name_check = 0
    extension_length_check = 0
    extentions_count = 0
    mail_truth = 0

    if 0 < extension_length <= 3:
        extension_length_check = 1

    try:
        user_name, extension = mail.split("@")
        mail_truth = 1
    except ValueError:
        mail_truth = 0

    try:
        extension_parts = extension.split(".")
    except Exception as err:
        pass

    try:
        if 0 < len(extension_parts) <= 3:
            extentions_count = 1
    except:
        pass

    try:
        if len(extension_parts[1]) == extension_length:
            length_check = 1
    except:
        pass

    try:
        check_username = re.match(r"(^[a-zA-Z0-9_.+-]+$)", user_name)  # @[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
        if check_username:
            name_check = 1
    except:
        pass

    return name_check == length_check == extension_length_check == extentions_count == mail_truth


while True:
    extension_l = int(input("Uzantı uzunluğunu giriniz: "))
    mail = input("Mail adresinizi giriniz: ")
    if check(extension_l, mail):
        print("Mail adresi uygundur!")
    else:
        print("Mail adresi uygun değildir!")