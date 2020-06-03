import pygame, os

WIDTH = 900
HEIGHT = 720


class Enemy:
    def __init__(self, x, y, width=64, height=64):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = 300
        self.images = [pygame.image.load(os.path.join("assets", "Virus.png")),
                       pygame.image.load(os.path.join("assets", "virus_damaged.png"))]
        self.isDamaged = 0
        self.damage = 100
        self.vel = 3
        self.direction = None

    def AI(self):

        if (self.x + self.width + self.vel) < WIDTH and self.direction == "right":
            self.x += self.vel
        if (self.x - self.vel > 0) and self.direction == "left":
            self.x -= self.vel
        if (self.y + self.height + self.vel) < HEIGHT and self.direction == "down":
            self.y += self.vel
        if (self.y - self.vel) > 50 and self.direction == "up":
            self.y -= self.vel

    def draw(self, window):
        window.blit(self.images[self.isDamaged], (self.x, self.y))
        self.isDamaged = 0

    def onHit(self, damage):
        self.health -= damage
        self.isDamaged = 1

    def playerCollision(self, player):
        this_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        player_rect = pygame.Rect(player.x, player.y, player.width, player.height)

        if this_rect.colliderect(player_rect):
            return True

        return False

    def objCollision(self, objs, index=-1):
        this_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        for i in range(len(objs)):
            if i == index:
                continue

            temp = pygame.Rect(objs[i].x, objs[i].y, objs[i].width, objs[i].height)
            if this_rect.colliderect(temp):
                if self.direction == "left":
                    self.x = objs[i].x + objs[i].width
                if self.direction == "right":
                    self.x = objs[i].x - objs[i].width
                if self.direction == "down":
                    self.y = objs[i].y - objs[i].height
                if self.direction == "up":
                    self.y = objs[i].y + objs[i].height
                return True

        return False
