from model.human import Human
from model.learner import Learner
from tkinter import *
import tkinter.messagebox, tkinter.filedialog
import numpy as np
import matplotlib.pyplot as plt

FULL_SET = []
TRUE_RESULT = {}


# def check():
#     create_training_data()
#     h = height.get()
#     w = weight.get()
#     print(int(h), int(w), v.get())
#     hum = Human("a", int(h), int(w), v.get())
#     FULL_SET.append(hum.get_fuzzy_info())
#     boosting()


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

    return result['a']


def boosting2(name):
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
        # return result[name]
        return result


# def onImport():
#     FULL_SET.clear()
#     ftypes = [('text files', '*.txt'), ('All files', '*')]
#     dlg = tkinter.filedialog.Open(mGui, filetypes=ftypes)
#     fl = dlg.show()
#     if fl != '':
#         upload_res = []
#         with open(fl, 'r') as f:
#             for line in f.readlines():
#                 temp_list_attr = line.split('\t')
#                 FULL_SET.append(Human(
#                     temp_list_attr[0],
#                     int(temp_list_attr[2]),
#                     int(temp_list_attr[3]),
#                     temp_list_attr[1].strip()
#                 ).get_fuzzy_info())
#             f.close()
#             upload_res = boosting2('a').values()
#         showPlot(upload_res)


def getIndex(res):
    objects = {
        'ExtremelyWeak':0, 'Weak':0, 'Normal':0, 'Overweight':0, 'Obesity':0, 'ExtremelyObesity':0
    }
    for i in res:
        objects[i] += 1
    shape = []
    num = []
    for k, v in objects.items():
        shape.append(k)
        num.append(v)
    # y_pos = np.arange(len(shape))
    print(objects)
    return shape, num

    # plt.bar(y_pos, num, align='center', alpha=0.5)
    # plt.xticks(y_pos, shape)
    # plt.ylabel('Number')
    # plt.title('Health statistical')

    # plt.savefig('templates/static/img/res.png')