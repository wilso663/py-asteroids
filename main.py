import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()

    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()



    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid_thing in asteroids:
            if asteroid_thing.is_colliding(player):
                print("Game over!")
                return
            for shot_thing in shots:
                if shot_thing.is_colliding(asteroid_thing):
                    asteroid_thing.split()
                    shot_thing.kill()

        screen.fill((0,0,0))

        for draw_thing in drawable:
            draw_thing.draw(screen)
 
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        #dt = clock.get_time() / 1000



if __name__ == "__main__":
    main()
