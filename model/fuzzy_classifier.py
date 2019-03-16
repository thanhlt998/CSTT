import helper
from model import human
from model.fuzzy_attribute import FuzzyAttribute
from model.output import ShouldEatLess, ShouldDoExercise, ShouldEatMore, Fine
import helper
from fuzzy_rule.height_rule import Height
from fuzzy_rule.weight_rule import Weight

import operator


class FuzzyClassifier:
    deleted_rule = []
    combined_rules = {}

    def __init__(self, itemset):
        self.rule_classify = {
            "fuzzy_short|fuzzy_light": ShouldEatMore,
            "fuzzy_short|fuzzy_medium": ShouldDoExercise,
            "fuzzy_short|fuzzy_heavy": ShouldEatLess,
            "fuzzy_average|fuzzy_light": ShouldDoExercise,
            "fuzzy_average|fuzzy_medium": Fine,
            "fuzzy_average|fuzzy_heavy": ShouldEatLess,
            "fuzzy_tall|fuzzy_light": ShouldEatMore,
            "fuzzy_tall|fuzzy_medium": Fine,
            "fuzzy_tall|fuzzy_heavy": ShouldDoExercise
        }

        self.class_determine = helper.safe_invert(self.rule_classify)

        self.output_class = {
            ShouldEatLess: FuzzyAttribute(),
            ShouldDoExercise: FuzzyAttribute(),
            ShouldEatMore: FuzzyAttribute(),
            Fine: FuzzyAttribute()
        }

        self.itemset = itemset

        self.get_combined_rules()

    def get_combined_rules(self):
        r = {}
        for r1 in [method for method in dir(Height) if
                   callable(getattr(Height, method)) and method.startswith('fuzzy')]:
            for r2 in [method for method in dir(Weight) if
                       callable(getattr(Weight, method)) and method.startswith('fuzzy')]:
                r["%s|%s" % (r1, r2)] = FuzzyAttribute()
        self.deleted_rule = []
        self.combined_rules = r

    def calculate_combined_rules_membership(self, item, applied_rule):
        dom = 1
        for key, _ in item.fuzzy_dom:
            if str(key) in applied_rule:
                dom = dom * item.fuzzy_dom[key]
        return dom

    def calculate_beta(self):
        for key, value in self.combined_rules.items():
            applied_rule = key.split("|")
            beta_rule = 0

            for obj in self.itemset:
                dom = self.calculate_combined_rules_membership(obj, applied_rule)
                beta_rule = beta_rule + dom

            self.combined_rules[key].beta = beta_rule

    def calculate_certainty_factor(self):
        for key, value in self.class_determine.items():
            rj = value
            beta_arr = []
            for rule in rj:
                beta_arr.append(self.combined_rules[rule].beta)
            beta_arr = sorted(beta_arr, reverse=True)
            if len(beta_arr) == 1:
                self.output_class[key].set_certainty_factor(1.0)
            elif len(beta_arr) == 0:
                self.output_class.__delitem__(key)
                self.deleted_rule.append(key)
                continue
            elif len(beta_arr) >= 2 and beta_arr[0] == beta_arr[1]:
                self.output_class.__delitem__(key)
                self.deleted_rule.append(key)
                continue
            else:
                self.output_class[key].set_certainty_factor(helper.calculate_certainty_factor(beta_arr, beta_arr[0]))

    def generate_if_then_rules(self):
        self.calculate_beta()
        self.calculate_certainty_factor()
        return self

    def reasoning(self, item):
        cls_attr = {
            ShouldEatLess: FuzzyAttribute(),
            ShouldDoExercise: FuzzyAttribute(),
            ShouldEatMore: FuzzyAttribute(),
            Fine: FuzzyAttribute()
        }

        for r in self.deleted_rule:
            cls_attr.__delitem__(r)

        for clss, rj in self.class_determine:
            if self.output_class[clss] is None:
                continue
            for rule in rj:
                applied_rule = rule.split("|")
                dom = self.calculate_combined_rules_membership(item, applied_rule)
                alpha = self.output_class[clss].get_certainty_factor() * dom
                if alpha > cls_attr[clss].get_alpha():
                    cls_attr[clss].set_alpha(alpha)
        sort_by_attr = sorted(cls_attr.items(), key=lambda v: v[1].get_alpha())
        cls_attr = {}
        for attr in sort_by_attr:
            cls_attr[attr[0]] = attr[1]

        if len(cls_attr) == 1:
            return list(cls_attr.items())[-1][0]

        if list(cls_attr.items())[-2][1].get_alpha() == list(cls_attr.items())[-1][1].get_alpha():
            return None
        else:
            return list(cls_attr.items())[-1][0]

    # def deduce(self, cls_attr):
    #     sort_by_attr = sorted(cls_attr.items(), key=lambda v: v.get_alpha())
    #     cls_attr = {}
    #     for attr in sort_by_attr:
    #         cls_attr[attr[0]] = attr[1]

    #     if len(cls_attr) == 1:
    #         return list(cls_attr.items())[-1][0]

    #     if list(cls_attr.items())[-2][1].get_alpha() == list(cls_attr.items())[-1][1].get_alpha():
    #         return None
    #     else:
    #         return list(cls_attr.items())[-1][0]
