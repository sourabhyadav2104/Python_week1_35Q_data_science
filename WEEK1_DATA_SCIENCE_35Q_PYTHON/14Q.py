## A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

import re

def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

passwords = input("Enter passwords separated by commas: ")
valid_passwords = []

for password in passwords.split(","):
    if check_password(password):
        valid_passwords.append(password)

print(",".join(valid_passwords))
