#Q1)Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

def div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = "Error: Division by zero is not allowed."
    return result

num1 = 20       # Example call to the function
num2 = 2
print(f"The division of {num1} by {num2} is: {div(num1, num2)}")    # Display the division result

print("-------*---------*--------*---------*-------*---------*--------*---------*---------")


#Q2)Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .
def square(x):
    return x * x

num = 10    # Example call to the function
print(f"The square of {num} is: {square(num)}")       # Display the square of the number

print("-------*---------*--------*---------*-------*---------*--------*---------*---------")


#Q3)Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random
numbers = [random.randint(1, 100) for _ in range(5)]    # Generate 5 random numbers

max_num = max(numbers)   # Find the maximum number
min_num = min(numbers)   # and minimum number

print(f"Random numbers: {numbers}")    # Displaying the results
print(f"Maximum number: {max_num}")
print(f"Minimum number: {min_num}")


print("-------*---------*--------*---------*-------*---------*--------*---------*---------")


#Q4)Accept a name from the user and display that in lower case using lower() function
name = input("Please enter your name and we will convert it into lowercase: ")

lowercase_name = name.lower()   # Converting the name to lowercase
print(f"Your name in lowercase is: {lowercase_name}")    # Display the name in lowercase
