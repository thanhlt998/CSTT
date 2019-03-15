class FuzzyAttribute:
    def __init__(self):
        self.beta = 0
        self.alpha = 0
        self.certainty_factor = 0

    def get_beta(self):
        return self.beta

    def set_beta(self, beta):
        self.beta = beta

    def add_beta(self, value):
        self.beta += value

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha

    def get_certainty_factor(self):
        return self.certainty_factor

    def set_certainty_factor(self, certain_factor):
        self.certain_factor = certain_factor
