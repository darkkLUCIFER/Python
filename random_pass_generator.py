import string
import random


def get_settings(pass_len=8, chk_upper_case=True, chk_lower_case=True, chk_symbol=True, chk_number=True, chk_space=False):

    alphabet_upper_list = list(string.ascii_uppercase)
    alphabet_lower_list = list(string.ascii_lowercase)
    symbol_list = list(string.punctuation)
    number_list = list(string.digits)
    space_list = list(string.whitespace)

    random_list = []
    if chk_upper_case:
        random_list.append("chk_upper_case")
    if chk_lower_case:
        random_list.append("chk_lower_case")
    if chk_symbol:
        random_list.append("chk_symbol")
    if chk_number:
        random_list.append("chk_number")
    if chk_space:
        random_list.append("chk_space")

    random_pass_list = []
    for i in range(pass_len):
        random_choose = random.choice(random_list)
        if random_choose == "chk_upper_case":
            random_pass_list.append(random.choice(alphabet_upper_list))
        elif random_choose == "chk_lower_case":
            random_pass_list.append(random.choice(alphabet_lower_list))
        elif random_choose == "chk_symbol":
            random_pass_list.append(random.choice(symbol_list))
        elif random_choose == "chk_number":
            random_pass_list.append(random.choice(number_list))
        elif random_choose == "chk_space":
            random_pass_list.append(random.choice(space_list))

    return "".join(random_pass_list)


print(get_settings(6, True, True, True, True, False))
