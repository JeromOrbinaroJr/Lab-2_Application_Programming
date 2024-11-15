import re

email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    try:
        if not isinstance(email, str):
            raise TypeError("The provided email must be a string.")
        return re.match(email_regex, email) is not None
    except TypeError as e:
        print(f"Error: {e}")
        return False

def find_emails_in_text(text):
    try:
        if not isinstance(text, str):
            raise TypeError("The provided text must be a string.")
        return re.findall(email_regex, text)
    except TypeError as e:
        print(f"Error: {e}")
        return []
