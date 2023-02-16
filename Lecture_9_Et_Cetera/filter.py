# ! filter in PYTHON
# students = [
#     {"name": "Hammad", "city": "Sialkot"},
#     {"name": "Ali", "city": "Qasoor"},
#     {"name": "Haroon", "city": "Nowshera"},
#     {"name": "Uzair", "city": "Qasoor"},
#     {"name": "Ayyan", "city": "Karachi"},
# ]

# qasoories = [student["name"] for student in students if student["city"] == "Qasoor"]

# # print(qasoories)
# for qasoor in sorted(qasoories):
#     print(qasoor)

# TODO Using filter to do the same

# def is_Qasoori(s):
#     return (s["city"] == "Qasoor")

# qasoories = filter(is_Qasoori, students)
# qasoories = filter(lambda s: s["city"] = "Qasoor", students)

# print(qasoories)
# for qasoor in sorted(qasoories, key = lambda s: s["name"]):
#     print(qasoor["name"])

# TODO Dict Comprehension in PYTHON

# students = ["Hammad", "Ali", "Haroon", "Uzair", "Ayyan"]

# Pakistani = []

# for student in students:
#     Pakistani.append({"name": student, "country": "Pakistan"})

# * Using List Comprehension
# Pakistani = [{"name": student, "country": "Pakistan"} for student in students]
# print(Pakistani)

# * Using Dict Comprehension

# Pakistanis = {student: "Pakistan" for student in students}
# print(Pakistanis)

# TODO enumerate in PYTHON

# students = ["Hammad", "Ali", "Haroon", "Uzair", "Ayyan"]

# for student in students:
#     print(student)
# * no numerical numbering

# for i in range(len(students)):
#     print( i + 1 , ":", students[i])
# * To do above procedure, we can use enumerate
# for i, student in enumerate(students):
#     print( i + 1 , ":", student)