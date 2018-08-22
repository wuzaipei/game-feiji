import pygame
from  MainGame import *

class Bullet:
    def __init__(self,image):
        self.width = 8
        self.height = 22
        self.x,self.y = pygame.mouse.get_pos()
        self.y = self.y - self.height-40
        self.x = self.x - 5
        self.speed=-5
        self.image = image

    # 子弹走路的方法
    def move(self):
        self.y += self.speed

    # 检测子弹是否越界

    def isOutOfBound(self):
        return self.y <= -self.height

    def hit(self,enemy):
        return self.x+self.width >= enemy.x and self.x <= enemy.x+enemy.width and self.y+self.height >= enemy.y and self.y <=  enemy.y+enemy.height


