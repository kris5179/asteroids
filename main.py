import pygame
import time
from constants import SCREEN_HEIGHT      
from constants import SCREEN_WIDTH      
from logger import log_state
from player import Player

def main():
    pygame.init()
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        log_state()

        # w ten sposób można zamykać grę przez X w oknie, a nie w terminalu 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)
        for item in drawable:
            item.draw(screen)


        # odświeżenie ekranu
        # ograniczenie do 60fps, dodatkowo .tick() zwraca czas od ostatniego wywołania (w milisekundach)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

