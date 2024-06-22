# Create a set with the names of four different colors and print the set.
colors = {"Red", "Green", "Blue", "Yellow"}
print(colors)

# Create a set with the names of five different animals.
# Add a new animal to the set and print the set.
# Remove an animal from the set and print the set.
animals = {"lion", "Zebra", "elephant", "rhino", "cheeta"}
animals.add("giraffe")
animals.remove("rhino")

# Create two sets: one with the numbers 1 to 5 and another with the numbers 4 to 8.
# Find and print the union of the two sets.
# Find and print the intersection of the two sets.
# Find and print the difference between the first set and the second set.
# Find and print the symmetric difference between the two sets.
one_five = {1, 2, 3, 4, 5}
four_eight = {4, 5, 6, 7, 8}
print(one_five.union(four_eight))
print(one_five.intersection(four_eight))
print(one_five.difference(four_eight))
print(one_five.symmetric_difference(four_eight))

# Create a set with the names of four different fruits.
# Check if "apple" and "mango" are in the set and print the results.
fruits = {"apple", "pear", "orange", "bannana"}
print("apple" in fruits)
print("mango" in fruits)

# Create a set with the names of three different cities.
# Use a for loop to iterate through the set and print each city.
cities = {"London", "Paris", "Madrid"}
for i in cities:
    print(city)

