import random
import string

def generate_password(length=12, include_lowercase=True, include_uppercase=True, include_numbers=True, include_special_chars=True):
    # Define character sets based on user preferences
    lowercase_chars = string.ascii_lowercase if include_lowercase else ''
    uppercase_chars = string.ascii_uppercase if include_uppercase else ''
    digit_chars = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Ensure that at least one character set is selected
    if not all_chars:
        raise ValueError("At least one character set must be selected.")

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        # Get user input for password parameters
        length = int(input("Enter the password length: "))
        include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        # Generate and print the password
        password = generate_password(length, include_lowercase, include_uppercase, include_numbers, include_special_chars)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
