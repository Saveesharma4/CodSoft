import random
import string

# Function to generate a random password
def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_lowercase
    elif complexity == "medium":
        characters = string.ascii_letters  # Lowercase and uppercase letters
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation  # Letters, digits, and special characters
    else:
        print("Invalid complexity level")
        return None

    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Main program
def main():
    # User inputs
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the desired complexity (low/medium/high): ").lower()

    # Generate password
    password = generate_password(length, complexity)

    if password:
        print("Generated Password: ", password)

if __name__ == "__main__":
    main()
