import pygame
import random
import math

# initializes pygame
pygame.init()

# creates a screen
screen = pygame.display.set_mode((500, 500))

# draw a player
playerimg = pygame.image.load('player.png')
playerx = 230
playery = 430
playerx_change = 0
playery_change = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


# creating an enemies
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
enum = 5
for i in range(enum):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, 436))
    enemyy.append(random.randint(50, 100))
    enemyx_change.append(4)
    enemyy_change.append(40)

score = 0


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


# creating bullet
# ready:bullet is idle
# fire:bullet is moving
bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 430
bulletx_change = 0
bullety_change = 20
bullet_state = "ready"


def fireBullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


# detecting collision
def ifCollision(bulletx, bullety, enemyx, enemyy):
    distance = math.sqrt(pow(bulletx - enemyx, 2) + pow(bullety - enemyy, 2))
    # print(distance)
    if distance < 27:
        return True


# title and  icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# setting background image
backgroundImg = pygame.image.load('gamebg.png')

running = True
# gameloop
while running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # adding key movements to main player

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -6
            if event.key == pygame.K_RIGHT:
                playerx_change = 6
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletx = playerx
                    fireBullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    playerx += playerx_change

    # setting the boundaries for player
    if playerx <= 0:
        playerx = 0
    elif playerx > 436:
        playerx = 436

    # creating movements for enemy
    for i in range(enum):
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 4
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] > 436:
            enemyx_change[i] = -4
            enemyy[i] += enemyy_change[i]
        # collision and score update
        collision = ifCollision(bulletx, bullety, enemyx[i], enemyy[i])
        if collision:
            bullety = 430
            bullet_state = "ready"
            score += 1
            print(score)
            enemyx[i] = random.randint(0, 436)
            enemyy[i] = random.randint(50, 100)
        enemy(enemyx[i], enemyy[i], i)

    # bullet movement
    if bullety <= 0:
        bullety = 430
        bullet_state = "ready"
    if bullet_state == "fire":
        fireBullet(bulletx, bullety)
        bullety -= bullety_change

    player(playerx, playery)
    pygame.display.update()
