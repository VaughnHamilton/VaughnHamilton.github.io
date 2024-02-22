
def check_pwd(pword):
    password = str(pword)
    if not any(part.isdigit() for part in password):
        return False
    elif not any(part.islower() for part in password):
        return False
    elif not any(part.isupper() for part in password):
        return False
        
    return True