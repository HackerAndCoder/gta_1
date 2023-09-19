import pygame, game_objects, utils

pygame.init()

# variables

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('GTA')

game_clock = pygame.time.Clock()

# game objects initialization

objects = [game_objects.Car(utils.Pos(10, 10))]

def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

while True:
    game_clock.tick(30)
    
    for object in objects:
        object.update()
        

    window.fill((255, 255, 255))
    pygame.display.flip()
    
    handle_events(pygame.event.get())