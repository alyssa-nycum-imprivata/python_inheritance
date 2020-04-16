from vehicle import Vehicle

class Toyota(Vehicle):

    def __init__(self, make, model, color, max_occupancy):
        super().__init__(make, model, color, max_occupancy)

    def drive(self):
        print(f"Lets jump in the {self.color} Toyota and go!!!")