#Importing
from tkinter import *
#Setup
root = Tk()
root.title("Name")
root.configure(background="blue")
name = StringVar()
namery = ""

def naming():
        heading = Label(root, text="Name", fg="red", bg="blue", font=("arial", 40, "bold")).pack()
        #Instruction label
        Instruction = Label(root, text="Type in your name.", bg="blue")
        Instruction.place(x=0, y=50)
        #Label
        Namelabel = Label(root, text="Enter your name:", bg="blue").place(x=0, y= 100)
        #Entry box
        Namebox = Entry(root, textvariable=name, bg="blue")
        Namebox.place(x=100, y=100)
        #Submit button
        def Submiter():
                namery = name.get()
                labeler = Label(root, text="Hello " + namery + "!", bg="blue").pack()
        Submitbutton = Button(root, text="Submit", command=Submiter, bg="blue").pack()
naming()
#Mainloop
root.mainloop()
