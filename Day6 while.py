# Write a python program to reverse a number using a while loop.

def reverse_number(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit

        number = number // 10
    return reversed_number

number = 12345
reversed_number = reverse_number(number)
print("Reversed Number:", reversed_number)



# Write a python program to check whether a number is palindrome or not?

number = int(input("Enter a number: "))

number_str = str(number)

reversed_str = number_str[::-1]

if number_str == reversed_str:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")



# Write a python program finding the factorial of a given number using a while loop

number = int(input("Enter a number: "))

factorial = 1

current = number
while current > 0:
    factorial *= current
    current -= 1

print(f"The factorial of {number} is {factorial}.")



# Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.

total_sum = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total_sum += number

print(f"The sum of all numbers is {total_sum}.")