import os, pygame

class Pos:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def get_pos(self):
        return (self.x, self.y)

def load_texture(path):
    return pygame.image.load(os.path.join('assets', path + '.png')).convert_alpha()

def add_vectors(vec1, vec2):
    vec3 = []
    for i in range(len(vec1)):
        vec3.append(int(vec1[i]) + int(vec2[i]))
    return vec3

def sub_vectors(vec1, vec2):
    vec3 = []
    for i in range(len(vec1)):
        vec3.append(int(vec1[i]) - int(vec2[i]))
    return vec3

def rot_center(image, angle, pos):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = pos.get_pos()).center)
    return rotated_image, new_rect

def rotate(image, rect, angle):
    """Rotate the image while keeping its center."""
    # Rotate the original image without modifying it.
    new_image = pygame.transform.rotate(image, angle)
    # Get a new rect with the center of the old rect.
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect