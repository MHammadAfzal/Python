# class Student:
#     def __init__(self, name, city):
#         if not name:
#             raise ValueError("Missing Name")
#         self.name = name
#         self.city = city

# class Professor:
#     def __init__(self, name, subject):
#         self.name = name
#         if not name:
#             raise ValueError("Missing Name")
#         self.subject = subject

# * Using Inheritance

# class Univerity:
#     def __init__(self, name):
#         if not name:
#             raise ValueError("Missing Name")
#         self.name = name
#     def __str__(self):
#         return f"{self.name}"

# # * Student class extends University Class
# class Student(Univerity):
#     def __init__(self, name, city):
#         super().__init__(name)
#         self.city = city
#     def __str__(self):
#         return f"{self.name} from {self.city}"

# # * Professor class extends University Class
# class Professor(Univerity):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#     def __str__(self):
#         return f"{self.name} from {self.subject}"

# university = Univerity("NUST MCS")
# student = Student("Hammad","Sialkot")
# professor = Professor("Dr Saeed","CVT")

# print(university)
# print(student)
# print(professor)

# TODO Operation Overloading

# * Go to vault.py for better understanding