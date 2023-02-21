import argparse
import shutil
import sys
import os.path
import winreg


parser = argparse.ArgumentParser()
parser.add_argument('-m', "--move", help="Input action: create, delete...",
                    required=True, type=str,
                    choices=["create", "delete", "write", "read", "copy",
                             "rename", "create_key", "delete_key", "val_set"])
parser.add_argument('-pth', "--path", help="Input path to file",
                    required=False, type=str)
parser.add_argument('-txt', "--text", help="Input text",
                    required=False, type=str)
args = parser.parse_args()


def create():
    """
    create_file
    """
    path = args.path
    if os.path.isfile(path):
        sys.exit("File already exists")
    else:
        with open(path, "w+") as f:
            print("Сreate file successful")

    sys.exit()


def delete_file():
    path = args.path
    if os.path.isfile(path):
        os.remove(path)
        sys.exit()
    else:
        sys.exit('Path is not a file or not found')


def write_file():
    path = args.path
    if args.text is None:
        sys.exit('Text not inpunt!')

    if os.path.isfile(path):
        with open(path, "a") as file_1:
            file_1.write(args.text)
    else:
        print('Path is not a file or not found')
    sys.exit()


def read_file():
    path = args.path
    if os.path.isfile(path):
        with open(path, "r") as file_1:
            print(file_1.read())
    else:
        print('Path is not a file or not found')
    sys.exit()


def copy_file():
    original = args.path
    target = args.text
    if args.text is None:
        sys.exit('One of path not input')
    if os.path.isfile(original) and os.path.exists(target):
        shutil.copy2(original, target)
    else:
        print('Path is not a file or not found')
    sys.exit()


def rename():
    path = args.path
    new_name = args.text
    if os.path.isfile(path) and not os.path.exists(new_name):
        os.rename(path, new_name)
    else:
        print('Path is not a file or new name is folder')
    sys.exit()


def create_key():
    path = r'SOFTWARE\REG123'
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, path)
    except OSError:
        print("Error with create key")


def delete_key():
    path = r'SOFTWARE\REG123'
    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, path)
    except OSError:
        print("Error with delete key")


def val_set():
    path = r'SOFTWARE\REG123'
    key_name = "TEST_PY"
    new_val = "My_value_123"
    key_type = winreg.REG_SZ
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, path)
        winreg.SetValueEx(key, key_name, 0, key_type, new_val)
        print("Value set correct")
    except OSError as e:
        print(e)


def parsing():
    match args.move:
        case "create":
            create()
        case "delete":
            delete_file()
        case "write":
            write_file()
        case "read":
            read_file()
        case "copy":
            copy_file()
        case "rename":
            rename()
        case "create_key":
            create_key()
        case "delete_key":
            delete_key()
        case "val_set":
            val_set()
        case _:
            sys.exit('Error -1')


def __main__():
    if (args.move in ["create", "delete", "write", "read", "copy", "rename"]):
        if args.path is None:
            sys.exit("Path not found")
            
    parsing()


if __name__ == "__main__":
    __main__()
