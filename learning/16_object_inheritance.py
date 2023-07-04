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

"""Let's expand a bit on our clothing class. Finish the 'Stock_by_Material' method and iterate over the amount of each item of a given material that is in stock. When you are finidshed 
the script should add up to 10 cotton clothing items"""


class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def stock_by_material(self, material):
        """
        :param material:
        :return:
        """
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class Shirt(Clothing):
    material = "Cotton"


class Pants(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
sweatpants = Pants("Sweatpants")

polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)

current_stock = polo.stock_by_material("Cotton")
print(current_stock)
