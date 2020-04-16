from vehicle import Vehicle

class Jeep(Vehicle):

    def __init__(self, make, model, color, max_occupancy):
        super().__init__(make, model, color, max_occupancy)

    def drive(self):
        print(f"Lets jump in the {self.color} Jeep and go!!!")

    def turn(self, direction):
        print(f"The {self.make} turned {direction} onto 123 Street.")

    def stop(self):
        print(f"The {self.make} came to a sudden stop.")