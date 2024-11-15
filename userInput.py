from reExpression import is_valid_email

def check_user_input():
    try:
        email = input("Enter your e-mail for verification: ")

        if not isinstance(email, str):
            raise TypeError("The entered value must be a string.")

        if is_valid_email(email):
            print("The e-mail is correct!")
        else:
            print("Incorrect e-mail.")

    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")

if __name__ == "__main__":
    check_user_input()
