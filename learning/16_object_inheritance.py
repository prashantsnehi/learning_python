class Fruit:
    """Constructor"""

    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    """return class name on printing the object of the class"""

    def __str__(self):
        print("This is Fruit Class")


"""Fruit class inheritance to Apple class"""


class Apple(Fruit):
    pass


class Grapes(Fruit):
    pass


granny_smith = Apple('green', 'tart')
carnelian = Grapes('purple', 'sweet')

print("Grenny Smith apples are {} and {}".format(granny_smith.color, granny_smith.flavor))
print("Carnelian grapes are {} and {}".format(carnelian.color, carnelian.flavor))
