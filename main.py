import pygame
from constants import *
from player import *

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Frame limiting
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(x, y)

    # Game Loop
    while True:

        # Handles window close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        dt = (clock.tick(60) / 1000)
        updatable.update(dt)

        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)
            

        pygame.display.flip()



if __name__ == "__main__":
    main()
