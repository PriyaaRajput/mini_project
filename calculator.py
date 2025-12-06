import tkinter as tk
root=tk.Tk()
root.title("Calculator")
root.geometry("300x500")

screen= tk.Entry(root,width=35,borderwidth=5)
screen.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def btn_click(value):
    if value =="clear":
        screen.delete(0,tk.END)
    elif value =="=":
        try:
            result= eval(screen.get())
            screen.delete(0,tk.END)
            screen.insert(0,str(result))
        except Exception:
            screen.delete(0,tk.END)
            screen.insert(0,"Error")
    else:
      screen.insert(tk.END,str(value))        
    
    
    
button1=tk.Button(root,text="1",padx=40,pady=30,command=lambda:btn_click(1))
button2=tk.Button(root,text="2",padx=40,pady=30,command=lambda:btn_click(2))
button3=tk.Button(root,text="3",padx=40,pady=30,command=lambda:btn_click(3))
button4=tk.Button(root,text="4",padx=40,pady=30,command=lambda:btn_click(4))
button5=tk.Button(root,text="5",padx=40,pady=30,command=lambda:btn_click(5))
button6=tk.Button(root,text="6",padx=40,pady=30,command=lambda:btn_click(6))
button7=tk.Button(root,text="7",padx=40,pady=30,command=lambda:btn_click(7))
button8=tk.Button(root,text="8",padx=40,pady=30,command=lambda:btn_click(8))
button9=tk.Button(root,text="9",padx=40,pady=30,command=lambda:btn_click(9))
button0=tk.Button(root,text="0",padx=40,pady=30,command=lambda:btn_click(0))
buttonadd=tk.Button(root,text="+",padx=86,pady=30,command=lambda:btn_click("+"))
buttoneq=tk.Button(root,text="=",padx=40,pady=30,command=lambda:btn_click("="))
buttonclear=tk.Button(root,text="clear",padx=79,pady=30,command=lambda:btn_click("clear"))
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

button0.grid(row=4,column=0)
buttonadd.grid(row=4,column=1,columnspan=2)

buttoneq.grid(row=5,column=0)
buttonclear.grid(row=5,column=1,columnspan=2)
root.mainloop()