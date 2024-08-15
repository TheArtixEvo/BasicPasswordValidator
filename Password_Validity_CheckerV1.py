# Password Validity Checker Program
import re

while True:
    password = input("Enter Your Password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not re.search("[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
    elif not re.search("[a-z]", password):
        print("Password must contain at least one lowercase letter.")
    elif not re.search("[0-9]", password):
        print("Password must contain at least one number.")
    else:
        print("Password is strong.")
        break  # Exit the loop if the password is valid
