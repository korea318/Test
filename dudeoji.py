import random

import pygame

pygame.init()

WIDTH, HEIGH = 1200, 600
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGH))
font = pygame.font.SysFont(None, 36) #텍스트 폰트
mole_show_time = 1000 # ms
mole_x, mole_y = 0, 0
mole_timer = 0
mole_status = 'normal'
game_duration = 10000

background_img = pygame.image.load('./background.png')
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGH))

mole_img = pygame.image.load('./normal.png')
mole_img = pygame.transform.scale_by(mole_img, 0.2)
mole_hit_img = pygame.image.load('./hit.png')
mole_hit_img = pygame.transform.scale_by(mole_hit_img, 0.5)
mole_miss_img = pygame.image.load('./miss.png')
mole_miss_img = pygame.transform.scale_by(mole_miss_img, 1.0)

mole_rec = mole_img.get_rect()

mouse_img = pygame.image.load('./mouse.png')
mouse_img = pygame.transform.scale_by(mouse_img, 0.4)

pygame.mouse.set_visible(False)

def draw_progress_bar(current_time):
    elapsed_ratio = current_time / game_duration
    progress = max(0, 1 - elapsed_ratio)
    pygame.draw.rect(screen, (255, 0, 0), [50, 20, (WIDTH - 100) * progress, 20])

def spawn_mole():
    global mole_x, mole_y, mole_timer, mole_rec, mole_status
    mole_x, mole_y = random.randint(0, WIDTH-mole_img.get_width()), random.randint(0, HEIGH-mole_img.get_height())
    mole_timer = pygame.time.get_ticks()
    mole_rec.topleft = (mole_x, mole_y)
    mole_status = 'normal'


while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mole_rec.collidepoint(pygame.mouse.get_pos()):
                mole_status = 'hit'
            else:
                mole_status = 'miss'

    screen.blit(background_img, (0, 0))

    current_time = pygame.time.get_ticks()
    if current_time - mole_timer > mole_show_time:
        spawn_mole()

    if mole_status == 'normal':
        screen.blit(mole_img, (mole_x, mole_y))
    elif mole_status == 'hit':
        screen.blit(mole_hit_img, (mole_x, mole_y))
    elif mole_status == 'miss':
        screen.blit(mole_miss_img, (mole_x, mole_y))

    text_surface = font.render("Time Limit", True, BLACK) #텍스트 추가
    screen.blit(text_surface, (50, 0)) #텍스트 위치
    draw_progress_bar(current_time)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(mouse_img, (mouse_x - mouse_img.get_width()//2, mouse_y - mouse_img.get_height()//2))

    pygame.display.update()
