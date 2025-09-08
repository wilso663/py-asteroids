import pygame
from constants import *
from player import Player
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill((0,0,0))

        for draw_thing in drawable:
            draw_thing.draw(screen)
 
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        #dt = clock.get_time() / 1000



if __name__ == "__main__":
    main()
