class Elevator:
    def __init__(self, bottom, top, current):
        """initialize the elevator instance"""
        self.bottom = bottom
        self.top = top
        self.current = current

    def __str__(self):
        """information about current floor"""
        return "Current floor is {}".format(self.current)

    def up(self):
        """makes the elevator to go up one floor"""
        if self.current < 10:
            self.current += 1

    def down(self):
        """makes the elevator to go down one floor"""
        if self.current > 0:
            self.current -= 1

    def go_to(self, floor):
        """makes the elevator go to the specific floor."""
        """if floor >= self.bottom and floor <= self.top:"""
        if self.bottom <= floor <= self.top:
            self.current = floor
        elif floor < 0:
            self.current = 0
        else:
            self.current = 10


elevator = Elevator(-1, 10, 0)

elevator.up()
elevator.current  # should output 1

elevator.down()
elevator.current  # should output 0

elevator.go_to(10)
elevator.current  # should output 10
