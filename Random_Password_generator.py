import random
import string
import os

settings = {
    "lower": True,
    "upper": True,
    "symbol": True,
    "number": True,
    "space": False,
    "length": 8
}

PASSWORD_MAX_LENGTH = 30
PASSWORD_MIN_LENGTH = 4


def get_yes_or_no_for_settings(option, default):
    """
    returns True or False for settings.
    without "length" option.
    """
    while True:
        user_input = input(
            f"Include {option} ? (Defult is: {default}) (y: yes , n: no, enter: defult ): ")

        if user_input in ["y", "n"]:
            return user_input == "y"
        elif user_input == "":
            return default
        print("not valid pls try again!!!")


def get_password_length(option, default, pw_min_length=PASSWORD_MIN_LENGTH, pw_max_length=PASSWORD_MAX_LENGTH):
    """
    returns the length of password.
    """
    while True:
        user_input = input(
            f"Enter Password length between {pw_min_length} and {pw_max_length} . Default is: {default} (enter:default): ")

        if user_input == "":
            return default
        if user_input.isdigit():
            user_password_length = int(user_input)
            if pw_min_length <= user_password_length <= pw_max_length:
                return user_password_length
            print("Invlaid input!")
            print(
                f"Password length should be between {pw_min_length} and {pw_max_length}.")
        else:
            print("Invalid input!!!")
            print("you should enter a number.")

        print("pls try again.")


def get_settings_from_user(settings):
    """
    returns user manuall settings.
    """

    for option, default in settings.items():
        if option != "length":
            user_choice = get_yes_or_no_for_settings(option, default)
            settings[option] = user_choice
        else:
            user_password_length = get_password_length(option, default)
            settings[option] = user_password_length


def genarate_random_char(choices):
    choice = random.choice(choices)
    if choice == "upper":
        return random.choice(list(string.ascii_uppercase))
    if choice == "lower":
        return random.choice(list(string.ascii_lowercase))
    if choice == "symbol":
        return random.choice(list(string.punctuation))
    if choice == "number":
        return random.choice(list(string.digits))
    if choice == "space":
        return random.choice(list(string.whitespace))


def clear_all():
    os.system('cls')


def password_generator(settings):
    clear_all()

    get_settings_from_user(settings)
    password_length = settings["length"]

    choices = list(filter(lambda x: settings[x], [
                   'upper', 'lower', 'symbol', 'number', 'space']))

    final_password = ""
    for i in range(password_length):
        final_password += genarate_random_char(choices)

    clear_all()
    return final_password


def run():
    while True:
        print(f"Generated Password: {password_generator(settings)}")
        want_another_password = input(
            "do you want another password? (y:yes, n:no): ")

        if want_another_password == "n":
            break


run()
