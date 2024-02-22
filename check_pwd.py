
def check_pwd(pword):
    symbols = '~`!@#$%^&*()_+-='
    password = str(pword)
    if not any(part.isdigit() for part in password):
        return False
    elif not any(part.islower() for part in password):
        return False
    elif not any(part.isupper() for part in password):
        return False
    elif not any(part in symbols for part in password):
        return False
    elif len(password) < 8 or len(password) > 20:
        return False
        
    return True