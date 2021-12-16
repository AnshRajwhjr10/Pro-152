# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:49:12 2021

@author: Ansh Raj
"""
import matplotlib.pyplot as plt

data = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0],
        ]
plt.imshow(data, cmap = 'gray')
plt.show()
