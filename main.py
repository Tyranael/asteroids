import pygame
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

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
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = shots, updatable, drawable


player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
asteroid_field_obj = AsteroidField()

#Helpers
def pygame_queue_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
        
def game_over_check():
    for ast in asteroids:
        if ast.collides_with(player):
            log_event("player_hit")
            print("Game over!")
            sys.exit(1)
            
def asteroid_state_check():
    for ast in asteroids:
        for shot in shots:
            if shot.collides_with(ast):
                log_event("asteroid_shot")
                shot.kill()
                ast.split()
                break    

while True:
    log_state()
    pygame_queue_event()

    # Updating state and position
    updatable.update(dt)

    # Checking collisions after movement
    game_over_check()
    asteroid_state_check()

    # Drawing elements onto the screen
    screen.fill("black")
    for element in drawable:
        element.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
