import pygame, os


class Projectile:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.image = pygame.image.load(os.path.join("assets", "laser.png"))
        self.vel = 7
        self.direction = direction
        self.damage = 100

    def move(self):
        self.x += (self.vel * self.direction)

    def offScreen(self, width):
        if self.x <= 0 or self.x >= width:
            return True
        else:
            return False

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def Collision(self, objs):
        bullet_rect = pygame.Rect(self.x, self.y, 20, 20)

        # check collisions with obj using rectangles
        # objs must be a list of either walls or enemies
        for obj in objs:
            temp_rec = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            if bullet_rect.colliderect(temp_rec):
                if obj.health == 0:
                    objs.pop(objs.index(obj))
                    return 1
                else:
                    obj.onHit(self.damage)
                    return 2
        return 0
