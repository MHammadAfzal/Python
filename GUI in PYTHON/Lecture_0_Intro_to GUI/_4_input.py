# ! Creating input fields by using tkinter

from tkinter import *

root = Tk()
# creating a window

def get_name():
    greet = f"Hello, {e.get()}"
    label = Label(root, text = greet)
    label.pack()

e = Entry(root, width=50, bg="blue", fg="white", borderwidth = 5)
e.pack()
e.insert(0,"e.g. Hammad")

"""
: Entry: an input widget used to get widgets

:param: root, width, fg, bg, borderwidth
: root: the input will go to the root
: width: width of the input field
: fg: foreground color in short text color for input
: bg: background color for input
: borderwidth: borderwidth of input field

:functions: insert, get, pack
: insert: insert the default text in an input field
: get: get the input entered by the user
: pack: shove input field on to the screen
"""

click = Button(root, text = "Enter your name", command = get_name)
click.pack()

root.mainloop()