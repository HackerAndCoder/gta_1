import math, utils, pygame

class GameObjects:
    car = 'car'
    player = 'player'
    blank = 'blank'
    npc = 'npc'

class GameObject:
    def __init__(self, type = GameObjects.blank):
        self.type = type

class Car(GameObject):
    def __init__(self, pos : utils.Pos):
        super().__init__(GameObjects.car)

        self.pos = pos
        self.direction = 0 # in radians!
        self.torque = 1 # the acceleration and deacceleration force
        self.turn_speed = 4 # how fast the car turns
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
    
    def _turn(self, degrees):
        self.direction += math.radians(degrees) * (self.speed / self.max_speed)
    
    def turn_left(self):
        self._turn(-self.turn_speed)
    
    def turn_right(self):
        self._turn(self.turn_speed)
    
    def _accelerate(self, amount):
        self.target_speed += amount
        if self.target_speed > self.max_speed:
            self.target_speed -= 1
    
    def stop(self):
        self.speed = 0
    
    def accelerate(self):
        self._accelerate(self.torque)
    
    def deaccelerate(self):
        self._accelerate(-self.torque)

    def update(self):
        self.pos.x += math.cos(self.direction) * self.speed
        self.pos.y += math.sin(self.direction) * self.speed
        if self.target_speed > self.resistance and self.target_speed > 0    :
            self.target_speed -= self.resistance
        elif self.target_speed > self.resistance and self.target_speed > 0:
            self.target_speed = 0
        
        elif self.target_speed < 0 and (self.target_speed + self.resistance < 0):
            self.target_speed += self.resistance
        
        if self.target_speed > self.speed:
            self.speed += self.power
        elif self.target_speed < self.speed:
            self.speed -= self.power
    
    def get_render(self):
        surface = pygame.Surface(self.texture.get_size(), pygame.SRCALPHA)
        surface.set_colorkey((0, 0, 0))

        img = utils.rotate_img(self.texture, self.texture.get_rect(), -self.get_direction()-90)[0]
        rotated_img_center = img.get_rect().center
        surface_center = self.texture.get_rect().center
        surface.blit(img, utils.sub_vectors(surface_center, rotated_img_center))

        return surface
    
class Humanoid(GameObject):
    def __init__(self, pos : utils.Pos, type = GameObjects.npc, walking_texture = None, standing_texture = None, inventory = [], direction = 0, walk_speed = 5):
        super().__init__(type)
        self.walking_texture = walking_texture
        self.standing_texture = standing_texture
        self.inventory = inventory
        self.pos = pos
        self.direction = direction # in radians!
        self.walk_speed = walk_speed
        self.speed = 0
        self.turn_speed = 1
    
    def _turn(self, amount):
        self.direction += math.radians(amount)
    
    def turn_left(self):
        self._turn(-self.turn_speed)
    
    def turn_right(self):
        self._turn(self.turn_speed)
    
    def walk(self):
        self.speed = self.walk_speed
    
    def run(self):
        self.speed = self.walk_speed * 1.5
    
    def update(self):
        self.pos.x += math.cos(self.direction) * self.speed
        self.pos.y += math.sin(self.direction) * self.speed
    
    def get_render(self):
        surface = pygame.Surface(self.texture.get_size(), pygame.SRCALPHA)
        surface.set_colorkey((0, 0, 0))

        img = utils.rotate_img(self.texture, self.texture.get_rect(), -self.get_direction()-90)[0]
        rotated_img_center = img.get_rect().center
        surface_center = self.texture.get_rect().center
        surface.blit(img, utils.sub_vectors(surface_center, rotated_img_center))

        return surface