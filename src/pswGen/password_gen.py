import string
import secrets

'''
Generate a password of the specified length using random letters, digits and punctation.
'''
def gen_psw(length: int):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

'''
Generate a password of the specified length using the selected parameters.
'''
def gen_psw_editable(length=12, digits=True, punctuation=True, uppercase=True):

    chars = string.ascii_lowercase
    if uppercase:
        chars += string.ascii_uppercase
    if digits:
        chars += string.digits
    if punctuation:
        chars += string.punctuation

    return ''.join(secrets.choice(chars) for _ in range(length))
