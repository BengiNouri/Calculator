
# To modify the calculator application to allow for a dynamic number of inputs for all operations, including division and power 
#(where applicable), you can adjust the approach. For division and power, though typically involving two numbers, 
# you might still ask the user for the number of inputs and then explain how those inputs will be used. For example, in division, 
# you could divide the first number by all subsequent numbers sequentially, and for power, you could raise the first number to the power of the second, 
# then that result to the power of the third, and so on.

# Here's how you can implement these adjustments:

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /= num
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def power(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result **= num
    return result

def get_numbers(input_message):
    num_inputs = int(input(input_message))
    return [float(input(f"Enter number {i+1}: ")) for i in range(num_inputs)]

def calculator():
    while True:
        print("\nSelect an operation to perform:")
        print("1. ADD")
        print("2. SUBTRACT")
        print("3. MULTIPLY")
        print("4. DIVIDE")
        print("5. POWER")
        print("6. EXIT")
        
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '6':
            print("Exiting the calculator...")
            break

        numbers = []
        if choice in ('1', '2', '3', '4', '5'):
            if choice == '4' or choice == '5':
                message = "How many numbers do you wish to calculate (for DIVIDE, first number will be divided by all subsequent ones; for POWER, calculated as first number to the power of the second, and so on): "
            else:
                message = "How many numbers do you wish to calculate? "
            numbers = get_numbers(message)

        if choice == '1':
            print("The sum is: ", add(numbers))
        elif choice == '2':
            print("The difference is: ", subtract(numbers))
        elif choice == '3':
            print("The product is: ", multiply(numbers))
        elif choice == '4':
            print("The quotient is: ", divide(numbers))
        elif choice == '5':
            print("The result is: ", power(numbers))
        else:
            print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    calculator()
