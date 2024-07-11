import secrets
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    password = secrets.choice(letters)
    password += secrets.choice(digits)
    password += secrets.choice(special_chars)

    remaining_length = length - 3  
    for _ in range(remaining_length):
        all_chars = letters + digits + special_chars
        password += secrets.choice(all_chars)

    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    return "".join(password_list)

user_length = int(input("Enter desired password length: "))
generated_password = generate_password(user_length)
print(f"Generated password: {generated_password}")
