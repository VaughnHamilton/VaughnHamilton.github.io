
def check_pwd(pword):
    password = str(pword)
    if len(password) < 8 or len(password) > 20:
        return False
    if not any(part.isdigit() for part in password):
        return False
    
        
    return True