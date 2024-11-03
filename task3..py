import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    try:
        # Ask the user for the password length
        length = int(input("Enter the desired length of the password: "))
        
        # Check if the length is valid
        if length < 1:
            print("Password length should be at least 1 character.")
        else:
            # Generate the password
            password = generate_password(length)
            print("Generated Password:", password)
    
    except ValueError:
        print("Please enter a valid number for the password length.")

# Run the main function
if __name__ == "__main__":
    main()