import re

def is_strong_password(password):
    # Password should be at least 8 characters long
    if len(password) < 8:
        return False

    # Password should contain at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Password should contain at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Password should contain at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Password should contain at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

# Sample usage
password = "SecureP@ssw0rd"
if is_strong_password(password):
    print("Password is strong.")
else:
    print("Password is weak. Please use a stronger password.")
