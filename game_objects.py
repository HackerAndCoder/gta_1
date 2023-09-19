import math, utils

class Car:
    def __init__(self, pos):
        self.pos = pos
        self.direction = 0 # in radians!
        self.speed = 0
        self.texture = utils.load_texture('default_car')
    
    def set_direction(self, angle):
        self.direction = math.radians(angle)
    
    def get_direction(self):
        return math.degrees(self.direction)
    
    def turn(self, degrees):
        self.direction += math.radians(degrees)