
# ! Generator, iterators ,yield in PYTHON


# def main():
#     n = int(input("What's n? "))

#     for i in lock(n):
#         print(i)


# def lock(x):
#     allLocks = []
#     for i in range(x):
#         allLocks.append("🔏" * i)
#     return allLocks
# * If we give input of large number like 10000000 the program hangs 

# TODO So, using generator to resolve this issues
# * 'yield' keyword in PYTHON

# def lock(x):
#     for i in range(x):
#         yield "🔏" * i

# if __name__ == "__main__":
#     main()
