# import re

# name = input("What's your name? ").strip()
# if "," in name:
#     last,first = name.split(", ?")
#     name = f"{first} {last}"
# print(f"Hello, {name}")
# * Capturing Groups in regex
# name = input("What's your name? ").strip()
# matches = re.search("^(.+), *?(.+)$",name)
# print(matches)
# if matches:
#     # last, first = matches.groups()

#     # last = matches.groups(1)
#     # first = matches.groups(2)

#     # name = f"{first} {last}"
#     name = f"{matches.group(2)} {matches.group(1)}"

# print(f"Hello, {name}")
# * Warlus Operator (:=) in PYTHON regex
# name = input("What's your name? ").strip()
# if matches:= re.search("^(.+), *?(.+)$",name):
#     name = f"{matches.group(2)} {matches.group(1)}"
# print(f"Hello, {name}")
# TODO Extract from strings in PYTHON

# * Go to twitter.py for this topic