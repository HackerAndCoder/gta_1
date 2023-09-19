import os, pygame

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def load_texture(path):
    return pygame.image.load(os.path.join('assets', path + '.png'))

def add_vectors(vec1, vec2):
    vec3 = []
    for i in range(len(vec1)):
        vec3.append(int(vec1[i]) + int(vec2[i]))
    return vec3