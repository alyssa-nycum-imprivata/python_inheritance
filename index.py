from vehicle import Vehicle
from honda import Honda
from jeep import Jeep
from tesla import Tesla
from toyota import Toyota
from volkswagon import Volkswagon

# Create an instance of each vehicle.

honda = Honda("Honda", "Civic", "burgandy", 5)
jeep = Jeep("Jeep", "Wrangler", "green", 5)
tesla = Tesla("Tesla", "X", "silver", 5)
toyota = Toyota("Toyota", "Corolla", "blue", 5)
volkswagon = Volkswagon("Volkswagon", "Jetta", "red", 5)

# Make your vehicle instances perform all three behaviors.

honda.drive()
honda.turn("right")
honda.stop()

tesla.drive()
tesla.turn("left")
tesla.stop()

toyota.drive()
toyota.turn("right")
toyota.stop()

jeep.drive()
jeep.turn("left")
jeep.stop()

volkswagon.drive()
volkswagon.turn("right")
volkswagon.stop()
