#code1-4

from tkinter import *

window = Tk()

photo = PhotoImage(file = "gif/dog.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()