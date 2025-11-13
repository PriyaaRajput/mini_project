# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 19:13:08 2025

@author: HP
"""

import tkinter as tk
root =tk.Tk()
root.title("Login Example")
root.geometry("400x400")

label= tk.Label(root, text="type something below", font=("Arial",14)) 
label.pack(pady=10) 
  
entry= tk.Entry(root,font=("Arial",14))
entry.pack(pady=10)
entry1= tk.Entry(root,show ="*",font=("Arial",14))
entry1.pack(10)

def show_txt():
    label.config( text= f"Input here :{entry.get()} | password:{entry1.get()}")

button =tk.Button(root,text="Login",command =show_txt ,font=("Arial",12))
button.pack(pady=10)
root.mainloop()    