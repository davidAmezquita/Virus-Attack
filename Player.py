import pygame, os


class Player:
    def __init__(self, x, y, width, height, health=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
        self.health = health
        self.direction = 1
        self.images = [pygame.image.load(os.path.join("assets", "Player.png")),
                       pygame.image.load(os.path.join("assets", "Player_left.png"))]
        self.laser = pygame.image.load(os.path.join("assets", "laser.png"))
        self.shoot_counter = 0

    def Draw(self, WIN):
        if self.direction == -1:
            WIN.blit(self.images[1], (self.x, self.y))
        else:
            WIN.blit(self.images[0], (self.x, self.y))

    # returns true if collision, false otherwise
    def checkCollision(self, objs, direction):

        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        for obj in objs:
            temp_rec = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            if player_rect.colliderect(temp_rec):
                if direction == "left":
                    self.x = obj.x + obj.width
                if direction == "right":
                    self.x = obj.x - obj.width
                if direction == "down":
                    self.y = obj.y - obj.height
                if direction == "up":
                    self.y = obj.y + obj.height
                return True

        return False
