print("Hello, World")

# ! More features of Python

# TODO Data type 'set' - every element is unique
# students = [
#     {"name": "Hammad", "city": "Sialkot"},
#     {"name": "Hassan", "city": "Qasoor"},
#     {"name": "Haroon", "city": "Nowshehra"},
#     {"name": "Uzairr", "city": "Qasoor"},
#     {"name": "Ayyan", "city": "Karachi"},
# ]

# city = []
# for student in students:
#     if student["city"] not in city:
#         city.append(student["city"])

# for i in sorted(city):
#     print(i)
# * We can easily do the above program using sets
# students = [
#     {"name": "Hammad", "city": "Sialkot"},
#     {"name": "Hassan", "city": "Qasoor"},
#     {"name": "Haroon", "city": "Nowshehra"},
#     {"name": "Uzairr", "city": "Qasoor"},
#     {"name": "Ayyan", "city": "Karachi"},
# ]
# city = set()

# for student in students:
#     city.add(student["city"])

# for i in sorted(city):
#     print(i)

# TODO Global Variables

# * Go to bank.py to study about global variables

# TODO Constants in PYTHON

# * Go to meows.py to study about constants

# TODO Type Hints and mypy module in PYTHON

# * -> means return None
# def meow(n : int) -> None:  # * type hint in the parameter
#     for _ in range(n):
#         print("meow")

# def meow(n : int) -> str:  # * type hint in the parameter
# return ("meow\n" * n)

# # n = input("What's n? ")
# n : int = input("What's n? ") # * type hint in input
# n : int = int(input("What's n? "))# * type hint in input
# m : str = meow(n)   # * type hint str
# # * mypy main.py will give error that function returns None
# print(m, end="")
# # meow(n)
# * Lets try "mypy" module
# * type in terminal 'mypy [source file]' - to check issues/errors

# TODO Docstrings in PYTHON - use """..."""

# def meow(n : int) -> str:
#         """
#         :Meow n times

#         :param n: number of times to meow
#         :type n: int
#         :raise TypeError: if n is not an int
#         :return: A string of n meows, one per line
#         :rtype: str
#         """
#         return ("meow\n" * n)

# number: int = int(input("What's the number"))

# TODO 'argparse' Library in PYTHON

# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#         n = int(sys.argv[2])
#         for _ in range(n):
#                 print("meow")
# else:
#     print("usage: meows.py")
# * simplifying above program
# * :import argparse library
import argparse

parser = argparse.ArgumentParser(description = "Meow like a cat")
parser.add_argument("-n", default = 1,help = "Nummber of times to meow", type = int)

args = parser.parse_args()
# print(args)

for _ in range(args.n):
        print("meow")

# * type in terminal: python [source file] -h to see what it does
