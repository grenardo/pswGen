import random
import string

def gen_psw(length: int):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def gen_psw_editable(length: int, has_digits: bool, has_punctation: bool, has_capitalization: bool):
    if has_digits == False and has_punctation == False and has_capitalization == False:
        characters = string.ascii_lowercase

    if has_digits == True and has_punctation == False and has_capitalization == False:
        characters = string.ascii_lowercase + string.digits

    if has_digits == False and has_punctation == True and has_capitalization == False:
        characters = string.ascii_lowercase + string.punctuation

    if has_digits == True and has_punctation == True and has_capitalization == False:
        characters = string.ascii_lowercase + string.digits + string.punctuation

    if has_digits == False and has_punctation == False and has_capitalization == True:
        characters = string.ascii_letters

    if has_digits == True and has_punctation == False and has_capitalization == True:
        characters = string.ascii_letters + string.digits

    if has_digits == False and has_punctation == True and has_capitalization == True:
        characters = string.ascii_letters + string.punctuation

    if has_digits == True and has_punctation == True and has_capitalization == True:
        characters = string.ascii_letters + string.digits + string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

