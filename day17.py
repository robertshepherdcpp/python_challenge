import csv

#Create a CSV file named students.csv with the following columns: Name, Age, Grade.
# Write a Python script to read the file and print each student's information.

with open('students.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(', '.join(row))

# Write a Python script that takes user input for Name, Age, and Grade, and appends this information to students.csv.
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles'],
    ['Charlie', '35', 'Chicago']
]

with open('students.csv', 'w', newline='') as csvfile_two:
    csvwrite = csv.writer(csvfile_two, delimiter=',')
    csvwrite.writerows(data)

# Modify the script from the first assignment to use DictReader.
# Modify the script from the second assignment to use DictWriter.
with open('students.csv', newline='') as csvfile_three:
    read_dict = csv.DictReader(csvfile_three)
    for row in read_dict:
        print(f"Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")

# fieldnames = ['Name', 'Age', 'City']
# with open('students.csv', 'w', newline='') as csvfile_four:
#     csvwriter = csv.DictWriter(csvfile_four, fieldnames=fieldnames)
#     csvwriter.writeheader()
#     csvwriter.writerows(data)

# Create a Python script that reads from students.csv and calculates the average age and grade
# of the students, then writes this information to a new CSV file named students_summary.csv.
from itertools import accumulate
with open('students.csv', newline='') as file_four:
    read_dict_two = csv.DictReader(file_four)
    ages = []
    #grades = []
    for i in read_dict_two:
        ages.append(int(row['Age']))
        #grades.append(row['Grade'])
    print("Age average: ", sum(ages) / len(ages))
    # print("Grade average: ", sum(grades) / len(grades))


