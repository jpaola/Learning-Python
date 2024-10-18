class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter / 2

    def circumference(self):
        circumference = 2 * self.pi * self.radius
        return circumference


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print('''
medium_pizza = {}
teaching_table = {}
round_room = {}
'''.format(medium_pizza.circumference(), teaching_table.circumference(), round_room.circumference()))
