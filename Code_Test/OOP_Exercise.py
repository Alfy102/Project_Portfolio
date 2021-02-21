class Vehicle:

    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
class Bus(Vehicle):
    pass

model=Bus('School Volvo',240,1800)
print('Vehicle Name: {} Speed: {} Milage: {}'.format(model.name, model.max_speed, model.milage))