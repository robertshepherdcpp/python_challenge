# Define a class called Rectangle with attributes width and height.
# Implement the __str__ and __repr__ methods to provide string representations of the rectangle.
class Rectangle:
    width = 0
    height = 0

    def __init__(self, p_width, p_height):
        self.width = p_width
        self.height = p_height
    def __str__(self):
        return f"({self.width}, {self.height})"
    def __repr__(self):
        return f"(width={self.width}, height={self.height})"
    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)
    def __mul__(self, other):
        return Rectangle(self.width * other.width, self.height * other.height)
    def __eq__(self, other):
        return (self.width * self.height) == (other.width * other.height)
    def __lt__(self, other):
        return (self.width * self.height) <= (other.width * other.height)

# Add methods to overload the + operator to add the areas of two rectangles.
# Add methods to overload the * operator to multiply the areas of two rectangles.

# Implement the __eq__ method to check if two rectangles have the same area.
# Implement the __lt__ method to check if one rectangle's area is less than another's.

# Notes:
#   __str__ - basically for a breif summary of the class, implicit converion
#   __repr__ - a more detailed summary, requires the repr() function to be called on it.

# test cases, made by chatgpt

rect1 = Rectangle(10, 15)
rect2 = Rectangle(30, 5)

print(rect1)
print(repr(rect1))
print(rect1)
print(rect2)
print(rect1 == rect2)
print(rect1 < rect2)
