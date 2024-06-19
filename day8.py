# Write a function named display_message() that prints a message "I'm learning Python!" and call it.
def display_message():
    print("I'm learning python!")
display_message()

# Write a function named favorite_book(title) that accepts one parameter and prints a message like "One of my favorite books is <title>."
def favorite_book(title):
    print(f"One of my favorite books is {title}")

# Write a function named square(number) that returns the square of a number. Call the function and print the result.
def square(number):
    return number * number
square(10)

# Write a function named describe_pet(animal_type, pet_name) that accepts two parameters and prints a message like "I have a <animal_type> named <pet_name>."
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Write a function named calculate_sum(a, b) that calculates the sum of two numbers and prints the result. Demonstrate that the variables a and b are local to the function by attempting to print them outside the function (which should result in an error).
def calculate_sum(a, b):
    print(a + b)

calculate_sum(10, 5)
# print(a) results in error and demonstrates scope