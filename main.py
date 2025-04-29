# imports
import pygame
from constants import *
from player import Player



# Base class for game objects

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    game_clock = pygame.time.Clock()
    dt = 0

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
               
        updatable.update(dt)                 # player1.update(dt)
        screen.fill(color="black")
        for pl in drawable:
            pl.draw(screen)                    #player1.draw(screen)
        pygame.display.flip()
    
        dt = game_clock.tick(60)/1000


if __name__ == "__main__":
    main()