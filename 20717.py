import pygame

import random

import sys

# 초기화

pygame.init()

# 화면 설정

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("🚀 Space Blaster 9000 👾")

# 색상

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

RED   = (255, 0, 0)

GREEN = (0, 255, 0)

# FPS

clock = pygame.time.Clock()

FPS = 60

# 글꼴

font = pygame.font.SysFont("consolas", 28)

# 플레이어 클래스

class Player(pygame.sprite.Sprite):

    def init(self):

        super().__init__()

        self.image = pygame.Surface((50, 40))

        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH // 2

        self.rect.bottom = HEIGHT - 10

        self.speed = 5

    def update(self, keys):

        if keys[pygame.K_LEFT] and self.rect.left > 0:

            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:

            self.rect.x += self.speed

# 적 클래스

class Enemy(pygame.sprite.Sprite):

    def init(self, x, y):

        super().__init__()

        self.image = pygame.Surface((40, 30))

        self.image.fill(RED)

        self.rect = self.image.get_rect(topleft=(x, y))

        self.speed_x = 2

    def update(self):

        self.rect.x += self.speed_x

        if self.rect.right >= WIDTH or self.rect.left <= 0:

            self.speed_x *= -1

            self.rect.y += 30

        if self.rect.bottom >= HEIGHT:

            global game_over

            game_over = True

# 총알 클래스

class Bullet(pygame.sprite.Sprite):

    def init(self, x, y):

        super().__init__()

        self.image = pygame.Surface((5, 10))

        self.image.fill(WHITE)

        self.rect = self.image.get_rect(center=(x, y))

        self.speed = -8

    def update(self):

        self.rect.y += self.speed

        if self.rect.bottom < 0:

            self.kill()

# 그룹 생성

player = Player()

player_group = pygame.sprite.Group(player)

bullets = pygame.sprite.Group()

enemies = pygame.sprite.Group()

# 적 스폰

for i in range(6):

    for j in range(4):

        enemy = Enemy(80 + i  100, 50 + j  50)

        enemies.add(enemy)

# 점수

score = 0

game_over = False

# 게임 루프

running = True

while running:

    clock.tick(FPS)

    screen.fill(BLACK)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                bullet = Bullet(player.rect.centerx, player.rect.top)

                bullets.add(bullet)

    if not game_over:

        player.update(keys)

        bullets.update()

        enemies.update()

        # 충돌 체크

        for bullet in bullets:

            hits = pygame.sprite.spritecollide(bullet, enemies, True)

            if hits:

                bullet.kill()

                score += 10

        # 그리기

        player_group.draw(screen)

        bullets.draw(screen)

        enemies.draw(screen)

        score_text = font.render(f"Score: {score}", True, WHITE)

        screen.blit(score_text, (10, 10))

    else:

        game_over_text = font.render("👾 GAME OVER 👾", True, RED)

        screen.blit(game_over_text, (WIDTH // 2 - 120, HEIGHT // 2 - 20))

    pygame.display.flip()

숭배합니다 대희재