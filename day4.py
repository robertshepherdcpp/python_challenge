# Write a program that takes two numbers as input and prints their sum, difference, product, quotient, and remainder.

input1 = 5
input2 = 3

print("Sum:", input1 + input2)

if input1 > input2:
    print("Difference:", input1-input2)
elif input2 > input1:
    print("Difference:", input2-input1)
else:
    print("Difference:", 0)

print("Product:", input1 * input2)

print("Quotient:", input1 // input2)

print("Remainder:", input1 % input2)

# Write a program that takes two numbers as input and compares them using all comparison operators, then prints the results.

print("num1 <= num2:", input1 <= input2)
print("num1 < num2:", input1 < input2)
print("num1 == num2:", input1 == input2)

# Write a program that demonstrates the use of logical operators with boolean variables.

print(True and False) # false
print(True and False or True) # true
print(not False) # true

