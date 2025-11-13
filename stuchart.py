# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 16:11:49 2025

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
file_path="C:/Users/HP/Documents/stu.xlsx"
data =pd.read_excel("file_path")
print(data)
plt.xlabel("Name")
plt.ylabel("Hours")
plt.show()