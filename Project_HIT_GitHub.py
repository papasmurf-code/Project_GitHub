class Vehicle:
    enging_capacity = "1, 6 Turbo" #attribute
    numWheels = 0
    tankType = 0
    seatingCapacity = 0
    maxVelocity = 0
    def __init__(self,numWheels, tanktype,seatingCapacity,maxVelocity):
        self.numWheels = numWheels
        self.tankType = tanktype
        self.seatingCapacity = seatingCapacity
        self.maxVelocity = maxVelocity

    def drive(self):
        print ("The vehicle is in driving mode")

    def stop (self):
        print ("The vehicle is in stop mode")


toyota = Vehicle (4, "petrol",5,150)
print(toyota.numWheels)
print(toyota.tankType)
print(toyota.seatingCapacity)
print(toyota.maxVelocity)
toyota.drive()
toyota.stop()

class ElectricCar(Vehicle):
    def __init__(self, numWheels, seatingCapacity,maxVelocity):
        Vehicle.__init__(self,numWheels,'electric',seatingCapacity,maxVelocity)

blueSG = ElectricCar(4,5,150)
blueSG.drive()
blueSG.stop()