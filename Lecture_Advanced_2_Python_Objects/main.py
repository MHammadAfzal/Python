print("Hello, world")
# ! PYTHON OBJECTS IN PYTHON


# class LetsParty:
#     x = 0

#     def party(self):
#         self.x += 1
#         print("So far", self.x)


# Hammad = LetsParty()
# Hammad.party()
# Hammad.party()
# Hammad.party()
# Hammad.party()


# TODO Constructor in Classes

# class Leader:
#     x = 0

#     def __init__(self, n):
#         # * Defining constructor
#         self.name = n
#         print(self.name, "is a leader")

#     def party(self):
#         self.x += 1
#         print(self.x, "members are under the leadership of", self.name)


# ldr = Leader("Hammad")
# ldr.party()
# ldr.party()
# ldr.party()


# TODO Inheritance in PYTHON


class Person:
    x = 0

    def __init__(self, n):
        # * Defining constructor
        self.name = n
        print(self.name, "is in Pakistan")

    def people(self):
        self.x += 1
        print(self.x, "persons are in Pakistan")


class Sialkot(Person):
    y = 0

    def inSialkot(self):
        self.people()
        self.y += 1
        print(self.y, "persons are in Sialkot")


# person = Person("Ali")
# person.people()
# person.people()
# person.people()

sialkot = Sialkot("Hammad")
sialkot.inSialkot()
sialkot.inSialkot()
sialkot.inSialkot()
sialkot.inSialkot()
sialkot.inSialkot()
