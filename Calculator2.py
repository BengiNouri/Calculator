#The Calculator2.py script is a more robust version of the Calculator.py script. It has added a power operation and a get_number function to validate the input. 
# It also has a main function  calculator  to handle the operations. 
# The calculator function will keep running until the user selects the exit option. 
# The Calculator2.py script is more modular and easier to maintain. 
# Let's run the Calculator2.py script. 
# python Calculator2.py
 
# The output will be: 
# Select an operation to perform:

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

# Extend with more operations as needed
def power(x, y):
    return x ** y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculator():
    while True:
        print("\nSelect an operation to perform: ")
        print("1. ADD")
        print("2. SUBTRACT")
        print("3. MULTIPLY")
        print("4. DIVIDE")
        print("5. POWER")
        print("6. EXIT")
        
        operation = input("Enter choice (1/2/3/4/5/6): ")

        if operation == "6":
            print("Exiting calculator.")
            break

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if operation == "1":
            print("The sum is: ", add(num1, num2))
        elif operation == "2":
            print("The difference is: ", subtract(num1, num2))
        elif operation == "3":
            print("The product is: ", multiply(num1, num2))
        elif operation == "4":
            print("The quotient is: ", divide(num1, num2))
        elif operation == "5":
            print("The result is: ", power(num1, num2))
        else:
            print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    calculator()
 
 