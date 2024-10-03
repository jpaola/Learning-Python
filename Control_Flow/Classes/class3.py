class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        print(f"New circle with diameter: {self.diameter}")


# Create a circle teaching_table with diameter 36
teaching_table = Circle(36)
