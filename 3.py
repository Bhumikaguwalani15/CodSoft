import random
import string

def generate_password(length):
    # Define the character sets to use in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            # Prompt the user for the desired password length
            length = int(input("Please enter the desired length of the password: "))
            
            if length <= 0:
                print("Password length must be greater than 0. Please try again.")
                continue
            
            # Generate the password
            password = generate_password(length)
            
            # Display the generated password
            print(f"Your generated password is: {password}")
        
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        
        # Ask the user if they want to generate another password
        cont = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Thank you for using the Password Generator. Goodbye!")
            break

# Run the password generator
main()
