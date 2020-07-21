#Creating a button is very simple. A button, like any other thing is a widget
#And getting a button to do something

from tkinter import *
root = Tk()
def my_Click():
    my_Label = Label(root, text="Look, i clicked!")
    my_Label.pack()
my_Button = Button(root, text="Click me", command = my_Click)
my_Button.pack()
root.mainloop()
