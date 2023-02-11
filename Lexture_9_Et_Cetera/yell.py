# ! map in PYTHON


# def main():
#     # yell("This is CS50")
#     # yell(["This", "is", "CS50"])
#     yell("This", "is", "CS50")


"""
: first yell function yell(phrasse)
: second yell function yell(words)
: third yell function yell(*words)
"""


# def yell(phrase):
#     print(phrase.upper())


# def yell(words):
#     upperCased = []
#     for word in words:
#         upperCased.append(word.upper())
#     # print(upperCased)
#     print(*upperCased)


# def yell(*words):
#     upperCased = []
#     for word in words:
#         upperCased.append(word.upper())
#     print(*upperCased)


# * Using map
# def yell(*words):
#     upperCased = map(str.upper, words)
#     print(*upperCased)


# if __name__ == "__main__":
#     main()


# ! List Comprehension in PYTHON
# def main():
#     yell("This", "is", "CS50")


# def yell(*words):
#     upperCased = [word.upper() for word in words]
#     print(*upperCased)


# if __name__ == "__main__":
#     main()
