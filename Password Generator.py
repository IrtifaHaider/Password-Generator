import re
import secrets
import string


def generate_password(length, nums, special_chars, uppercase, lowercase):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
def main():
    length = int(input("Enter the length of the password: "))
    nums = int(input("Enter the number of numbers you want in the password: "))
    special_chars = int(input("Enter the number of special characters you want in the password: "))
    uppercase = int(input("Enter the number of uppercase letters you want in the password: "))
    lowercase = int(input("Enter the number of lowercase letters you want in the password: "))
    new_password = generate_password(length, nums, special_chars, uppercase, lowercase)
    print('Generated password:', new_password)

main()