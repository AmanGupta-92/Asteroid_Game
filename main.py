import pygame
from constants import *
from player import * 
from asteroidfield import *
from asteroid import *
import sys
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.checkCollision(player):
                sys.exit("Game Over!")

            for bullet in shots:
                if bullet.checkCollision(asteroid):
                    bullet.kill()
                    asteroid.split()

        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)
        # player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__== "__main__":
    main()