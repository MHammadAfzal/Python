from tkinter import *

root = Tk()

"""
: tkinter is a library which is used for GUI in PYTHON
: Tk() for a window
"""

myLabel = Label(root, text="Hello, world")
myLabel.pack()
"""
: Created a label widget

: param: root, text
: root: label widget will go to our root
: text: It will

: mylabel.pack(): shoving onto the screen
"""

root.mainloop()

"""
: root.mainloop(): making our root i.e. screen our main loop in which we will detect events
"""
