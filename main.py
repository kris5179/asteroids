import pygame
import time
from constants import SCREEN_HEIGHT      
from constants import SCREEN_WIDTH      
from logger import log_state

def main():
    pygame.init()
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    i = 0
#   while True:
#       log_state()
#       for event in pygame.event.get():
#           if event.type == pygame.QUIT:
#               return
#       screen.fill("black")
#       pygame.display.flip()


    i = 0
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        colors = ["red", "green", "yellow", "blue", "pink", "white"]
        screen.fill(colors[i])
        i += 1 
        i = i % len(colors)
        pygame.display.flip()
        time.sleep(1)

if __name__ == "__main__":
    main()

