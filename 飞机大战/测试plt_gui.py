# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi*2,np.pi*2,0.1)
y = np.sin(x)

for i in range(2):
    plt.figure(i)
    if i == 0:
        plt.scatter(x,y,s=5)
    elif i == 1:
        plt.plot(x,y)

plt.show()
