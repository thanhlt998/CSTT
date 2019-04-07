from helper import triangle_calculate_membership


class Height:
    MALE = 'Male'
    FEMALE = 'Female'

    def list(self):
        pass

    def fuzzy_extremely_short(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 140
            top = 140
            right = 155
        else:
            left = 140
            top = 140
            right = 155

        if human.height <= left:
            dom = 1
        elif left < human.height < right:
            dom = 1 - (top - human.height)/(top - right)

        return dom

    def fuzzy_short(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 140
            top = 155
            right = 170
        else:
            left = 140
            top = 155
            right = 170

        if left < human.height < right:
            dom = triangle_calculate_membership(left, top, right, human.height)

        return dom

    def fuzzy_average(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 155
            top = 170
            right = 185
        else:
            left = 155
            top = 170
            right = 185

        if left < human.height < right:
            dom = triangle_calculate_membership(left, top, right, human.height)

        return dom

    def fuzzy_tall(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 170
            top = 185
            right = 200
        else:
            left = 170
            top = 185
            right = 200

        if left < human.height < right:
            dom = triangle_calculate_membership(left, top, right, human.height)

        return dom

    def fuzzy_extremely_tall(self, human):
        dom = 0
        if human.sex == self.MALE:
            left = 185
            top = 200
            right = 200
        else:
            left = 185
            top = 200
            right = 200

        if human.height >= right:
            dom = 1
        elif left < human.height < right:
            dom = 1 - (top - human.height)/(top - left)

        return dom
