# Print the first 10 natural numbers using for loop.

for number in range(1, 11):
    print(number)



# Python program to check if the given string is a palindrome.

string = "madam"

cleaned_string = string.replace(" ", "").lower()

is_palindrome = True

length = len(cleaned_string)

for i in range(length // 2):
    if cleaned_string[i] != cleaned_string[length - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")



# Python program to check if a given number is an armstrong number.

num = int(input("Enter a number: "))
order = len(str(num))
sum = 0

for digit in str(num):
  sum += int(digit) ** order

if num == sum:
  print(num, "is an Armstrong number")
else:
  print(num, "is not an Armstrong number")



# Python program to get the fibonacci series between 0 to 50.

a, b = 0, 1

for _ in range(15):  
    if a > 50:
        break
    print(a)
    a, b = b, a + b



# Python program to check the validity of password input by users.

import string

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Password is valid.")
    else:
        print("Password is invalid.")
else:
    print("Password is invalid.")

  










#Print the table of 5 using for loop

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")



#Print even number series by taking input from the user

limit = int(input("Enter the limit: "))

for number in range(2, limit + 1, 2):
    print(number)



#Create a list and iterate through its items using a for loop

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)



#Calculate the sum of numbers from 1 to 10

total_sum = 0

for number in range(1, 11):
    total_sum += number

print("The sum of numbers from 1 to 10 is:", total_sum)
