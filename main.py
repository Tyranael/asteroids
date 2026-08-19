import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



#Initializing the game elements
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0.0

#Initializing pygame groups and elements
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
asteroid_field = pygame.sprite.Group()

Player.containers = (updatable, drawable)
player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
asteroid_field_obj = AsteroidField()

#Helpers
def pygame_queue_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return


while True:
    log_state()
    pygame_queue_event()
    
    #Drawing elements into the screen
    screen.fill("black")
    for element in drawable:
        element.draw(screen)
    
    #Updating data and position
    pygame.display.flip()
    updatable.update(dt)
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
