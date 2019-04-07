# import helper
from model.human import Human
# from model import fuzzy_attribute
# from model import output
# from fuzzy_rule import height_rule
# from fuzzy_rule import weight_rule
# from model import fuzzy_classifier
from model.learner import Learner
from sklearn.metrics import accuracy_score

import operator

FULL_SET = []
TRUE_RESULT = {}


def create_training_data():
    with open('train.txt', 'r') as f:
        for line in f.readlines():
            temp_list_attr = line.split('\t')
            # if temp_list_attr[1].strip() == 'Female':
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
    result = []

    for item in FULL_SET:
        boost_set[item] = Learner([item]).action()

    # for k, learner in boost_set.items():
    #     if learner.is_terminated():
    #         del boost_set[k]

    tmp_boost_set = {}
    for k, learner in boost_set.items():
        if learner.is_terminated():
            result += [(hum.name, hum.cls.index) for hum in learner.itemset]
        else:
            tmp_boost_set[k] = learner
    boost_set = tmp_boost_set
    # result = [k: learner for k, learner in boost_set.items() if learner.is_terminated()]
    # boost_set = {k: learner for k, learner in boost_set.items() if not learner.is_terminated()}

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

        # for k, learner in boost_set.items():
        #     if learner.is_terminated():
        #         del boost_set[k]

        tmp_boost_set = {}
        for k, learner in boost_set.items():
            if learner.is_terminated():
                result += [(hum.name, hum.cls.index) for hum in learner.itemset]
            else:
                tmp_boost_set[k] = learner
        boost_set = tmp_boost_set

        # boost_set = {k: learner for k, learner in boost_set.items() if not learner.is_terminated()}

        round_ = round_ + 1
        weak_learner = []
        print("--------8<---------- round: #", round_, "input left: #", len(boost_set))

    true_classifier = [TRUE_RESULT[name] for name, index in result]
    pred_classifier = [index for name, index in result]
    print("Accuracy: %.2f" % (
                accuracy_score(true_classifier, pred_classifier) * 100))

    test_count = []
    for i in range(len(result)):
        if result[i][1] != true_classifier[i]:
            # print(f'{result[i][0]}\t{result[i][1]}\t{true_classifier[i]}')
            test_count.append((result[i][1], true_classifier[i]))

    test_count_set = list(set(test_count))
    test_count_set = sorted(test_count_set, key=lambda v: test_count.count(v))
    for test in test_count_set:
        print(test, '\t', test_count.count(test))


create_training_data()
boosting()
