# Q1  Write a Python program that determines if a given year is a leap year or not.

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Q2 Python Program to Find the Largest Among Three Numbers
def find_largest(a, b, c):
    # Compare the three numbers and return the largest
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = find_largest(num1, num2, num3)
print(f"The largest number is: {largest}")

#Q3 Create a Python program that checks if a user-given number is positive, negative, or zero.

a = int(input("Enter a number: "))

if a>0 :
    print("Positive number")
elif a==0 :
    print("Zero")
else:
    print ("Negative number")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Q4 A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs.1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively
#  Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

def calculate_discount(product_code, order_amount):
    # Initialize the discount percentage
    discount = 0
    
    # Check for the type of toy and apply discount accordingly
    if product_code == 1:  # Battery Based Toys
        if order_amount > 1000:
            discount = 0.10
    elif product_code == 2:  # Key-based Toys
        if order_amount > 100:
            discount = 0.05
    elif product_code == 3:  # Electrical Charging Based Toys
        if order_amount > 500:
            discount = 0.10
    else:
        return "Invalid product code"

    # Calculate the discount amount and net amount
    discount_amount = order_amount * discount
    net_amount = order_amount - discount_amount
    
    return net_amount

# Example usage
try:
    product_code = int(input("Enter the product code (1 for Battery Based, 2 for Key-based, 3 for Electrical Charging): "))
    order_amount = float(input("Enter the order amount: "))

    net_amount = calculate_discount(product_code, order_amount)
    if isinstance(net_amount, str):
        print(net_amount)
    else:
        print(f"The net amount to be paid after discount is: Rs.{net_amount:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for product code and order amount.")

#Q5 A transport company charges the fare according to following table:
""" Distance - 8 Rs/Km - 10 Rs/Km - 12 Rs/Km
Charges - 1-50 - 51-100 - 100 """

def calculate_fare(distance):
    # Determine the fare rate based on the distance
    if 1 <= distance <= 50:
        fare_per_km = 8
    elif 51 <= distance <= 100:
        fare_per_km = 10
    elif distance > 100:
        fare_per_km = 12
    else:
        return "Invalid distance. Distance must be greater than 0."

    # Calculate the total fare
    total_fare = distance * fare_per_km
    return total_fare

# Example usage
try:
    distance = float(input("Enter the distance traveled (in kilometers): "))
    
    if distance <= 0:
        print("Distance must be greater than 0.")
    else:
        fare = calculate_fare(distance)
        if isinstance(fare, str):
            print(fare)
        else:
            print(f"The total fare for {distance} km is: Rs.{fare:.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric value for the distance.")
