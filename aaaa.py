import sys
from tkinter import *
import tkinter.messagebox
from model.human import Human
from model.learner import Learner

def check():
    
    h = height.get()
    w = weight.get()
    hum = Human("a", int(h), int(w), "Male")
    learner = Learner([hum.get_fuzzy_info()]).action()
    if learner.is_terminated:
        result = hum.cls.__name__
    tkinter.messagebox.showinfo("Result", result)

    

mGui = Tk()
height = StringVar()
weight = StringVar()


mGui.geometry('250x180')
mGui.title("Health Checker")

mLabel = Label(mGui, text="Please import yout information")
mLabel.pack(side=TOP, padx=5, pady=5)
mLabelW = Label(mGui, text="Weight")
mLabelW.place(x=10,y=50)
mWeight = Entry(mGui, textvariable=weight)
mWeight.place(x=60,y=50)
mLabelW = Label(mGui, text="Height")
mLabelW.place(x=10,y=80)
mHeight = Entry(mGui, textvariable=height)
mHeight.place(x=60,y=80)
mButton = Button(mGui, text="Check", command = check)
mButton.place(x=90,y=120)

mGui.mainloop()
