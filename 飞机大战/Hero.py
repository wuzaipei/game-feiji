import pygame
from MainGame import *


class Hero:

    def __init__(self,image):
        self.image = image
        # 飞机的宽
        self.width = 104
        # 飞机的高
        self.height = 122
        # 飞机初始化的纵坐标
        self.x = (MainGame.WIDTH/2) - self.width/2
        # 飞机初始化的横坐标
        self.y = (MainGame.HEIGHT/2) - self.height/2

    def move(self,screen):
        self.x,self.y = pygame.mouse.get_pos()
        self.x = self.x - self.width/2
        self.y = self.y - self.height/2
        screen.blit(self.image,(self.x,self.y))





