from helper import triangle_calculate_membership


class Height:
    MALE = 'm'
    FEMALE = 'f'

    def list(self):
        pass

    def fuzzy_short(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 160
            top = 160
            right = 170
        else:
            left = 152
            top = 152
            right = 160

        if human.height <= left:
            dom = 1
        elif left < human.height < right:
            dom = 1 - (top - human.height)/(top - right)

        return dom

    def fuzzy_average(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 160
            top = 170
            right = 180
        else:
            left = 152
            top = 160
            right = 168

        if left < human.height < right:
            dom = triangle_calculate_membership(left, top, right, human.height)

        return dom

    def fuzzy_tall(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 170
            top = 180
            right = 180
        else:
            left = 160
            top = 168
            right = 168

        if human.height >= right:
            dom = 1
        elif left < human.height < right:
            dom = 1 - (top - human.height)/(top - left)

        return dom
