import os, pygame

def load_texture(path):
    return pygame.image.load(os.path.join('assets', path + '.png'))