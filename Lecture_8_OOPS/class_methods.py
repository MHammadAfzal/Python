# from random import choice

# ! Class Methods in PYTHON

# * '@classmethod' is used to define class method


# class Hat:
#     def __init__(self):
#         self.houses = ["Sialkot", "Lahore", "Isb"]

#     def sort(self, name):
#         print(name, "is in", choice(self.houses))


# hat = Hat()
# hat.sort("Hammad")

# * Class Variables and Class Methods

# class Hat:
#     houses = ["Sialkot", "Lahore", "Isb"]  # * class variable

#     @classmethod
#     def sort(cls, name):  # * class method
#         print(name, "is in", choice(cls.houses))


# Hat.sort("Hammad")
# Hat.sort("Ali")


# * Another example
# class Student:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

#     def __str__(self):
#         return f"{self.name} from {self.city}"

#     @classmethod
#     def get(cls):
#         name = input("Name: ")
#         city = input("City: ")
#         return cls(name, city)


# def main():
#     student = Student.get()
#     print(student)

# if __name__ == "__main__":
#     main()

# * Static Methods in Python

# TODO Inheritance in PYTHON Classes

# * Go to inheritance.py to study inheritance in PYTHON