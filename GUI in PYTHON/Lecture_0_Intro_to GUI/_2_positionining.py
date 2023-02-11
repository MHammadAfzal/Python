# ! Positioning with tkinter's grid system

# from tkinter import *

# root = Tk()

# myLabel1 = Label(root, text = "Hello, world")
# myLabel2 = Label(root, text="Hello, Hammad")
# * creating a label widget

# myLabel1.pack()
# myLabel2.pack()

# myLabel1.grid(row = 0, column = 0 )
# myLabel2.grid(row = 1, column = 0)
# myLabel2.grid(row = 1, column = 1)
# myLabel2.grid(row = 1, column = 5)
# * Shoving onto the screen

"""
: grid layout contains rows and columns

: param: rows, columns
: rows: on which horizontal line the item should be on the screen
: column: on which vertical line the item should be on the screen

: important: items are relative to each other ... see visual example by uncommenting label with column = 5 and column = 1
"""


# * CONCLUSION - we can reduce the steps
# Label(root, text = "Hello, world").grid(row = 0, column = 0 )
# Label(root, text="Hello, Hammad").grid(row = 1, column = 5)

# root.mainloop()

# TODO study creating buttons by using tkinter
