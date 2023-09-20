import pygame, game_objects, utils

pygame.init()

# variables

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('GTA')

game_clock = pygame.time.Clock()

targeted_object = 0

camera_pos = utils.Pos()

# game objects initialization

objects = [game_objects.Car(utils.Pos(100, 100))]

def is_pressed(key):
    return pygame.key.get_pressed()[key]

def get_targeted_object():
    try:
        return objects[targeted_object]
    except:
        return None

def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def handle_movement():
    # temporary testing code
    if get_targeted_object().type == game_objects.GameObjects.car:
        if is_pressed(pygame.K_w):
            objects[0].accelerate()
        if is_pressed(pygame.K_a):
            objects[0].turn_left()
        if is_pressed(pygame.K_d):
            objects[0].turn_right()
        if is_pressed(pygame.K_s):
            objects[0].deaccelerate()

while True:
    game_clock.tick(30)
    window.fill((200, 200, 200))

    for object in objects:
        object.update()
        window.blit(object.get_render(), utils.add_vectors(object.pos.get_pos(), camera_pos.get_pos()))
    
    pygame.display.flip()
    
    handle_events(pygame.event.get())
    handle_movement()