import math, utils, pygame

class Car:
    def __init__(self, pos : utils.Pos):
        self.pos = pos
        self.direction = 0 # in radians!
        self.speed = 0
        self.target_speed = 0 
        self.power = 0.2 # how fast the car speeds up 
        self.max_speed = 10 # the cars max speed
        self.resistance = 0.8 # how fast the car slowes down
        self.texture = utils.load_texture('default_car')
    
    def set_direction(self, angle):
        self.direction = math.radians(angle)
    
    def get_direction(self):
        return math.degrees(self.direction)
    
    def turn(self, degrees):
        self.direction += math.radians(degrees)
    
    def accelerate(self, amount):
        self.target_speed += amount
        if self.target_speed > self.max_speed:
            self.target_speed -= 1
    
    def stop(self):
        self.speed = 0

    def update(self):
        self.pos.x += math.cos(self.direction) * self.speed
        self.pos.y += math.sin(self.direction) * self.speed
        if self.target_speed > self.resistance:
            self.target_speed -= self.resistance
        elif self.target_speed > self.resistance and self.target_speed > 0:
            self.target_speed = 0
        
        if self.target_speed > self.speed:
            self.speed += self.power
        elif self.target_speed < self.speed:
            self.speed -= self.power
    
    def get_render(self):
        surface = pygame.Surface(self.texture.get_size(), pygame.SRCALPHA)
        surface.set_colorkey((0, 0, 0))
        img = utils.rotate(self.texture, self.texture.get_rect(), self.get_direction())[0]
        surface.blit(img, utils.add_vectors(self.texture.get_size(), img.get_rect()))
        return surface