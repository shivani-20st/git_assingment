# sample.py

def is_even(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

# Updated: Get user input
try:
    number = int(input("Enter a number: "))
    print(is_even(number))
except ValueError:
    print("Please enter a valid integer.")
