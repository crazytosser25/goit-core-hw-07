"""imports"""
try:
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
    COLOR = True
except ImportError:
    COLOR = False


def check_txt(arg):
    """_summary_

    Args:
        arg (_type_): _description_

    Returns:
        _type_: _description_
    """
    output = ColorTxt() if COLOR else StandardTxt()
    return output(arg)

class ColorTxt:
    """Colorized output in case of user input, output and mistakes."""
    def __call__(self, request):
        return self.formatted_txt(request)

    def formatted_txt(self, request: str) -> str:
        """Colorized output in case of user input, output and mistakes.

    This function takes a single argument, `request` which is a string
    representing a message. It returns a formatted string with colorful
    terminal output based on the given request.

    Args:
        request (str): The message to be displayed.

    Returns:
        str: A formatted string containing the error message in colorful
        terminal output.
    """
        match request:
            case 'greeting':
                return f"\n{Fore.YELLOW}Welcome to the assistant bot!\n" \
                "(enter 'help' for list of commands)\n"
            case 'placeholder':
                return f"Enter a command: {Fore.BLUE}"
            case 'bye':
                return f"{Fore.YELLOW}Good bye!\n"
            case 'hello':
                return f"{Fore.YELLOW}How can I help you?\n"
            case 'invalid command':
                return f"{Fore.RED}Invalid command.\n"
            case 'phone not in contacts':
                return f"{Fore.RED}Invalid Name.\n{Fore.YELLOW}This contact " \
                    "doesn't exist."
            case 'contact exists':
                return f"{Fore.RED}Invalid Name.\n{Fore.YELLOW}This contact " \
                    "already exists."
            case 'no name for search':
                return f"{Fore.RED}Invalid data.\n{Fore.YELLOW}You must " \
                    "give me Name."
            case 'invalid phone':
                return f"{Fore.RED}Invalid Phone-number.\n{Fore.YELLOW}Must " \
                    "be 10 numbers."
            case 'invalid args':
                return f"{Fore.RED}Invalid data.\n{Fore.YELLOW}You must " \
                    "give me Name and Phone-number."
            case 'help':
                return "'add [name] [phone]'\tto add new contact " \
                "(phone must be 10 digits).\n" \
                "'all'\t\t\tto review all contacts.\n" \
                "'change [name] [phone]'\tto change contact's phone number.\n" \
                "'del [name]'\t\tto delete contact from list.\n" \
                "'phone [name]'\t\tto review contact's phone number.\n" \
                "'close' or 'exit'\tto exit assistant.\n"


class StandardTxt:
    """Non-colorized output in case of user input, output and mistakes.
    """
    def __call__(self, request):
        return self.formatted_txt(request)

    def formatted_txt(self, request: str) -> str:
        """Non-colorized output in case of user input, output and mistakes.

    This function takes a single argument, `request` which is a string
    representing a message. It returns a formatted string based on the given
    request.

    Args:
        request (str): The message to be displayed.

    Returns:
        str: A formatted string containing the error message in colorful
        terminal output.
    """
        match request:
            case 'greeting':
                return "\nWelcome to the assistant bot!\n" \
                "(enter 'help' for list of commands)\n"
            case 'placeholder':
                return "Enter a command: "
            case 'bye':
                return "Good bye!\n"
            case 'hello':
                return "How can I help you?\n"
            case 'invalid command':
                return "Invalid command.\n"
            case 'phone not in contacts':
                return "Invalid Name.\nThis contact " \
                    "doesn't exist."
            case 'contact exists':
                return "Invalid Name.\nThis contact " \
                    "already exists."
            case 'no name for search':
                return "Invalid data.\nYou must " \
                    "give me Name."
            case 'invalid phone':
                return "Invalid Phone-number.\nMust " \
                    "be 10 numbers."
            case 'invalid args':
                return "Invalid data.\nYou must " \
                    "give me Name and Phone-number."
            case 'help':
                return "'add [name] [phone]'\tto add new contact " \
                "(phone must be 10 digits).\n" \
                "'all'\t\t\tto review all contacts.\n" \
                "'change [name] [phone]'\tto change contact's phone number.\n" \
                "'del [name]'\t\tto delete contact from list.\n" \
                "'phone [name]'\t\tto review contact's phone number.\n" \
                "'close' or 'exit'\tto exit assistant.\n"
