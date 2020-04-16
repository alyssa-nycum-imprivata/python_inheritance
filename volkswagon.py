from vehicle import Vehicle

class Volkswagon(Vehicle):

    def __init__(self, make, model, color, max_occupancy):
        super().__init__(make, model, color, max_occupancy)

    def drive(self):
        print(f"Lets jump in the {self.color} Volkswagon and go!!!")

    def turn(self, direction):
        print(f"The {self.make} turned {direction} after the big farm house.")

    def stop(self):
        print(f"The {self.make} came to a halting stop because they crashed.")