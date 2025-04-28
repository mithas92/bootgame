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

    game_clock = pygame.time.Clock()
    dt = 0

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        
        player1.update(dt)
        screen.fill(color="black")
        player1.draw(screen)
        pygame.display.flip()
    
        dt = game_clock.tick(60)/1000


if __name__ == "__main__":
    main()