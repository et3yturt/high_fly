import time

import pygame
import random

from pygame import RLEACCEL
from pygame.locals import(RLEACCEL,K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT,K_r)

pygame.init()



SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

live = 100
score = 0


class Spacecraft(pygame.sprite.Sprite):
    def __init__(self):
        super(Spacecraft, self).__init__()
        self.surf = pygame.image.load("spacecraft.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
            random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
            random.randint(0, SCREEN_HEIGHT),
        )
    )
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)

class fog(pygame.sprite.Sprite):
    def __init__(self):
        super(fog, self).__init__()
        self.surf = pygame.image.load("fog.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
            random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
            random.randint(0, SCREEN_HEIGHT),
        )
    )
        self.speed = 3

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("Image20251219175548.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0,SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5,20)



    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0,350)
            )
        )
        self.speed = random.randint(4,10)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Health(pygame.sprite.Sprite):
    def __init__(self):
        super(Health, self).__init__()
        self.surf = pygame.image.load("health.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
            random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
            random.randint(0, SCREEN_HEIGHT),
        )
    )
        self.speed = 4

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()
        self.surf = pygame.image.load("coin.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                 random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = 4

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 300)

ADDCRAFT = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCRAFT, 3000)

ADDFOG = pygame.USEREVENT + 3
pygame.time.set_timer(ADDFOG, 100000)

ADDHEALTH = pygame.USEREVENT + 4
pygame.time.set_timer(ADDHEALTH, 6000)

ADDCLOUD = pygame.USEREVENT + 5
pygame.time.set_timer(ADDCLOUD, 1000)

ADDCOIN = pygame.USEREVENT + 6
pygame.time.set_timer(ADDCOIN, 500)


player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

spacecrafts = pygame.sprite.Group()
Fog = pygame.sprite.Group()
health = pygame.sprite.Group()
clouds = pygame.sprite.Group()
coins = pygame.sprite.Group()


running = True

clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_r and live <= 0:
                player = Player()
                all_sprites.add(player)
                #player.rect.move_ip(100, 100)
                live = 100
                score = 0
            if event.key == K_ESCAPE:
                RUNING = False

        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDHEALTH:
            new_health = Health()
            health.add(new_health)
            all_sprites.add(new_health)

        elif event.type == ADDFOG:
            new_fog = fog()
            Fog.add(new_fog)
            all_sprites.add(new_fog)

        elif event.type == ADDCRAFT:
            new_craft = Spacecraft()
            spacecrafts.add(new_craft)
            all_sprites.add(new_craft)

        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

        elif event.type == ADDCOIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()
    spacecrafts.update()
    Fog.update()
    health.update()
    clouds.update()
    coins.update()

    screen.fill((0,255,255))

    font = pygame.font.SysFont("Tahoma", 25)
    live_text = font.render("HEALTH:" + str(live), True, (0, 0, 0))
    screen.blit(live_text, (100, 20))

    font = pygame.font.SysFont("Tahoma", 25)
    score_text = font.render("COINS:" + str(score), True, (0, 0, 0))
    screen.blit(score_text, (950, 20))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)


    if pygame.sprite.spritecollideany(player, enemies):
        # If so, remove the player
        enem = pygame.sprite.spritecollideany(player, enemies)
        enem.kill()
        live -= 10


    if pygame.sprite.spritecollideany(player, health):
        # If so, remove the player
        live += 20
        hea = pygame.sprite.spritecollideany(player, health)
        hea.kill()

    if pygame.sprite.spritecollideany(player, spacecrafts):
        # If so, remove the player
        spcr = pygame.sprite.spritecollideany(player, spacecrafts)
        spcr.kill()
        live -= 40


    if pygame.sprite.spritecollideany(player, clouds):
        # If so, remove the player
        clo = pygame.sprite.spritecollideany(player, clouds)
        clo.kill()
        live -= 5

    if pygame.sprite.spritecollideany(player, coins):
        # If so, remove the player
        cis = pygame.sprite.spritecollideany(player, coins)
        cis.kill()
        score += 1



    if live <= 0:
        player.kill()
        player.rect.move_ip(1000, 1000)
        font = pygame.font.SysFont("Tahoma", 25)
        gameover_text = font.render("GAMEOVER" , True, (0, 0, 0))
        screen.blit(gameover_text, (450, 200))
        live = 0
        font = pygame.font.SysFont("Tahoma", 50)
        restart_text = font.render("RESTART", True, (0, 0, 0))
        screen.blit(restart_text, (50, 400))
        font = pygame.font.SysFont("Tahoma", 50)
        Exit_text = font.render("EXIT", True, (0, 0, 0))
        screen.blit(Exit_text, (750, 400))




    clock.tick(60)





    pygame.display.flip()