print("Hello World!")

# ! LOOPS IN PYTHON

# print("meow")
# print("meow")
# print("meow")
# * Better way to write above code
# TODO While Loop
# i = 5
# while i != 0:
#     print("meow")
#     i -= 1
# * Same output for different logic...
# i = 0
# while i < 5:
#     print(f"{i+1}: meow")
#     i += 1
# * Python does not include i++ or i-- (increment and decrement) operators
# TODO For Loop
# * First method
# for i in [0,1,2]:
#     print(f"{i+1}: meow")
# * Second method
# for i in range(5):
#     print(f"{i+1}: meow")
# * some improvements if i is not required
# for _ in range(5):
#     print(f"{_+1}: meow")
# * Interesting thing
# print("meow\n" * 5,end="")
#  * Input Validation by loops
# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break
# * making it simple
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break
# * By for loop
# for _ in range(n):
#     print("meow")
# * Some more logical thinking
# def main():
#     number = getNumber()
#     meow(number)
# def getNumber():
#     while True:
#         n = int(input("What's n? "))
#         if n > 0:
#             return n
# def meow(n):
#     for _ in range(n):
#         print("meow")
# main()

# TODO LISTS IN PYTHON
# students = ["Hammad","Hassan","Haroon"]
# print(students)
# print(students[0])
# print(students[1])
# print(students[2])
# * Using loops for better functionality
# for student in students:
#     print(f"{students}: {student}")
# * Another method
# for i in range(len(students)):
#     print(i+1, students[i])

# TODO DICTIONARIES IN PYTHON
# students = ["Hammad","Hassan","Haroon"]
# place = ["Pasrur","Qassoor","Nowshehra"]
# students = {
#     "Hammad": "Pasrur",
#     "Hassan": "Qasoor",
#     "Haroon": "Nowshehra"
# }
# print(students)
# print(students["Hammad"])
# print(students["Hassan"])
# print(students["Haroon"])

# for student in students:
#     print(student,students[student], sep=": ")
# * List of dictionaries 
# students = [
#     {"Name": "Hammad", "City" : "Pasrur", "Department": "Softee"},
#     {"Name": "Hassan", "City" : "Qasoor", "Department": "EE"},
#     {"Name": "Haroon", "City" : "Nowshehra", "Department": None}
# ]
# print(stu0dents)

# for student in students:
#     print(student["Name"], student["City"],student["Department"],sep=": ")

# TODO Nested Loops
# print("#")
# print("#")
# print("#")
# * Better way to do it
# for _ in range(3):
#     print("#")
# * Some logical thinking
def main():
    print_Col(5)
    print_Row(5)
    print_Square(5)
def print_Col(height = 0):
    # print("#\n" * height, end ="")
    # * Does same thing as above print
    for _ in range(height):
        print("#")
def print_Row(width):
    print("?" * width)
def print_Square(size):
    # * For each row in square
    for i in range(size):
        # * For each column (hash) in row
        for j in range(size):
            # * print hash
            print("#", end="")
        # * Go to next line after first row
        print()
main() 