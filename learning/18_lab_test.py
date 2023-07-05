class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category


class Turtle(Animal):
    category = "reptile"


print(Turtle.category)


class Snake(Animal):
    category = 'reptile'


class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_if_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            print(animal)
            if animal == category:
                result = + 1
        return result


zoo = Zoo()

turtle = Turtle('Turtle')
snake = Snake('Snake')

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_if_category('reptile'))
