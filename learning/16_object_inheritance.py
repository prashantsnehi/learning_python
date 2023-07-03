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

"""Animal Class"""


class Animal:
    sound = ""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        print("This is Animal Class")

    def speak(self):
        print("{sound} I'm {name}! {sound}".format(sound=self.sound, name=self.name))


"""Piglet class inherited from Animal Class"""


class Piglet(Animal):
    sound = "Oink!"


"""Cow class inherited from Animal class"""


class Cow(Animal):
    sound = "Moooooo!"


"""Creating object of Piglet class"""
hamlet = Piglet("Hamlet")
hamlet.speak()


"""Creating object of Cow class"""
milky = Cow("Milky-White")
milky.speak()
