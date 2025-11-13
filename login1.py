# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 05:53:04 2025

@author: HP
"""

import tkinter as tk
def show_txt():
    user_txt = entry.get()
    pwd_txt= entry1.get()
    label.config(text= f"Username:{user_txt}| password:{pwd_txt}")
#  creating first label and field
root = tk.Tk()
root.title("Login successful")
root.geometry("400x400")
root.config(bg="#333333")
label= tk.Label(root,text="Username:",font=("Arial",14))
label.config(bg="#555555",fg="white")
label.pack(pady=(30,10))
entry= tk.Entry(root,font=("Arial",14))
entry.pack(pady=10,ipady=5)
#creating second field
label1= tk.Label(root,text="Password:",font=("Arial",14))
label1.config(bg="#555555",fg="white")
label1.pack(pady=(30,10))

entry1= tk.Entry(root,show ="*",font=("Arial",14))

entry1.pack(pady=10,ipady=5)

button = tk.Button(root,text="Submit",command = show_txt ,font =("Arial",14))
button.config(bg="green",fg="white",activebackground="darkgreen")
button.pack(pady=10, padx=50,ipady=8)
root.mainloop()    

