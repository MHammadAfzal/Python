# first, _ = input("What's your name?").split(" ")
# print("Hello,", first)
# * Lets dig it deep
# TODO Unpacking Lists

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# coins = [100,50,25]

# print(total(100,50,25), "knuts")
# print(total(coins[0],coins[1],coins[2]), "knuts")

# print(total(*coins), "knuts")
# * Unpacking by putting * before list name
# TODO Unpacking Dictionaries
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = {
#     "galleons": 100,
#     "sickles": 50,
#     "knuts": 25,
# }

# print(total(galleons=100, sickles=50, knuts=25), "knuts")
# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts")

# print(total(**coins), "knuts")
# * Unpacking by putting 2 * before dict name


# TODO '*args' and '**kwargs' in PYTHON

# def f1(*args):
#     print("Positional: ", args)


# # * returns a list

# f1(100)
# f1(100, 50)
# f1(100, 50, 25)
# f1(100, 50, 25, 5)


# def f2(**kwargs):
#     print("Named:", kwargs)


# # * returns a dict

# f2(galleons=100, sickles=50, knuts=25)
