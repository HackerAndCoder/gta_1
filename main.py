import pygame, game_objects, utils

pygame.init()

# variables

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('GTA')

game_clock = pygame.time.Clock()

camera_pos = utils.Pos()

# game objects initialization

objects = [game_objects.Car(utils.Pos(10, 10))]

def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def handle_movement():
    # temporary testing code
    if pygame.key.get_pressed()[pygame.K_w]:
        objects[0].accelerate(2)

while True:
    game_clock.tick(30)
    window.fill((255, 255, 255))

    for object in objects:
        object.update()
        window.blit(object.get_render(), utils.add_vectors(object.pos.get_pos(), camera_pos.get_pos()))
    
    pygame.display.flip()
    
    handle_events(pygame.event.get())
    handle_movement()