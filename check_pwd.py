
def check_pwd(password):
    if len(str(password)) < 8 or len(str(password)) > 20:
        return False
    return True