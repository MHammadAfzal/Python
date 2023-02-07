print("Hello World")
# ! FILE I/O IN PYTHON

# * Let's just write a simple program for user input
# name = input("What's your name? ")
# print(f"Hello, {name}")
# TODO You should make a list of names to store student's name
# * Now add the input given by user to names

# names = []  # * list of names
# for _ in range(3):
#     name = input("What's your name? ")
#     names.append(name)
# * Making for loop better
# for _ in range(3):
#     names.append(input("What's your name? "))
# print(f"Hello, {names}")
# TODO Sort the list and then print it
# for i in sorted(names):
# print(i)
# * There is a issue in the program. The stored names are vanished after the program ends. So to store something, we use file I/O system
# TODO Let's learn about file I/O
# name = input("What's your name? ")
#  ---------------------------------------------------------------
# # * open keyword used in PYTHON for file open
# # file = open("names.txt","w") # * it will recreate new file always
# # * Open the file and allow to append
# file = open("names.txt", "a")
# # * Write what you want in the file
# # file.write(name)  # * It will not create a new line in file
# file.write(f"{name}\n")   # * # * It will create a new line in file
# # * After writing what you want, close the file
# file.close()
# * WELL DONE
#  ---------------------------------------------------------------
# name = input("What's your name? ")
# # * with keyword in PYTHON --> automatically opens and closes file
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")
#  ---------------------------------------------------------------
# TODO Reading file in PYTHON
# with open("names.txt","r") as file:
#     lines = file.readlines()
# # print(lines)
# for line in lines:
#     print("Hello,", line.rstrip())
# * Concise code of above program
# with open("names.txt","r") as file:
#     for line in file:
#         print("Hello,",line.rstrip())
#  ---------------------------------------------------------------
# TODO Sorting the list in PYTHON
# names = []
# * You can read file without giving the argument of 'r'
# with open("names.txt") as file:
#     lines = file.readlines()
#     for line in lines:
#         names.append(line.rstrip())
# # print(sorted(names))
# print(sorted(names,reverse=True))
# for name in sorted(names):
#     print("Hello",name)
#  ---------------------------------------------------------------
# ! '.txt' file for lists and '.csv' for dict/objects/key-value-pairs
# ! 'csv' stands for comma separated value
#  ---------------------------------------------------------------
# TODO creating file of key-value pairs and reading that file

# --------------------------------------------------
# ! CSV - Comma Separated Values

# with open("students.csv") as file:
#     lines = file.readlines()
#     for line in lines:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")
# * Better way to write above program
# with open("students.csv") as file:
#     lines = file.readlines()
#     for line in lines:
#         name,city = line.rstrip().split(",")
#         print(f"{name} is in {city}")
# * Much Better way to write above program
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, city = line.rstrip().split(",")
#         students.append(f"{name} is in {city}")
# for student in sorted(students):
#     print(student)
# * Experimenting the program
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, city = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["city"] = city
#         students.append(student)
# for student in students:
#     print(f"{student['name']} is in {student['city']}")
# * A bit complicated. Let's make it simpler
# def get_name(student):
#     return student["name"]


# def get_city(student):
#     return student["city"]


# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, city = line.rstrip().split(",")
#         student = {"name": name, "city": city}
#         students.append(student)
# for student in sorted(students, key=get_city, reverse=False):
#     print(f"{student['name']} is in{student['city']}")

# ? Anonymous functions in PYTHON - If we do not want to use function then what?

# * lambda keyword in PYTHOD is used to define anonymous function like:
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in{student['city']}")
# * for lambda parameters-put commas to give parameters:
# lambda a,x y:
# * We also covered sorting here somewhat

# --------------------------------------------------

# TODO Go to students.py for further details about csv - comma separated values

# --------------------------------------------------

# TODO Images in FILE in PYTHON - PIL --> pillow library

# * To study this, go to img folder and read the program logic in costumes.py python file
