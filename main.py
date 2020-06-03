import pygame
import os
import sys
import random
from Player import Player
from Enemy import Enemy
from Projectile import Projectile
from Wall import Wall
import mainMenu
from time import sleep

# displays main screen GUI
run = False
main_screen = mainMenu.StartScreen()
main_screen.start()
if main_screen.runGame:
    run = True


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (200, 50)
pygame.init()
WIDTH = 900
HEIGHT = 720
SIZE = WIDTH, HEIGHT
screen = pygame.display.set_mode(SIZE)
pointCounter = pygame.Rect(0, 0, WIDTH, 50)
result = None  # string used for printing end game results to GUI

#text font
font = pygame.font.SysFont("arial", 50)


def renderGame(player, walls, shots, enemies, numPoints):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), pointCounter)
    points = font.render("Points: " + str(numPoints), True, (255, 255, 255))

    screen.blit(points, (640, 0))
    for wall in walls:
        wall.Draw(screen)

    for bullets in shots:
        bullets.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    player.Draw(screen)
    pygame.display.flip()


def main():
    global run
    global result
    fps = 60
    clock = pygame.time.Clock()
    num_walls = 9
    num_enemies = 6
    num_points = 0

    # make player
    player = Player(300, 300, 64, 64)

    #make list of walls, enemies, bullets
    walls = []
    bullets = []
    enemies = []

    #set locations for walls
    wall_placement = [[150, 100], [150, 300], [150, 500],
                      [440, 100], [440, 300], [440, 500],
                      [700, 100], [700, 300], [700, 500]]

    #set locations for enemies
    enemy_placement = [[90, 100], [500, 100], [800, 100],
                       [100, 500], [400, 500], [700, 500]]

    #create walls
    for i in range(num_walls):
        wall = Wall(wall_placement[i][0], wall_placement[i][1], 64, 64)
        walls.append(wall)

    #create enemies
    for i in range(num_enemies):
        enemy = Enemy(enemy_placement[i][0], enemy_placement[i][1])
        enemies.append(enemy)

    #utilized for enemy movement throughout the game
    choices = ["up", "down", "left", "right"]
    length = 80    # time before enemy changes direction
    choice_timer = length  # timer to keep track of lenght passed
    while run:
        clock.tick(fps)

        # draw everything on screen
        renderGame(player, walls, bullets, enemies, num_points)

        if len(enemies) == 0:
            result = "You killed all the virus!"
            break

        #implements enemy artificial movement
        if choice_timer <= 0:
            choice_timer = length
        threshold = length - len(enemies)
        for enemy in enemies:
            #begins countdown till the enemy changes movement direction
            if choice_timer < threshold:
                choice_timer -= 1
            else:
                #decides a random direction for the enemy to move
                enemy.direction = random.choice(choices)
                choice_timer -= 1
            enemy.AI()

            #check wall collision
            enemy.objCollision(walls)

            #check enemy collision with another enemy
            enemy.objCollision(enemies, enemies.index(enemy))

            if enemy.playerCollision(player):
                #player collied with an enemy and lost
                run = False
                result = "You lost. Total points: " + str(num_points)

        # handel bullet movement through screen
        if player.shoot_counter < 5:
            for bullet in bullets:
                if not bullet.offScreen(WIDTH):
                    bullet.move()
                    # check for collision with wall
                    if bullet.Collision(walls) > 0:
                        bullets.pop(bullets.index(bullet))
                    # check collision with enemy
                    ret_val = bullet.Collision(enemies)
                    if ret_val == 1:
                        bullets.pop(bullets.index(bullet))
                        num_points += 1
                    elif ret_val == 2:
                        bullets.pop(bullets.index(bullet))
                else:
                    bullets.pop(bullets.index(bullet))
            player.shoot_counter += 1
        else:
            player.shoot_counter = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        keys = pygame.key.get_pressed()
        # handle player movement and check for collisions with walls
        if keys[pygame.K_a] and player.x - player.vel > 0:  # move left
            player.direction = -1
            player.x -= player.vel
            player.checkCollision(walls, "left")
        if keys[pygame.K_d] and (player.x + player.vel + 64) < WIDTH:  # move right
            player.direction = 1
            player.x += player.vel
            player.checkCollision(walls, "right")
        if keys[pygame.K_w] and player.y - player.vel > 50:  # move up (50 to account for the point counter rect
            player.y -= player.vel
            player.checkCollision(walls, "up")
        if keys[pygame.K_s] and ((player.y + player.vel + 64) < HEIGHT):  # move down
            player.y += player.vel
            player.checkCollision(walls, "down")

        # handle player shooting
        if keys[pygame.K_SPACE] and player.shoot_counter == 0:
            if player.direction == -1:
                bullets.append(Projectile(player.x - 32, player.y, player.direction))
            else:
                bullets.append(Projectile(player.x + 64, player.y, player.direction))


if __name__ == "__main__":
    main()

end_screen = mainMenu.EndScreen(result)
end_screen.start()
