  #Print the table of 5 using for loop
  # Table of 5
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

#Print even number series by taking input from the user:
# Taking input from the user for the range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Even number series:")

# Loop to print even numbers in the specified range
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)

#Create a list and iterate through its items using a for loop:
# Creating a list
my_list = ['Data', 'Meta', 'Google', 'elderberry']

# Iterating through the list items using a for loop
for item in my_list:
    print(item)

#Calculate the sum of numbers from 1 to 10 
total_sum = 0
for i in range(1, 11):
    total_sum += i

print("The sum of numbers from 1 to 10 is:", total_sum)
