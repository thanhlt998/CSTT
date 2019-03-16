# import helper
from model.human import Human
# from model import fuzzy_attribute
# from model import output
# from fuzzy_rule import height_rule
# from fuzzy_rule import weight_rule
# from model import fuzzy_classifier
from model.learner import Learner

import operator

FULL_SET = []


def create_training_data():
    with open('training_patterns', 'r') as f:
        for line in f.readlines():
            temp_list_attr = line.split('\t')
            FULL_SET.append(Human(
                temp_list_attr[0],
                int(temp_list_attr[1]),
                int(temp_list_attr[2]),
                temp_list_attr[3]
            ).get_fuzzy_info())
        f.close()


def boosting():
    weak_learner = []
    boost_set = {}

    for item in FULL_SET:
        boost_set[item] = Learner([item]).action()

    # for k, learner in boost_set.items():
    #     if learner.is_terminated():
    #         del boost_set[k]

    boost_set = {k: learner for k, learner in boost_set.items() if learner.is_terminated()}

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

        print("Weakest learner to be combined: #", item_learner.itemset[0].name)

        del boost_set[item]

        for k, learner in boost_set.items():
            learner.add_another_weak_learner(item)

        for k, learner in boost_set.items():
            learner.action()

        # for k, learner in boost_set.items():
        #     if learner.is_terminated():
        #         del boost_set[k]

        boost_set = {k: learner for k, learner in boost_set.items() if learner.is_terminated()}

        round_ = round_ + 1
        weak_learner = []
        print("--------8<---------- round: #", round_, "input left: #", len(boost_set))


create_training_data()
boosting()
