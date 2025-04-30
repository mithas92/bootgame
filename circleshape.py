import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        # Measure distance
        #the_distance = self.position.distance_to(other.position)
        #touch_dist = (self.radius + other.radius)/2
        # return the_distance <= touch_dist
        return self.position.distance_to(other.position) <= (self.radius + other.radius)/2
        