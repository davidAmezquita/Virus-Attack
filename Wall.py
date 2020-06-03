import pygame, os


class Wall:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = 400
        self.images = [pygame.image.load(os.path.join("assets", "wall.png")),
                       pygame.image.load(os.path.join("assets", "wall_destroyed1.png")),
                       pygame.image.load(os.path.join("assets", "wall_destroyed2.png")),
                       pygame.image.load(os.path.join("assets", "wall_destroyed3.png"))]

    def Draw(self, WIN):
        i = 0
        if self.health < 300:
            i = 1
        if self.health < 200:
            i = 2
        if self.health < 100:
            i = 3

        WIN.blit(self.images[i], (self.x, self.y))

    def onHit(self, damage):
        self.health -= damage
