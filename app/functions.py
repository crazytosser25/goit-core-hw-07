"""imports"""
# import re
from datetime import timedelta
# from app.book import AddressBook, Record

class Decorators:
    """Collection of decorators for AddressBook
    """
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
    def validate_birthday(func):
        """Decorator to validate functions with 2 arguments."""
        def inner(contacts, args):
            if len(args) != 2:
                return 'invalid args'
            name = args[0]
            date = args[1]
            # pattern = r"\d{2}.\d{2}.\d{4}"
            # if re.search(date, pattern):
            return func(contacts, name, date)
            # return f'invalid date {date}'

        return inner

    @staticmethod
    def validate_three_args(func):
        """Decorator to validate functions with 3 arguments."""
        def inner(contacts, *args):
            if len(args) != 3:
                return 'invalid args'
            phone1, phone2 = args[1], args[2]
            if len(phone1) != 10 and len(phone2) != 10:
                return 'invalid phones.'
            return func(contacts, *args)

        return inner


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday

def date_to_string(date):
    # return type(date)
    return date.strftime("%d.%m.%Y")

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%d.%m.%Y").date()
