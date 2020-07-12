#Instead of packing, now we will used grid system, rows and columns
#Now instead of .pack() it will be .grid()
from tkinter import *
root = Tk()
my_Label = Label(root, text="1").grid(row=0, column=0)
my_Label_1 = Label(root, text="3").grid(row=0, column=1)
my_Label_2 = Label(root, text="2").grid(row=1, column=0)
my_Label_3 = Label(root, text="4").grid(row=1, column=1)
root.mainloop()
