#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero. 
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return f"The result is {result}"

# Example usage
numerator = 10
denominator = 0

print(divide_numbers(numerator, denominator))

#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer. 
def get_integer():
    user_input = input("Please enter an integer: ")
    if not user_input.isdigit():
        raise ValueError("Error: The input is not a valid integer.")
    return int(user_input)

try:
    number = get_integer()
    print(f"You entered the integer: {number}")
except ValueError as e:
    print(e)


#Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist. 
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage
filename = "example.txt"

open_file(filename)


#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
def get_numbers():
    try:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
        return num1, num2
    except ValueError:
        raise TypeError("Error: Both inputs must be numerical.")

try:
    number1, number2 = get_numbers()
    print(f"You entered: {number1} and {number2}")
except TypeError as e:
    print(e)
