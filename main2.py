from model.human import Human
from model.learner import Learner
from tkinter import *

FULL_SET = []
TRUE_RESULT = {}


def check():
    h = height.get()
    w = weight.get()
    print(int(h), int(w))
    hum = Human("a", int(h), int(w), "Male")
    FULL_SET.append(hum.get_fuzzy_info())
    boosting()


def create_training_data():
    FULL_SET.clear()
    with open('train.txt', 'r') as f:
        for line in f.readlines():
            temp_list_attr = line.split('\t')
            FULL_SET.append(Human(
                temp_list_attr[0],
                int(temp_list_attr[2]),
                int(temp_list_attr[3]),
                temp_list_attr[1].strip()
            ).get_fuzzy_info())
            TRUE_RESULT[temp_list_attr[0]] = int(temp_list_attr[4])
        f.close()


def boosting():
    weak_learner = []
    boost_set = {}
    result = {}

    for item in FULL_SET:
        boost_set[item] = Learner([item]).action()

    tmp_boost_set = {}
    for k, learner in boost_set.items():
        if learner.is_terminated():
            result = {**result, **{hum.name: hum.cls.__name__ for hum in learner.itemset}}
        else:
            tmp_boost_set[k] = learner
    boost_set = tmp_boost_set

    round_ = 0
    while len(boost_set) > 0:
        for item, _ in boost_set.items():
            weak_learner.append(item.name)
        print("Weak learner: #", weak_learner)

        sorted_boost_set = sorted(boost_set.items(), key=lambda v: v[1].get_dp())
        ramp = {}
        for i in sorted_boost_set:
            ramp[i[0]] = i[1]

        item = list(ramp.items())[0][0]
        item_learner = list(ramp.items())[0][1]

        print("Weakest learner to be combined: #", [item_.name for item_ in item_learner.itemset])

        del boost_set[item]

        for k, learner in boost_set.items():
            learner.add_another_weak_learner(item)

        for k, learner in boost_set.items():
            learner.action()

        tmp_boost_set = {}
        for k, learner in boost_set.items():
            if learner.is_terminated():
                # result += [(hum.name, hum.cls.index) for hum in learner.itemset]
                result = {**result, **{hum.name: hum.cls.__name__ for hum in learner.itemset}}
            else:
                tmp_boost_set[k] = learner
        boost_set = tmp_boost_set

        round_ = round_ + 1
        weak_learner = []
        print("--------8<---------- round: #", round_, "input left: #", len(boost_set))
        mlabel2 = Label(mGui, text=result['a'])
        mlabel2.place(x=75, y=150)


create_training_data()

mGui = Tk()
height = StringVar()
weight = StringVar()

mGui.geometry('250x180')
mGui.title("Health Checker")

mLabel = Label(mGui, text="Please import your information")
mLabel.place(x=20, y=10)
mLabelW = Label(mGui, text="Weight")
mLabelW.place(x=10, y=50)
mWeight = Entry(mGui, textvariable=weight)
mWeight.place(x=60, y=50)
mLabelW = Label(mGui, text="Height")
mLabelW.place(x=10, y=80)
mHeight = Entry(mGui, textvariable=height)
mHeight.place(x=60, y=80)
mButton = Button(mGui, text="Check", command=check)
mButton.place(x=90, y=120)

mGui.mainloop()
