
# ! XML in PYTHON

import xml.etree.ElementTree as ET

# * Example 1
# data = """ 
#         <person>
#             <name>M Hammad</name>
#             <phone type="intl">0348-7244160</phone>
#             <email hide="yes" />
#         </person>
#         """
# tree = ET.fromstring(data)
# # print(tree)
# print("Name:",tree.find("name").text)
# print("Phone:",tree.find("phone").text)
# print("Attr:",tree.find("email").get("hide"))
# * Example 2
# data = """
# <stuff>
#     <users>
#         <user x="2">
#             <id>01</id>
#             <name>Hammad</name>
#         </user>
#         <user x="7">
#             <id>02</id>
#             <name>Fahad</name>
#         </user>
#     </users>
# </stuff>"""

# stuff = ET.fromstring(data)
# # print(stuff)
# li = stuff.findall("users/user")
# # print(li)
# print("User Count:", len(li))

# for item in li:
#     print("Name:", item.find("name").text)
#     print("ID:", item.find("id").text)
#     print("Attribute:", item.get("x"))
