while True:
    pass_length = input("Enter length of password: ")

    if pass_length.isdigit():  # check if input is all digits
        pass_int = int(pass_length)
        print("valid input")
        break
    else:
        print("Please give a valid number, not a letter or symbol")

print(f"Password must be {pass_int} characters long")

# Ask for password and validate
while True:
    password = input("Enter password: ")
    pass_len = len(password)

    if pass_len < pass_int:
        print("Password not long enough")
        continue
    elif pass_len > pass_int:
        print("Password too long")
        continue

    # Only check requirements if length is correct
    alpha = any(i.isalpha() for i in password)
    number = any(i.isdigit() for i in password)
    special = any(not i.isalnum() for i in password)  # special chars
    uppercase = any(i.isupper() for i in password)
    lowercase = any(i.islower() for i in password)

    if alpha and number and special and uppercase and lowercase:
        # Ask user to confirm password
        confirm = input("Re-enter password to confirm: ")
        if confirm == password:
            print(f"Password '{password}' accepted!")
            break
        else:
            print("Passwords do not match. Please choose a new one.")
            continue
    else:
        print("Password must include letters (at least one upper/lower case), numbers, and special characters")