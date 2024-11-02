# source material: http://www.codingwithruss.com/pygame/how-to-use-pygame-masks-for-pixel-perfect-collision/

import pygame

pygame.init()

# размер окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Masks")

# объявление цветов
BG = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


# создание класса Солдат
class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Если поверхность была создана на базе изображения с альфа-каналом (картинки формата png)
        # то используем convert_alpha() для эффективной обработки при запуске игры
        self.image = pygame.image.load("soldier.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        print(self.rect.x)
        print(self.rect.y)
        print(self.rect.top)
        print(self.rect.left)
        print(self.rect.bottom)
        print(self.rect.right)
        print(self.rect.size)
        print(self.rect.w)
        self.mask = pygame.mask.from_surface(self.image)


# создание класса Пуля
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, colour):
        pos = pygame.mouse.get_pos()
        self.rect.center = (pos)
        self.image.fill(colour)


# скрыть курсор мыши
pygame.mouse.set_visible(False)

# создание экземпляров класса
soldier = Soldier(350, 250)
bullet = Bullet()

# создание групп
soldier_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# добавление в группы
soldier_group.add(soldier)
bullet_group.add(bullet)

# главный цикл
run = True
while run:

    # заливка фона
    screen.fill(BG)

    if pygame.sprite.spritecollide(bullet, soldier_group, False, pygame.sprite.collide_mask):
        col = RED
    else:
        col = GREEN

    bullet_group.update(col)

    soldier_group.draw(screen)
    bullet_group.draw(screen)

    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # обновление содержимого окна
    pygame.display.flip()

pygame.quit()