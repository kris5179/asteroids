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

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        log_state()

        # w ten sposób można zamykać grę przez X w oknie, a nie w terminalu 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        #odświeżenie ekranu
        pygame.display.flip()

        # ograniczenie do 60fps, dodatkowo .tick() zwraca czas od ostatniego wywołania (w milisekundach)
        dt = clock.tick(60) / 1000
#        print(f"{dt}")

if __name__ == "__main__":
    main()

