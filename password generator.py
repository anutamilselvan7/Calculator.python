import random
import string

def generate_password(length, use_digits, use_symbols):
    """
    Generates a random password based on user specifications.
    """
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    
    character_pool = letters
    
   
    if use_digits:
        character_pool += digits
    if use_symbols:
        character_pool += symbols

   
    password = ''.join(random.choices(character_pool, k=length))
    return password

def main():
    print("---------------------------------")
    print("   PYTHON PASSWORD GENERATOR")
    print("---------------------------------")

    while True:
        try:
            
            length = int(input("\nEnter desired password length: "))
            
            if length <= 0:
                print("!! Length must be a positive number.")
                continue

            # 2. User Input: Complexity
            include_digits = input("Include numbers? (y/n): ").lower() == 'y'
            include_symbols = input("Include special characters? (y/n): ").lower() == 'y'

            # 3. Generate and Display
            result = generate_password(length, include_digits, include_symbols)
            
            print("\n" + "=" * 40)
            print(f" GENERATED PASSWORD: {result}")
            print("=" * 40)

        except ValueError:
            print("!! Invalid input. Please enter a number for the length.")

        # Ask to generate another
        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()