# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 18:29:36 2025

@author: HP
"""

import tkinter as tk
def show_txt():
    user_txt= entry.get()
    label.config(text = f"you typed:{ user_txt}")
root = tk.Tk()
root.title("Input Example")
root.geometry("400x300")
label= tk.Label(root, text="Type something below ",font =("Blue",14))
label.pack(pady=10)
entry =tk.Entry(root,font=("Arial",14))
entry.pack(pady=10)
button =tk.Button(root,text="Show Text",command =show_txt,font=("Arial",12))
button.pack(pady=10)
root.mainloop()

