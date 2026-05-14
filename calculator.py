def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def main():
    print("================================")
    print("   PYTHON COMMAND-LINE CALC")
    print("================================")

    while True:
        try:
            # Get numbers from user
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Display operation menu
            print("\nSelect Operation:")
            print(" + (Add)")
            print(" - (Subtract)")
            print(" * (Multiply)")
            print(" / (Divide)")
            
            operation = input("\nChoice (+, -, *, /): ").strip()

            # Process the math
            if operation == '+':
                print(f" >> Result: {num1} + {num2} = {add(num1, num2)}")
            elif operation == '-':
                print(f" >> Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif operation == '*':
                print(f" >> Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif operation == '/':
                result = divide(num1, num2)
                print(f" >> Result: {num1} / {num2} = {result}")
            else:
                print(" >> Invalid operation. Please use +, -, *, or /.")

        except ValueError:
            print(" >> Invalid Input! Please enter numeric values only.")

        
        next_calc = input("\nPerform another calculation? (y/n): ").lower()
        if next_calc != 'y':
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()