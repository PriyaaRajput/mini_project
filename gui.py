# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 17:43:50 2025

@author: HP
"""

import tkinter as tk
root =tk.Tk()
root.title("Label example")
root.geometry("400x300")

label = tk.Label(root, text= "hello guys", font =("Arial",18))
label.pack(pady=20)
root.mainloop()