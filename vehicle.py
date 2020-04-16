class Vehicle:

    def __init__(self, make, model, color, max_occupancy):
        self.make = make
        self.model = model
        self.color = color
        self.max_occupancy = max_occupancy

    def drive(self):
        print("Let's go!")

    def turn(self, direction):
        print(f"The {self.make} turned {direction} at the stop sign.")

    def stop(self):
        print(f"The {self.make} came slowly to a stop.")