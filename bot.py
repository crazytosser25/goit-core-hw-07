"""imports"""
import re
from pathlib import Path
from app.main import AddressBook
try:
    from app.color_txt import ColorTxt
    COLOR = True
except ImportError:
    from app.standard_txt import StandardTxt
    COLOR = False


def check_txt(arg):
    output = ColorTxt() if COLOR else StandardTxt()
    return output(arg)

def parse_input(user_input: str) -> tuple:
    """Split the user's input into command and arguments.
        
    Args:
        user_input (str): User input string.

    Returns:
        tuple: A tuple containing the command and its arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    cmd = re.sub("[^A-Za-z]", "", cmd)
    return cmd, *args

def main():
    """This code is designed to create a simple command-line interface (CLI)
    application that interacts with a contacts database. The user can perform
    actions such as adding, changing, and viewing contact information. The CLI
    uses the 'colorama' module to add colors to the output strings for better
    readability.
    """
    # database = Path("contacts.json")
    contacts = AddressBook()

    print(check_txt('greeting'))

    while True:
        user_input = input(check_txt('placeholder'))
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                # write_file(database, contacts)
                print(check_txt('bye'))
                break
            case "hello":
                print(check_txt('hello'))
            case "help":
                print(check_txt('help'))
            case "add":
                print(f"{Fore.YELLOW}{add_contact(contacts, args)}\n")
            case "change":
                print(f"{Fore.YELLOW}{change_contact(contacts, args)}\n")
            case "del":
                print(f"{Fore.YELLOW}{delete_contact(contacts, args)}\n")
            case "phone":
                print(f"{show_phone(contacts, args)}\n")
            case "all":
                print(show_all(contacts))
            case _:
                print(check_txt('invalid command'))


if __name__ == "__main__":
    main()

