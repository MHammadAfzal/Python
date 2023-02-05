print("Compare Values")

# ! CONDITIONALS IN PYTHON

# x = int(input("What's X? "))
# y = int(input("What's Y? "))

# * if x is smaller
# if  x < y:
    # print(f"{y} is greater than {x}")
# * if x is larger
# elif  x > y:
    # print(f"{x} is greater than {y}")
# * if x equals y
# else:
    # print(f"{x} is equal to {y}")
# * if x is less than y or greater than y ----> x not equals y
# TODO OR Operator
# if  x > y or x < y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")
# * same above scenario
# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")
# TODO AND Operator
# marks = int(input("Marks: "))

# * Simple way to check grades
# if marks <= 100 and marks >= 90:
#     print("Grade: A")
# elif marks < 90 and marks >= 80:
#     print("Grade: B+")
# elif marks < 80 and marks >= 70:
#     print("Grade: B")
# elif marks < 70 and marks >= 60:
#     print("Grade: C+")
# elif marks < 60 and marks >= 50:
#     print("Grade: C")
# elif marks < 50 and marks >= 35:
#     print("Grade: D")
# else:
#     print("Grade: F")
# * Better way to write above code
# if 90 <= marks <= 100:
#     print("Grade: A")
# elif 80 <= marks < 90:
#     print("Grade: B+")
# elif 70 <= marks < 80:
#     print("Grade: B")
# elif 60 <= marks < 70:
#     print("Grade: C+")
# elif 50 <= marks < 60:
#     print("Grade: C")
# elif 35 <= marks < 50:
#     print("Grade: D")
# else:
#     print("Grade: F")
# * If we know that marks are between 0 and 100
# if 0 <= marks <= 100:
#     if 90 <= marks <= 100:
#         print("Grade: A")
#     elif 80 <= marks < 90:
#         print("Grade: B+")
#     elif 70 <= marks < 80:
#         print("Grade: B")
#     elif 60 <= marks < 70:
#         print("Grade: C+")
#     elif 50 <= marks < 60:
#         print("Grade: C")
#     elif 35 <= marks < 50:
#         print("Grade: D")
#     else:
#         print("Grade: F")
# else:
#     print("Marks are out of range")
# TODO MODULO Operator
# x = int(input("Give me a number: "))
# * Define a function if the number is even or not
# TODO Boolean Values
# def isEven(n = 0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# * More better way to write above function of even
# def isEven(n):
#     return True if n % 2 == 0 else False
# * Much More better way to write above function of even
# def isEven(n):
#     return (n % 2 == 0)
# * call the function to check number is even?
# def main():
#     if isEven(x):
#         print(f"{x} is even")
#     else:
#         print(f"{x} is odd")
# main()

# TODO match keyword (switch) in PYTHON
# name = input("What's your name? ")
# def isMohal(name):
#     if name == "Hammad":
#         print(f"{name} Mohal")
#     elif name == "Afzal":
#         print(f"{name} Mohal")
#     elif name == "Hamza":
#         print(f"{name} Mohal")
#     elif name == "Atif":
#         print(f"{name} Mohal")
#     elif name == "Waqar":
#         print(f"{name} Mohal")
#     elif name == "Fahad":
#         print(f"{name} Mohal")
#     else:
#         print(f"{name} is unrecognized")
# * Better way to write above function
# def isMohal(name):
#     if name == "Hammad" or name == "Afzal" or name == "Hamza" or name == "Atif" or name == "Waqar" or name == "Fahad":
#         print(f"{name} Mohal")
#     else:
#         print(f"{name} is unrecognized")
# * More Better way to write above function
# def isMohal(n):
#     match n:
#         case "Hammad":
#             print(f"{name} Mohal")
#         case "Afzal":
#             print(f"{name} Mohal")
#         case "Hamza":
#             print(f"{name} Mohal")
#         case "Atif":
#             print(f"{name} Mohal")
#         case "Waqar":
#             print(f"{name} Mohal")
#         case "Fahad":
#             print(f"{name} Mohal")
#         case _:
#             print(f"{name} is unrecognized")
# * Much Better way to write above function
# def isMohal(n):
#     match n:
#         case "Hammad" | "Afzal" | "Hamza" | "Atif" | "Waqar" | "Fahad":
#             print(f"{n} Mohal")
#         case _:
#             print(f"{n} is unrecognized")
# isMohal(name)