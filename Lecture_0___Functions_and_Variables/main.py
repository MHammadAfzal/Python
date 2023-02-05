# print("Hello World")

# <--------- Input (Getting input from user) -------->

# input("What's your name? ")

# ***** Need of Variables ******
"""Multiline Comments in python"""

#  * ask user for the name 
# a = input("What's your name? ")
#  * say hello to user hammad
# print("Hello ");
# print(a)
# * prevent print function to jump onto a new line
# print("Hello ", end="")
# print(a)

# * another way to say hello
# print("Hello " + a)
# print("Hello", a, sep = "")
# print("Hello", a)

# * double cotation marks in print
# print("Hello \"Hammad\"")

# * Latest and best feature for above problems
# name = input("What's Your Name? ")
# print(f"Hello {name}")

# !STRINGS

# * While giving input if user put some space before and after input then see what happens like...
# name = "      hammad afzal mohal      "
# print(f"Hello {name} !")

# * So to solve this problem we have some string methods...
# TODO remove whitespaces from name
# name = name.strip()
# print(f"Hello {name}")
# TODO make name capitalized
# name = name.capitalize();
# print(f"Hello {name}")
# TODO make all words capitalized
# name = name.title()
# print(f"Hello {name}")
# TODO remove whitespaces and capitalize all words
# name = name.strip().title();
# print(f"Hello {name}")
# TODO split name into first name and last name
# first, middle, last = name.split(" ")
# print(f"Hello! \nYour first name is :  {first} \nYour middle name is :  {middle} \nYour last name is :  {last} ")

# !INTEGER Values

# a = input()
# * a is a string so convert a to integer
# print(int(a) + 7)


# ? Make a simple calculator
print("Solve this... x + y")
# x = int(input("Whats's x ? "))  
# y = int(input("What' y? ")) 
# print(x + y )
# * one-liner ----> Try not to use one-liner as it can become complicated
# print(int(input("What's X? ")) + int(input("What's Y? ")))

# ! FLOAT Point Values
# x = float(input("Whats's x ? "))  
# y = float(input("What' y? ")) 
# z = x + y
# print(z)

# * Round Values
# z = round(z,3)
# print(z)

# * Numeric Formatting
# print(f"{z:,}")

# * Division
# x = float(input("Whats's x ? "))  
# y = float(input("What' y? ")) 
# z = x / y
# print(round(z,2))
# print(f"{z:.2f}")

# ! FUNCTIONS IN PYTHON

# name = input("What's your name? ")

# * Scope

# def main() :
#     sayHello()
#     name = input("What's your name? ")
#     sayHello(name)

# def sayHello(to = "world"):
#     print("Hello", to)


# main()

# * Return Values
def main():
    x = int(input("What's X? "))
    print("X squared is : ", square(x))

def square(n = "Not Exist"):
    return int (n * n)

main()