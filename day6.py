# Create a list of your favorite movies and print the list.
arr = ["chitty chitty bang bang", "chicken run", "dispicable me"]
for i in arr:
    print(i)

# Create a list of your top 5 favorite books.
fav_books = ["embracing modern c++ safely", "C++ templates", "C++ core guide lines", "C++", "C++ networking", "C++ concurrency"]
print("First: " + fav_books[0])
print("Last: " + fav_books[5])

# create a list of the 5 cities that you want to visit
cities = ["manchester", "london", "birmingham", "sheffield", "leeds"]
cities[2] = "cardiff"

ten_positive = []
for i in range(10):
    ten_positive.append(i)
print(ten_positive[:3])
print(ten_positive[len(ten_positive) - 3: len(ten_positive)])
print(ten_positive[3:len(ten_positive)-3])

