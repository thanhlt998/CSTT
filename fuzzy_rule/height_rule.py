from helper import triangle_calculate_membership


class Height:
    MALE = 'Male'
    FEMALE = 'Female'

    def list(self):
        pass

    def fuzzy_extremely_short(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 155
            top = 155
            right = 165
        else:
            left = 145
            top = 145
            right = 157.5

        if human.height <= left:
            dom = 1
        elif left < human.height < right:
            dom = 1 - (top - human.height)/(top - right)

        return dom

    def fuzzy_short(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 155
            top = 165
            right = 175
        else:
            left = 145
            top = 157.5
            right = 170

        if left < human.height < right:
            dom = triangle_calculate_membership(left, top, right, human.height)

        return dom

    def fuzzy_average(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 165
            top = 175
            right = 185
        else:
            left = 157.5
            top = 170
            right = 182.5

        if left < human.height < right:
            dom = triangle_calculate_membership(left, top, right, human.height)

        return dom

    def fuzzy_tall(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 175
            top = 185
            right = 195
        else:
            left = 170
            top = 182.5
            right = 195

        if left < human.height < right:
            dom = triangle_calculate_membership(left, top, right, human.height)

        return dom

    def fuzzy_extremely_tall(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 185
            top = 195
            right = 195
        else:
            left = 182.5
            top = 195
            right = 195

        if human.height >= right:
            dom = 1
        elif left < human.height < right:
            dom = 1 - (top - human.height)/(top - left)

        return dom
