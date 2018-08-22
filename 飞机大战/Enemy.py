import pygame
from random import randint
from MainGame import *
from Bullet import *
class Enemy:
    def __init__(self,image):
        self.width = 61
        self.height = 43
        self.y = -self.height
        self.x = randint(0,420)  # 产生随机的敌战舰
        self.speed=2
        self.image = image

    # 敌方战舰走路的方法
    def move(self):
        self.y += self.speed

    # 检测敌方战舰是否越界
    def crash(self):

        pass




# import cv2
# from scipy.misc import imresize
# import numpy as np
#
# x = np.random.randn(100)
# x = np.sort(x)
# y = np.sin(x)
# print(x)
# plt.plot(x,y)
# plt.show()

