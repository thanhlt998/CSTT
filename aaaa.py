import sys
from tkinter import *
from model.human import Human
from model.learner import Learner

def check():
    
    h = height.get()
    w = weight.get()
    hum = Human("a", int(h), int(w), "Male")
    learner = Learner([hum.get_fuzzy_info()]).action()
    if learner.is_terminated:
        result = hum.cls.__name__
    mlabel2 = Label(mGui, text=result)
    mlabel2.place(x=75, y=150)

mGui = Tk()
height = StringVar()
weight = StringVar()


mGui.geometry('250x180')
mGui.title("Health Checker")

mLabel = Label(mGui, text="Please import yout information")
mLabel.place(x=20,y=10)
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
