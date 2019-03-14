from fuzzy_rule.height_rule import Height
from fuzzy_rule.weight_rule import Weight


class Human:
    APPLIED_FUZZY_RULES = [Height, Weight]

    def __init__(self, name, height, weight, sex):
        self.name = name
        self.height = height
        self.weight = weight
        self.sex = sex
        self.fuzzy_dom = {}

    def __eq__(self, other):
        return self.name == other.name

    def get_fuzzy_info(self):
        for rule in self.APPLIED_FUZZY_RULES:
            fuzzy_rules = [method for method in dir(rule) if callable(getattr(rule, method)) and method.startswith('fuzzy')]
            for fuzzy_rule in fuzzy_rules:
                self.fuzzy_dom[fuzzy_rule] = getattr(rule, fuzzy_rule)(self)
