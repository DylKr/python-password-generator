import string
import random

def get_strength():
    """Prompt the user for a password strength, strong or weak"""
    while True:
        try:
            strength = input("Do you want a strong or a weak password? (strong/weak) ")
            if strength not in ("strong", "weak"):
                raise ValueError("Invalid strength")
            return strength
        except ValueError:     
            print("Invalid Strength")

def get_size():
    """Prompt user for a password size."""
    while True:
        try:
            size = int(input("What is the desired password size? "))
            if size <= 0:
                print("Please provide an integer type")
                continue
            return size
        except ValueError:
            print("Please provide an integer type")

def main():
    """Create random password base on user input and print"""
    service = input("What is the password for? ")
    strength = get_strength()
    size = get_size()

    if strength == 'strong':
        characters = string.ascii_letters
    elif strength == 'weak':
        characters = string.digits

    password = service + ''.join(random.choice(characters) for _ in range(size))

    print(f"Your password is: {password}")

if __name__ == "__main__": 
    main()