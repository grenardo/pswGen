import string
import secrets

def gen_psw(length: int):

    """
    Generate a password of the specified length using random letters, digits and punctation.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def gen_psw_editable(length=12, digits=True, punctuation=True, uppercase=True):

    """
    Generate a password of the specified length using the selected parameters.
    """

    chars = string.ascii_lowercase
    if uppercase:
        chars += string.ascii_uppercase
    if digits:
        chars += string.digits
    if punctuation:
        chars += string.punctuation

    return ''.join(secrets.choice(chars) for _ in range(length))


def __has_punctation(text):
    return any(char in string.punctuation for char in text)

def __has_capitalization(text):
    return any(char.isupper() for char in text)

def __has_digits(text):
    return any(char.isdigit() for char in text)

def psw_strength_check(password: str):
    
    """
    checks the strength of a passwork based on how long and how complex it is.
    """
    score = 0

    if len(password) >= 8:
        score += 1
    if __has_capitalization(password):
        score += 1
    if __has_digits(password):
        score += 1
    if __has_punctation(password):
        score += 1

    if score == 4:
        return "Password molto sicura."
    elif score == 3:
        return "Password sicura, ma può essere migliorata."
    elif score == 2:
        return "Password debole. Aggiungi maiuscole, numeri o simboli."
    else:
        return "Password molto debole. Usa almeno 8 caratteri, una maiuscola, un numero e un simbolo."
    
