class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("Driving on the road")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")


# Objects
v1 = Car()
v2 = Bicycle()

# Polymorphism
v1.move()
v2.move()