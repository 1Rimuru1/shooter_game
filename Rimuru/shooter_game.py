from pygame import *
#mixer.init()
#mixer.music.load("space.ogg")
font.init()
from random import randint
font1 = font.Font(None, 36)
window  = display.set_mode((700,500))
display.set_caption("Шутер")

background = transform.scale(
    image.load("Kosmo.jpg.jpg"),
    (700, 500)
)

bullets = sprite.Group()
finish = False
clock = time.Clock()
FPS = 999

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (100, 100))
        self.speed = 4
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Bullet(GameSprite):
    def __init__(self, bullet_image, speed, x, y):
        super().__init__(bullet_image, speed, x, y)
    def update(self):
        if self.rect.y <= 0:
            self.kill()
        self.rect.y -= 3

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 620:
            self.rect.x += self.speed
    def fire(self):
        global Bullet
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:
            bullet = Bullet("bullet.png", 1, self.rect.x, self.rect.y)
            bullets.add(bullet)
lost = 0

class Enemy(GameSprite):
    def __init__(self, enemy_image, enemy_x, enemy_y, enemy_speed):
        super().__init__(enemy_image, enemy_x, enemy_y, enemy_speed)
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y >= 470:
            self.rect.y = 0
            self.rect.x = randint(0, 700)
            lost = lost + 1

enemys = sprite.Group()





player = Player('rocket.png', 20, 50, 400)

#mixer.music.play()
game = True
while game:
    text_lose = font1.render(
        "Пропущено:" + str(lost), 1, (255, 255, 255))
    for i in range(1):
        enemy = Enemy("ufo.png", randint(0, 700), 0, 20)
        enemys.add(enemy)
    sprites_list = sprite.groupcollide(
        enemys, bullets, True, True
    )
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        window.blit(text_lose, (0, 0))
        player.fire()
        player.reset()
        player.update()
        enemys.update()
        enemys.draw(window)
        bullets.update()
        bullets.draw(window)


        clock.tick(FPS)
        display.update()