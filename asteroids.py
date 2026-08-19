from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    #Drawing the asteroid
    def draw(self, screen_obj):
        pygame.draw.circle(screen_obj, "white", self.position, self.radius, width=LINE_WIDTH)
    
    #Updating state and position
    def update(self, delta):
        self.position += self.velocity*delta

    def split(self):
            self.kill()

            if self.radius <= ASTEROID_MIN_RADIUS:
                return

            log_event("asteroid_split")

            angle = random.uniform(20, 50)

            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = velocity1 * 1.2
            asteroid2.velocity = velocity2 * 1.2