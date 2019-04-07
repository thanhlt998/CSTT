from helper import triangle_calculate_membership


class Weight:
    MALE = 'Male'
    FEMALE = 'Female'

    def list_rule(self):
        pass

    def fuzzy_light(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 55
            top = 55
            right = 75
        else:
            left = 50
            top = 50
            right = 70

        if human.weight <= left:
            dom = 1
        elif left < human.weight < right:
            dom = 1 - (top - human.weight) / (top - right)

        return dom

    def fuzzy_medium(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 55
            top = 75
            right = 95
        else:
            left = 50
            top = 70
            right = 90

        if left < human.weight < right:
            dom = triangle_calculate_membership(left, top, right, human.weight)

        return dom

    def fuzzy_heavy_1(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 75
            top = 95
            right = 115
        else:
            left = 70
            top = 90
            right = 110

        if left < human.weight < right:
            dom = triangle_calculate_membership(left, top, right, human.weight)

        return dom

    def fuzzy_heavy_2(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 95
            top = 115
            right = 135
        else:
            left = 90
            top = 110
            right = 130

        if left < human.weight < right:
            dom = triangle_calculate_membership(left, top, right, human.weight)

        return dom

    def fuzzy_heavy_3(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 115
            top = 135
            right = 155
        else:
            left = 110
            top = 130
            right = 150

        if left < human.weight < right:
            dom = triangle_calculate_membership(left, top, right, human.weight)

        return dom

    def fuzzy_heavy_4(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 135
            top = 155
            right = 155
        else:
            left = 130
            top = 150
            right = 150

        if human.weight >= right:
            dom = 1
        elif left < human.weight < right:
            dom = 1 - (top - human.weight) / (top - left)
        return dom
