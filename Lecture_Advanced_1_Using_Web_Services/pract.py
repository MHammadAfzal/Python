# ! JSON IN PYTHON

import json

# data = '''{
#     "name": "Hammad",
#     "phone": {
#         "type" : "intl",
#         "number": "03432039299"
#     },
#     "email": {
#         "hide": "yes"
#     }
# }'''

# info = json.loads(data)
# # print(info)
# print("Name:", info["name"])
# print("Hide:", info["email"]["hide"])

input = '''
[
    {   "id": "001",
        "x": "2",
        "name": "Hammad"
    },
    {   "id": "009",
        "x": "7",
        "name": "Fahad"
    }
]'''

info = json.loads(input)
# print(info)
print("User Count: ", len(info))

for item in info:
    print("Name:", item["name"])
    print("ID:", item["id"])
    print("Attribute:", item["x"])
