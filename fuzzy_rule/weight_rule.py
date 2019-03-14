from helper import triangle_calculate_membership


class Weight:
    MALE = 'm'
    FEMALE = 'f'

    def list_rule(self):
        pass

    def fuzzy_light(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 60
            top = 60
            right = 70
        else:
            left = 44
            top = 44
            right = 50

        if human.weight <= left:
            dom = 1
        elif left < human.weight < right:
            dom = 1 - (top - human.weight) / (top - right)

        return dom

    def fuzzy_medium(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 60
            top = 70
            right = 80
        else:
            left = 44
            top = 50
            right = 56

        if left < human.weight < right:
            dom = triangle_calculate_membership(left, top, right, human.weight)

        return dom

    def fuzzy_heavy(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 70
            top = 80
            right = 80
        else:
            left = 50
            top = 56
            right = 56

        if human.weight >= right:
            dom = 1
        elif left < human.weight < right:
            dom = 1 - (top - human.weight) / (top - left)
        return dom
