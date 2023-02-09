# ! Classes and objects in PYTHON

# TODO use class keyword to define class
# class Student:  # * class
#     ...


# def main():
#     student = get_student() # * getting object and storing in student
#     print(f"{student.name} from {student.city}")

# def get_student():
#     student = Student() # * object
#     student.name = input("Name: ").strip()
#     student.city = input("City: ").strip()
#     return student # * return object

# main()


# TODO Instance Methods
# * giving more power to classes
# class Student:
#     def __init__(self, name, city):
#         #  ----------------
#         if not name:  # * name == ""
#             raise ValueError("Missing Name")  # * raising exception
#         if city not in ["Sialkot", "Lahore", "Isb"]:
#             raise ValueError("Invalid City")  # * raising exception
#         #  ----------------
#         self.name = name
#         self.city = city


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.city}")


# def get_student():
#     name = input("Name: ").strip()
#     city = input("City: ").strip()
#     return Student(name, city)
#     # try:
#     #     return Student(name,city)
#     # except ValueError:
#     #     ...

# main()

# TODO String method in Classes

# class Student:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

#     def __str__(self):  # * will return string to object
#         return f"{self.name} from {self.city}"


# def main():
#     student = get_student() # * getting f("{Hammad} from {Sialkot}")
#     print(student)


# def get_student():
#     name = input("Name: ").strip()
#     city = input("City: ").strip()
#     return Student(name, city) # * getting self.name from self.city


# main()

# TODO Custom Methods in Classes

# class Student:
#     def __init__(self, name, city, college):
#         self.name = name
#         self.city = city
#         self.college = college

#     def __str__(self):  # * will return string to object
#         return f"{self.name} from {self.city} studying in {self.college}"

#     def get_charm(self):
#         match self.college:
#             case "GCU":
#                 return "🤞"
#             case _:
#                 return "👌"


# def main():
#     student = get_student()
#     print(student)
#     print(student.get_charm())


# def get_student():
#     name = input("Name: ").strip()
#     city = input("City: ").strip()
#     college = input("College: ").strip()
#     return Student(name, city, college)


# main()

# TODO Properties, Getters and Setters in Classes

# * '@property' keyword in classes


# class Student:
#     def __init__(self, name, city):
#         #  ----------------
#         if not name:  # * name == ""
#             raise ValueError("Missing Name")  # * raising exception
#         #  ----------------
#         self.name = name
#         self.city = city # * will call setter method of city

#     # * getter
#     @property
#     def name(self):
#         return self._name

#     # * setter
#     @city.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Missing Name")  # * raising exception
#         self._name = name


#     # * getter
#     @property
#     def city(self):
#         return self._city

#     # * setter
#     @city.setter
#     def city(self, city):
#         if city not in ["Sialkot", "Lahore", "Isb"]:
#             raise ValueError("Invalid City")  # * raising exception
#         self._city = city


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.city}")


# def get_student():
#     name = input("Name: ").strip()
#     city = input("City: ").strip()
#     return Student(name, city)
#     # try:
#     #     return Student(name,city)
#     # except ValueError:
#     #     ...


# main()

# * Types of classes
# print(type(50))
# print(type("Hello, world"))
# print(type([]))
# print(type(list()))
# print(type({}))
# print(type(dict()))

# TODO CLASS METHODS

# * Go to class_methods.py tmo move further
