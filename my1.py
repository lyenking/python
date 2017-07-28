
background_image = 'sushiplate.jpg'
mouse_image = 'fugu.png'


import pygame

# 导入一些常用的函数和变量
from pygame.locals import *

# 导入sys的退出函数
from sys import exit


# 初始化
pygame.init()


# create a 窗口 三个参数第一个为元祖，代表分辨率（必须）
#第二个是一个标志位，如果不用什么特性，就指定0；
        #FULLSCREEN     创建一个全屏窗口
        #OPENGL     	创建一个OPENGL渲染的窗口
        #RESIZABLE 	创建一个可以改变大小的窗口
        #NOFRAME 	创建一个没有边框的窗口

#第三个为色深。最大32
#screen = pygame.display.set_mode((640,480),0,32)
screen = pygame.display.set_mode((1092,1080),NOFRAME, 32)

# 设置标题
pygame.display.set_caption("hello my first game")


# 加载图片,并转换图片
background = pygame.image.load(background_image).convert()
mouse = pygame.image.load(mouse_image).convert_alpha() # alpha透明


# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()

    # 将背景图片画上去
    #screen.blit(background, (0,0))

    # 获得鼠标位置
    x, y = pygame.mouse.get_pos()

    # 计算光标的左上角位置
    x-= mouse.get_width() / 2
    y-= mouse.get_height() / 2

    # 把光标画上去 第一个参数为一个Surface对象，第二个为左上角位置。画完以后一定记得用update更新一下，否则画面一片漆黑。
    screen.blit(mouse, (x, y))

    # 刷新画面
    pygame.display.update()








































    


