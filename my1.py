
background_image = 'sushiplate.jpg'
mouse_image = 'fugu.png'


import pygame

# ����һЩ���õĺ����ͱ���
from pygame.locals import *

# ����sys���˳�����
from sys import exit


# ��ʼ��
pygame.init()


# create a ���� ����������һ��ΪԪ�棬����ֱ��ʣ����룩
#�ڶ�����һ����־λ���������ʲô���ԣ���ָ��0��
        #FULLSCREEN     ����һ��ȫ������
        #OPENGL     	����һ��OPENGL��Ⱦ�Ĵ���
        #RESIZABLE 	����һ�����Ըı��С�Ĵ���
        #NOFRAME 	����һ��û�б߿�Ĵ���

#������Ϊɫ����32
#screen = pygame.display.set_mode((640,480),0,32)
screen = pygame.display.set_mode((1092,1080),NOFRAME, 32)

# ���ñ���
pygame.display.set_caption("hello my first game")


# ����ͼƬ,��ת��ͼƬ
background = pygame.image.load(background_image).convert()
mouse = pygame.image.load(mouse_image).convert_alpha() # alpha͸��


# ��Ϸѭ��
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # ���յ��˳��¼����˳�����
            exit()

    # ������ͼƬ����ȥ
    #screen.blit(background, (0,0))

    # ������λ��
    x, y = pygame.mouse.get_pos()

    # ����������Ͻ�λ��
    x-= mouse.get_width() / 2
    y-= mouse.get_height() / 2

    # �ѹ�껭��ȥ ��һ������Ϊһ��Surface���󣬵ڶ���Ϊ���Ͻ�λ�á������Ժ�һ���ǵ���update����һ�£�������һƬ��ڡ�
    screen.blit(mouse, (x, y))

    # ˢ�»���
    pygame.display.update()








































    


