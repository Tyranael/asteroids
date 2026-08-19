from circleshape import CircleShape
from constants import SHOTS_RADIUS, LINE_WIDTH
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOTS_RADIUS)
        
    def draw(self, screen_obj):
        pygame.draw.circle(screen_obj, "red", self.position, self.radius, width=LINE_WIDTH)

    def update(self, delta):
        self.position += self.velocity*delta