# -*- coding: utf-8 -*-

background_image = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,480), 0, 32)
background = pygame.image.load(background_image).convert_alpha()
Fullscreen = False
x , y = 0,0
move_x , move_y = 0,0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((640, 480), 0, 32)
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0
            
    # 注意换行符，应该是for 循环完之后再执行后面的语句
    x += move_x
    y += move_y

    screen.fill((0,0,0))
    screen.blit(background, (x,y))
    pygame.display.update()
                        
                    























