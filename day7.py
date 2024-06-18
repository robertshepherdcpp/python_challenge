# Write a program that prints each character of a string on a new line.
str = "Hello"
for i in str:
    print(i)

# Write a program that uses a while loop to print the numbers from 10 to 1.
starter = 10
while starter > 0:
    print(starter)
    starter -= 1

# Write a program that iterates over a list of numbers and prints each number. If it encounters the number 5, the program should terminate.
arr = []
for i in range(10):
    arr.append(i)
for i in arr:
    if i == 5:
        break
    else:
        print(i)

# Write a program that iterates over a list of numbers and prints only the even numbers.
arr2 = []
for i in range(10):
    arr2.append(i)
for i in arr2:
    if i % 2 == 1:
        continue
    else:
        print(i)

# Write a program that iterates over the numbers from 0 to 9 and uses the pass statement for the number 5, but prints all other numbers.
arr3 = []
for i in range(10):
    arr3.append(i)
for i in arr3:
    if i == 5:
        pass
    else:
        print(i)
