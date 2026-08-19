import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



#Initializing the game elements
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0.0
player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
player.draw(screen)

#Helpers
def pygame_queue_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return


while True:
    log_state()
    pygame_queue_event()
    screen.fill("black")
    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
