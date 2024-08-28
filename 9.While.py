#Print the reverse order series  using a while loop
# Define the starting point
n = 10  # You can change this value to start from a different number

# Use a while loop to print numbers in reverse order
while n > 0:
    print(n)
    n -= 1  # Decrement the value of n by 1

#Create a code that describe the use of break statement in while loop
# Start a counter
n = 10

# Use a while loop
while n > 0:
    print(n)
    n -= 1  # Decrement the value of n by 1

    # Use a break statement to exit the loop when n reaches 5
    if n == 5:
        print("Breaking out of the loop as n reached 5.")
        break

print("Loop has ended.")

#Write a Python program using a while loop to iterate through each character of the string "Python" and print each character on a new line.
# Additionally, calculate and print the length of the string.
# Define the string
my_string = "Python"

# Initialize an index variable
index = 0

# Use a while loop to iterate through each character
while index < len(my_string):
    # Print the current character
    print(my_string[index])
    # Increment the index
    index += 1

# Calculate and print the length of the string
length_of_string = len(my_string)
print(f"Length of the string: {length_of_string}")


#  Write a Python program that takes an integer input from the user and calculates its factorial using a while loop. Display the result as the factorial of the entered number.
# Function to calculate factorial
def calculate_factorial(number):
    # Initialize the factorial result to 1
    factorial = 1
    
    # Initialize the counter
    counter = 1
    
    # Use a while loop to calculate factorial
    while counter <= number:
        factorial *= counter  # Multiply current counter to factorial
        counter += 1  # Increment the counter
    
    return factorial

# Take user input
try:
    user_input = int(input("Enter a positive integer to calculate its factorial: "))
    
    if user_input < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Calculate factorial
        result = calculate_factorial(user_input)
        # Display the result
        print(f"The factorial of {user_input} is {result}.")
except ValueError:
    print("Please enter a valid integer.")

