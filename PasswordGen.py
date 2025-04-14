import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive number.")
            return
        
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the password generator
password_generator()