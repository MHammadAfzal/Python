print("Hello world")

# ! Regular Expressions in PYTHON

# * Lets make a simple program using regex
# email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")
# * Lets put some more login in it
# email = input("What's your email? ").strip()

# userName, domain = email.split("@")

# if userName and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")
# * Lets be more precise
# if userName and domain.endswith(".nust.edu.pk"):
#     print("Valid")
# else:
#     print("Invalid")
# TODO Now we understand what regex can do. So lets introduce its library
# * Importing regex library 're'
import re
email = input("What's your email? ").strip()
# TODO Regular Expressions Patterns
# *    '.'  accepts any character except newline
# *    '*'  accepts 0 or more repitions
# *    '+'  accepts 1 or more repitions
# *    '?'  accepts 0 or 1 repitions
# *   '{m}' accepts m repitions
# * '{m,n}' accepts m-n repitions
# * Lets start now
# if re.search(".*@.*",email):
#     print("Valid")
# else:
#     print("Invalid")
# * Make it better
# if re.search(".+@.+",email):
#     print("Valid")
# else:
#     print("Invalid")
# * Same as above
# if re.search("..*@..*",email):
#     print("Valid")
# else:
#     print("Invalid")
# * Getting better
# if re.search(r".+@.+\.edu",email):
#     print("Valid")
# else:
#     print("Invalid")
# * Restricting more...
# * '^' matches start of string
# * '$' matches end of string just before new line at the end of string
# if re.search(r"^.+@.+\.edu$",email):
#     print("Valid")
# else:
#     print("Invalid")
# TODO regex - set of characters
# * [] --> set of characters
# * [^] --> complementing set
# if re.search(r"^[^@]+@[^@]+\.edu$",email):
#     print("Valid")
# else:
#     print("Invalid")
# * Improving above code
# if re.search(r"^[a-zA-z0-9_]+@[a-zA-z0-9_]+\.edu$",email):
#     print("Valid")
# else:
#     print("Invalid")
# TODO Character classes
# * '\w' means alpha-numeric and underscore value
# * '\W' not a word character
# * '\d' decimal digit
# * '\D' not a decimal digit
# * '\s' whitespace character
# * '\S' not a whitespace character
# * ---- Lets begin ----
# if re.search(r"^\w+@\w+\.(edu|pk|com)$",email):
#     print("Valid")
# else:
#     print("Invalid")
# * For uppercase letters
# if re.search(r"^\w+@\w+\.(edu|pk|com)$",email, re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")
# * For addresses like hammad@mcs.nust.edu
# if re.search(r"^\w+@(\w+.)?\w+\.(edu|pk|com)$",email, re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")
# * re.match() and re.fullmatch()

# * Go to format.py for further knowledge...