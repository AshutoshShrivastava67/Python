# Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(num1, num2):
    try:
        # Perform the division and return the result
        result = num1 / num2
        return result
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Division by zero is not allowed."

# Example usage
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    result = div(number1, number2)
    if isinstance(result, str):
        print(result)
    else:
        print(f"The result of dividing {number1} by {number2} is: {result:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")


# Declare a square() function with one parameter. Then call the function and pass one
# number and display the square of that number.

def square(number):
    # Calculate the square of the number
    return number * number

# Example usage
try:
    # Get user input
    num = float(input("Enter a number: "))
    
    # Call the square function
    result = square(num)
    
    # Display the result
    print(f"The square of {num} is: {result:.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")

#Using max() and min() functions display the maximum and minimum of 5 random numbers.
import random

# Generate 5 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Display the generated random numbers
print("Random numbers:", random_numbers)

# Find and display the maximum and minimum numbers
maximum_number = max(random_numbers)
minimum_number = min(random_numbers)

print(f"The maximum number is: {maximum_number}")
print(f"The minimum number is: {minimum_number}")

#Accept a name from the user and display that in lower case using lower() function
# Get the name input from the user
name = input("Enter a name: ")

# Convert the name to lowercase using the lower() function
lowercase_name = name.lower()

# Display the name in lowercase
print(f"The name in lowercase is: {lowercase_name}")
