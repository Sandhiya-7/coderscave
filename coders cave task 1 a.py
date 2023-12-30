import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")

    # Get user input
    length = int(input("Enter the desired password length: "))

    # Generate and display the password
    password = generate_password(length)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
