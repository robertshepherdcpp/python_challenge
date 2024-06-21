# Create a tuple with the names of four different animals and print the tuple.
tup1 = ("Cat", "Dog", "Cow", "Sheep")
print(tup1)

# Create a tuple with the names of five cities.
# Print the first and last city in the tuple.
tup2 = ("London", "Madrid", "Berlin", "Paris", "Oslo")
print(tup2[0] + " " + tup2[len(tup2) - 1])

# Create a tuple with five different numbers.
# Attempt to change the second number (this should result in an error).
# Concatenate the tuple with another tuple containing one number and print the new tuple.
tup3 = (10, 11, 14, 18, 20)
# tup3[1] = 5  results in error
print(tup3 + (21,))

# Create a tuple with the first six positive integers.
# Print a slice of the tuple from index 2 to 4.
# Check if the number 4 is in the tuple and print the result.
# Iterate over the tuple and print each number.
tup4 = (5, 6, 7, 8, 9, 11)
print(tup4[2: 4])
if 4 in tup4:
    print(tup4)
for i in tup4:
    print(i)