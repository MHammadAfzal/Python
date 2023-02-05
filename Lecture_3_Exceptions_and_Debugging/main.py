print("Hello World!")

# ! Exceptions in PYTHON

# * try and except
# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print("x is",x)
# * else keyword in try and except
# TODO make above program user-friendly
# * Introducing loop to keep asking user for a number if user gave the input wrong
# while True:
    # try:
        # * Ask user to input a number
        # x = int(input("What's x? "))
    # except ValueError:
        # * Error occurs so start the loop again after printing what the error was
        # print("x is not an integer")
    # else:
        # * Break the loop as user entered the number correct
        # break
# * Print the value user entered
# print("x is",x)
# TODO  Proper form of above program
# def main():
#     x = get_int()
#     print("x is",x)
# # * Defining a function to get a input from a user
# def get_int():
#     while True:
#         try:
#             # * Ask user to input a number. If entered correctly, return it
#             return int(input("What's x? "))
#         except ValueError:
#             # * Error occurs so start the loop again after printing what the error was
#             print("x is not an integer")
# # * Call main function
# main()
# * pass keyword in Python Exceptions
# def main():
#     x = get_int()
#     print("x is",x)
# def get_int():
#     while True:
#         try:
#            # * Ask user to input a number. If entered correctly, return it
#             return int(input("What's x? "))
#         except:
#             # * Pass to next step and do nothing
#             pass
# # * Call main function
# main()
# * Using function arguments to get more control to main program
# def main():
#     x = get_int("What's x? ")
#     print("x is",x)
# def get_int(prompt):
#     while True:
#         try:
#            # * Ask user to input a number. If entered correctly, return it
#             return int(input(prompt))
#         except:
#             # * Pass to next step and do nothing
#             pass
# # * Call main function
# main()
# TODO raise keyword in Python Exceptions......

# ! Debugging in PYTHON

def main():
    height = int(input("What's height? "))
    pyramid(height)

def pyramid(h):
    for i in range(h):
        print("#" * i)
        
main() # * DEBUGGING from this breakpoint