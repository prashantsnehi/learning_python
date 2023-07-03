class Piglet:
    sound= ''
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Hi {}! I'm object of Piglet class".format(self.name)

    def speak(self):
        return "{}! Hi {}. I generate {} sound".format(self.sound, self.name, self.sound)



