# Create a dictionary with information about your favorite movie (title, director, year, genre) and print the dictionary.
fav_movie = {
    "title": "Lion the witch and the wardrobe",
    "director": "John Brown",
    "year": 1989,
    "genre": "fiction"
}
print(fav_movie)

# Create a dictionary with information about your favorite book (title, author, year, genre).
# Print the title and author of the book.
fav_book = {
    "title": "Embracing modern C++ safely",
    "author": "John Lakos",
    "year": 2021,
    "genre": "programming"
}
print("Title: " + fav_book["title"])
print("Author: " + fav_book["author"])

# Create a dictionary with information about a laptop (brand, model, price).
# Update the price of the laptop and print the updated dictionary.
laptop = {
    "brand": "dell",
    "model": "Inspiron",
    "price": 299
}
laptop["price"] = 300
print(laptop)

# Create a dictionary with information about a car (brand, model, year).
# Add the color of the car to the dictionary.
# Remove the year from the dictionary.
# Print the final dictionary.
car = {
    "brand": "Tesla",
    "model": "X",
    "year": 2019
}
car["color"] = "white"
del car["year"]
print(car)

# Create a dictionary with information about a smartphone (brand, model, price, color).
# Print all the keys in the dictionary.
# Print all the values in the dictionary.
# Print all the key-value pairs in the dictionary.
smartphone = {
    "brand": "Nokia",
    "model": "brick",
    "price": 5,
    "color": "blue"
}
print(smartphone.keys())
print(smartphone.values())
print(smartphone.values())
