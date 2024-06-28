# Create a text file named data.txt with several lines of text.
# Write a Python script to read the file and print its contents line by line.
with open('data.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        print(i)

# Write a Python script that asks the user for input and writes the input to a file named output.txt.
# The script should continue asking for input until the user types "STOP".
input_ = ""
file_two = open("output.txt", 'w')
while input_ != "STOP":
    input_ = input("Enter text to be written to: ")
    file_two.write(input_)

# Write a Python script to read from data.txt and count the number of lines, words, and characters in the file.
with open('data.txt', 'r') as file_three:
    lines_two = file_three.readlines()
    word_count = 1
    character_count = 0
    for i in lines_two:
        for j in i:
            character_count += 1
            if j == ' ':
                word_count += 1
    print("num lines:", len(lines_two))
    print("num words:", word_count)
    print("num characters:", character_count)

# Create a Python script that reads from one file (data.txt) and writes its content to another file (copy.txt),
# but in reverse order (i.e., the last line of data.txt should be the first line of copy.txt).
file_four = open("data.txt", 'r')
file_five = open("copy.txt", 'w')
lines = file_four.readlines()
for i in range(len(lines) - 1, 0, -1):
    file_five.write(lines[i])