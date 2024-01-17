import string
import secrets

def generate_password(length):
    uppercase_letters =string.ascii_uppercase
    lowercase_letters=string.ascii_lowercase
    digits = string.digits
    symbols=string.punctuation
    all_characters= uppercase_letters +lowercase_letters +digits +symbols
    password=''.join(secrets.choice(all_characters) for _ in range(length))
    return password

length=int(input("Enter the length of password:"))
password= generate_password(length)
print("Generated password:",password)


