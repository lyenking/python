import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen_size = (640,480)
screen = pygame.display.set_mode(screen_size,0,32)

font = pygame.font.SysFont("arial",16)
font_height = font.get_linesize()
event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))

    # ��ȡʱ������
    event_text = event_text[-screen_size[1]/font_height:]

    #�����Ƭ������֤��event_text����ֻ����һ����Ļ������
    if event.type == QUIT:
        exit()

    screen.fill((255,255,255))

    y = screen_size[1] - font_height

    #��һ�����ʵ����λ�ã������濪ʼ����Ҫ��һ�еĿ�
    for text in reversed(event_text):
        screen.blit( font.render(text, True, (0,212,0)), (0,y))
        y -= font_height


    pygame.display.update()















    
	



















