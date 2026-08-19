from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    #Drawing the asteroid
    def draw(self):
        pygame.draw.circle(screen_obj, "white", self.position, self.radius, width=LINE_WIDTH)
    
    #Updating state and position
    def update(self, delta):
        self.position += self.velocity*delta