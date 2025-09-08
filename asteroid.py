from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

  def update(self, dt):
    self.position += (self.velocity * dt)

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    spawn_angle = random.uniform(20,50)
    asteroid1_angle = pygame.math.Vector2.rotate(self.velocity, spawn_angle)
    asteroid2_angle = pygame.math.Vector2.rotate(self.velocity, -spawn_angle)
    asteroids_radii = self.radius - ASTEROID_MIN_RADIUS
    asteroid1 = Asteroid(self.position.x, self.position.y, asteroids_radii)
    asteroid2 = Asteroid(self.position.x, self.position.y, asteroids_radii)
    asteroid1.velocity = asteroid1_angle * 1.2
    asteroid2.velocity = asteroid2_angle * 1.2
    