"""imports"""
# from collections import UserDict
# from datetime import datetime
# from app.book import AddressBook, Record

class Decorators:
    """Collection of decorators for AddressBook
    """
    @staticmethod
    def validate_two_args(func):
        """Decorator to validate functions with 2 arguments."""
        def inner(contacts, args):
            if len(args) != 2:
                return 'invalid args'
            phone = args[1]
            if len(phone) != 10:
                return f'invalid phone {phone}'
            return func(contacts, args)

        return inner

    @staticmethod
    def validate_one_arg(func):
        """Decorator to validate functions with 1 argument."""
        def inner(contacts, args):
            if len(args) != 1:
                return 'no name for search'
            contact_name = args[0]
            if contact_name not in contacts:
                return 'phone not in contacts'
            return func(contacts, contact_name)

        return inner
