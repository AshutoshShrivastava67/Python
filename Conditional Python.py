# Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
# Ask the user to input a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


#Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
# Ask the user to input their age
age = int(input("Enter your age: "))

# Check if the person is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Write a Python program that determines if a given year is a leap year or not.
# Ask the user to input a year
year = int(input("Enter a year: "))

# Determine if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#Create a Python program that checks if a user-given number is positive, negative, or zero.
# Ask the user to input a number
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")


#Write a Python program that determines the largest of three numbers entered by the user.
# Ask the user to input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest of the three numbers
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the largest number
print(f"The largest number is {largest}.")
