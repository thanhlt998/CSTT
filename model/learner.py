from model.fuzzy_classifier import FuzzyClassifier
import itertools
import math


class Learner:
    T = 7

    def __init__(self, itemset):
        # self.itemset = list(itertools.chain(*itemset))
        self.itemset = itemset
        self.dp = 0
        self.cp = 0
        self.t = 1
        self.delta = 0
        self.terminated = False

        self.fuzzy_classifier = FuzzyClassifier(itemset).generate_if_then_rules()

    def get_dp(self):
        return self.dp

    def add_another_weak_learner(self, _itemset):
        if self.t > self.T:
            self.terminated = True
            return

        self.itemset.append(_itemset)
        self.t = self.t + 1

        self.cp = 0
        self.fuzzy_classifier = FuzzyClassifier(self.itemset).generate_if_then_rules()

        return self

    def can_classified(self, item):
        if self.fuzzy_classifier.reasoning(item) is not None:
            return True
        else:
            return False

    def assign_class(self, item):
        clss = self.fuzzy_classifier.reasoning(item)
        item.of_class(clss)

    def action(self):
        self.calculate_cp()
        self.calculate_delta()
        self.update_dp()

        return self

    def calculate_cp(self):
        for item in self.itemset:
            if self.can_classified(item):
                self.assign_class(item)
                self.cp = self.cp + 1

        if len(self.itemset) == self.cp:
            self.terminated = True
        return self

    def calculate_delta(self):
        m = len(self.itemset)
        classified = 0
        for item in self.itemset:
            if not self.can_classified(item):
                classified = classified + 1

        epsilon = float(classified) / m
        self.delta = math.sqrt(1 - epsilon)

    def update_dp(self):
        self.dp = float(self.cp) / self.t
        return self

    def is_terminated(self):
        if self.terminated:
            for item in self.itemset:
                print("Terminated: #", str(item.name), " #", item.cls.__name__)
                # print("\n")
            return True
        else:
            return False
