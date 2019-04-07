from helper import triangle_calculate_membership


class Weight:
    MALE = 'Male'
    FEMALE = 'Female'

    def list_rule(self):
        pass

    def fuzzy_light(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 50
            top = 50
            right = 70
        else:
            left = 60
            top = 60
            right = 75

        if human.weight <= left:
            dom = 1
        elif left < human.weight < right:
            dom = 1 - (top - human.weight) / (top - right)

        return dom

    def fuzzy_medium(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 50
            top = 70
            right = 90
        else:
            left = 60
            top = 75
            right = 90

        if left < human.weight < right:
            dom = triangle_calculate_membership(left, top, right, human.weight)

        return dom

    def fuzzy_heavy_1(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 70
            top = 90
            right = 110
        else:
            left = 75
            top = 90
            right = 105

        if left < human.weight < right:
            dom = triangle_calculate_membership(left, top, right, human.weight)

        return dom

    def fuzzy_heavy_2(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 90
            top = 105
            right = 120
        else:
            left = 90
            top = 105
            right = 120

        if left < human.weight < right:
            dom = triangle_calculate_membership(left, top, right, human.weight)

        return dom

    def fuzzy_heavy_3(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 110
            top = 130
            right = 150
        else:
            left = 105
            top = 120
            right = 135

        if left < human.weight < right:
            dom = triangle_calculate_membership(left, top, right, human.weight)

        return dom

    def fuzzy_heavy_4(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 130
            top = 150
            right = 150
        else:
            left = 120
            top = 135
            right = 135

        if human.weight >= right:
            dom = 1
        elif left < human.weight < right:
            dom = 1 - (top - human.weight) / (top - left)
        return dom
