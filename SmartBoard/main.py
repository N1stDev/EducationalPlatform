if __name__ != '__main__': quit()

import pygame
from settings import *
import math

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(DISPLAY_RESOLUTION)
background_surf = pygame.Surface(DISPLAY_RESOLUTION)
background_surf.set_colorkey((255,0,255))
background_surf.fill((255,0,255))

drawing_initiated_flag = False
last_point = pygame.mouse.get_pos()

pictures = [[pygame.image.load('image.png'), [100, 50]], [pygame.image.load('image1.png'), [200, 200]]]
selected_picture = -1

while 1:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()

    # Выбор инструмента
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]: CURRENT_TOOL = 'PEN'
    elif keys[pygame.K_b]: CURRENT_TOOL = 'BRUSH'
    elif keys[pygame.K_e]: CURRENT_TOOL = 'ERASER'
    elif keys[pygame.K_h]: CURRENT_TOOL = 'HAND'

    # Провкерка нажатия лкм
    if not drawing_initiated_flag and pygame.mouse.get_pressed(3)[0]: #Если нажата (только первое нажатие)
        drawing_initiated_flag = True
        last_point = pygame.mouse.get_pos()
        #print('debug')
    elif not pygame.mouse.get_pressed(3)[0]: #Если отпущена
        drawing_initiated_flag = False


    # Здесь проверяется какой инструмент сейчас активен и выполняется соответствующее действие при нажатии
    if drawing_initiated_flag:
        if CURRENT_TOOL in DRAWING_TOOLS:
            interpolation = 20
            step_x = (-pygame.mouse.get_pos()[0] + last_point[0]) / interpolation
            step_y = (-pygame.mouse.get_pos()[1] + last_point[1]) / interpolation

            for i in range(interpolation):
                pygame.draw.circle(background_surf,
                                   TOOL_PARAMS[CURRENT_TOOL]['COLOR'],
                                   (step_x*i + pygame.mouse.get_pos()[0],
                                    step_y*i+pygame.mouse.get_pos()[1]),
                                   TOOL_PARAMS[CURRENT_TOOL]['WIDTH'])
        elif CURRENT_TOOL == 'HAND' and pygame.mouse.get_pressed(3)[0]:
            for p in pictures[::-1]:
                corner = p[1]
                width = p[0].get_width()
                height = p[0].get_height()
                if p[0].get_rect().collidepoint((pygame.mouse.get_pos()[0]-corner[0], pygame.mouse.get_pos()[1]-corner[1])):
                    selected_picture = pictures.index(p)
                    pictures.pop(pictures.index(p))
                    pictures.append(p)
                    break
                else: selected_picture = -1

    screen.fill((200,200,255))

    for p in pictures:
        screen.blit(p[0], p[1])

    screen.blit(background_surf, (0,0))

    # рисуем "курсор"
    if CURRENT_TOOL in DRAWING_TOOLS:
        pygame.draw.circle(
            surface=screen,
            color=[0, 0, 0],
            center=pygame.mouse.get_pos(),
            radius=TOOL_PARAMS[CURRENT_TOOL]['WIDTH'],
            width=1)

    if selected_picture != -1 and drawing_initiated_flag and CURRENT_TOOL == 'HAND':
        corner = pictures[selected_picture][1]
        pygame.draw.rect(screen, [255,0,0], [corner[0], corner[1], pictures[selected_picture][0].get_width(), pictures[selected_picture][0].get_height()], 5)
        pictures[pictures.index(pictures[selected_picture])][1][0] += -last_point[0] + pygame.mouse.get_pos()[0]
        pictures[pictures.index(pictures[selected_picture])][1][1] += -last_point[1] + pygame.mouse.get_pos()[1]

    pygame.display.flip()
    last_point = pygame.mouse.get_pos()
    clock.tick(FPS)





