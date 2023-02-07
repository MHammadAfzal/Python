# ! CSV Library

# * Importing csv module...
# import csv

# students = []

# with open("people.csv") as file:
#     reader = csv.reader(file)
#     # for row in reader:
#     #     students.append({"name": row[0], "city": row[1]})
#     for name, city in reader:
#         students.append({"name": name, "city": city})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from{student['city']}")
# * DictReader in CSV - reading from a file as a dictionary/object
# students = []

# with open("people.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "city": row["city"]})
    

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from{student['city']}")

# TODO writing CSV files

import csv

#  * Writing a file
# name = input("What's your name? ")
# city = input("Where do you live? ")

# with open("exp.csv","a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, city])
#  * Writing a dict file
name = input("What's your name? ")
city = input("Where do you live? ")

with open("expt.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","city"])
    writer.writerow({"name": name, "city": city})
