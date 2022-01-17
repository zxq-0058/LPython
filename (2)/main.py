"""
制作飞机大战游戏
"""

import pygame
import random

# Global Variables
Screen_width = 500
Screen_Height = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((Screen_width, Screen_Height))
clock = pygame.time.Clock()
FPS = 60
Fire_ID = pygame.USEREVENT
Enemy_ID = pygame.USEREVENT + 1

# image load
plane_img = pygame.image.load('image/plane.png').convert_alpha()
bg_img = pygame.image.load('image/bg.png').convert_alpha()
bullet_img = pygame.image.load('image/bullet.jpeg').convert_alpha()
enemy_img = pygame.image.load('image/enemy.jpeg')



class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bullet_img
        self.speed = -2
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()



class Enemy_Plane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.speed = 3
    def update(self):
        self.rect.y += self.speed
        if(self.rect.bottom > Screen_Height):
            self.kill()


class Enemys():
    def __init__(self):
        self.planes = pygame.sprite.Group()
    def draw(self):
        self.planes.update()
        self.planes.draw(screen)
    def generate(self):
        enemy_plane = Enemy_Plane()
        enemy_plane.rect.bottom = 50
        enemy_plane.rect.centerx = random.randint(20,550)
        self.planes.add(enemy_plane)

class Plane(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(plane_img, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        dx = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= 10
        if key[pygame.K_d]:
            dx += 10
        self.rect.x += dx
        if self.rect.x < 0: self.rect.x = 0
        elif self.rect.x > Screen_width - 40 : self.rect.x = Screen_width - 40


class Player():
    def __init__(self):
        self.plane = Plane(Screen_width // 2, Screen_Height - 150)
        self.bullets = pygame.sprite.Group()

    def fire(self):
        bullet = Bullet()
        bullet.rect.bottom = self.plane.rect.y - 5
        bullet.rect.centerx = self.plane.rect.centerx
        self.bullets.add(bullet)

    def move(self):
        self.plane.move()


    def draw(self):
        screen.blit(self.plane.image, (self.plane.rect.x - 10 , self.plane.rect.y))
        pygame.draw.rect(screen, WHITE, self.plane.rect, 2)
        self.bullets.update()
        self.bullets.draw(screen)


def Game_init():
    pygame.init()
    pygame.time.set_timer(Fire_ID, 500)
    pygame.time.set_timer(Enemy_ID, 1000)
    global player
    player = Player()
    global enemys
    enemys = Enemys()

def Game_Logic():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == Fire_ID:
            player.fire()
        elif event.type == Enemy_ID:
            enemys.generate()

    player.move()
    pygame.sprite.groupcollide(player.bullets, enemys.planes, True, True)
    Check_List = pygame.sprite.spritecollide(player.plane, enemys.planes, True)
    if(len(Check_List) > 0):
        print("Game Over!")
        return False
    return True

def Screen_Update():
    # background
    screen.fill(WHITE)
    # player
    player.draw()
    # enemy planes
    enemys.draw()
    pygame.display.update()

def Game():

    Game_init()

    Running = True
    while Running:
        clock.tick(FPS)
        Running = Game_Logic()
        Screen_Update()

    pygame.quit()

def main():
    Game()

if __name__ == "__main__":
    main()
