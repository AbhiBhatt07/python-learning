# import nassacery modules
import random
import string


# function of generate the password.
def password_generate(length, lower_chr, upper_chr, digits, special_chr):
    characters = ""

    if lower_chr:
        characters = characters + string.ascii_lowercase

    if upper_chr:
        characters = characters + string.ascii_uppercase

    if digits:
        characters = characters + string.digits

    if special_chr:
        characters = characters + string.punctuation

    if not characters:
        return " Please select atleast one character type."

    password = "".join(random.choice(characters) for _ in range(length))

    return password


length = int(input("Enter the length of password: "))

# ask user to which character you want to add in password.
lower_chr = input("Include lower letters? (y/n): ").lower() == "y"
upper_chr = input("Include upper letters? (y/n): ").lower() == "y"
digits = input("Include digits letters? (y/n): ").lower() == "y"
special_chr = input("Include special character? (y/n): ").lower() == "y"

password = password_generate(length, lower_chr, upper_chr, digits, special_chr)

print("Your password: ", password)