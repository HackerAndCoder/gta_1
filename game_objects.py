import math, utils, pygame

class Car:
    def __init__(self, pos : utils.Pos):
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
    
    def accelerate(self, amount):
        self.speed = amount
    
    def stop(self):
        self.speed = 0

    def update(self):
        self.pos.x += math.cos(self.direction) * self.speed
        self.pos.y += math.sin(self.direction) * self.speed
    
    def get_render(self):
        surface = pygame.Surface()
        draw_pos = self.texture.get_rect().move(self.pos.x - self.texture.get_width() / 2, self.pos.y - self.texture.get_height() / 2)
        surface.blit(self.texture, draw_pos)
        return surface