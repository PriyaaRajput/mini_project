# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 05:33:13 2025

@author: HP
"""

import matplotlib.pyplot as plt
import numpy as np
x=["python","java","c","c++"]
y=[85,80,70,75]
z=[20,40,40,10]
width=0.2
p=np.arange(len(x))
p1=[j+width for j in p]
plt.xlabel("language",fontsize=15)
plt.ylabel("popularity",fontsize=15)
c=["m","r","g","b"]
plt.bar(p,y,width,color="r",edgecolor="white",linewidth=2)
plt.bar(p1,z,width,color="y",edgecolor="white",linewidth=2)
plt.xticks(p+width/2,x)
plt.show()