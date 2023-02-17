from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

root = tk.Tk()
root.geometry('1500x720')
root.title('Bus Sewa')
root['bg']='white'

head_frame = tk.Frame(root,bg='#3AAFA9', highlightbackground='WHITE', highlightthickness=1)

title_lb = tk.Label(head_frame, text='Bus Sewa', bg='#3AAFA9', fg='white',
                       font=('Bold', 20))

title_lb.pack(side=tk.LEFT)

Register_btn = tk.Button(head_frame, text='Register',
                        font = (14), bd=0, bg='#3AAFA9', fg='white', 
                        activebackground='#3AAFA9', activeforeground='white')
Register_btn.pack(side=tk.RIGHT, anchor=tk.W)


Signin_btn = tk.Button(head_frame, text='Log in',
                        font = (14), bd=0, bg='#3AAFA9', fg='white', 
                        activebackground='#3AAFA9', activeforeground='white')
Signin_btn.pack(side=tk.RIGHT, anchor=tk.W)

howto_btn = tk.Button(head_frame, text='How to buy ticket?',
                        font = (14), bd=0, bg='#3AAFA9', fg='white', 
                        activebackground='#3AAFA9', activeforeground='white')
howto_btn.pack(side=tk.RIGHT, anchor=tk.W)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=70)

# leaving=Label(root,text='Leaving From',font=('times new roman',14),bg='white',fg='black').place(x=40,y=70)
textbox1= Entry(root,font=('times new roman',14)).place(x=120,y=90)
# going=Label(root,text='Going Destination',font=('times new roman',14),bg='white',fg='black').place(x=250,y=150)
textbox2= Entry(root,font=('times new roman',14)).place(x=320,y=90)
# Travel=Label(root,text='Travel Date',font=('times new roman',14),bg='white',fg='black').place(x=40,y=260)
textbox2= Entry(root,font=('times new roman',14)).place(x=520,y=90)
# shift=Label(root,text='Select Shift',font=('times new roman',14),bg='white',fg='black').place(x=40,y=370)

var=IntVar()
Radiobutton1 = Radiobutton(root, text="Day", variable=var, value=1, command=lambda: print(var.get()))
Radiobutton1.config(font=(14), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton1.place(x=720, y=90)

Radiobutton2 = Radiobutton(root, text="Night", variable=var, value=2, command=lambda: print(var.get()))
Radiobutton2.config(font=(14), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=800, y=90)

Signin_btn = tk.Button(root, text='Search Buses',
                       font=(14), bd=0, bg='#296d98', fg='white', activebackground='#296d98', activeforeground='white',padx=50, pady=1)
Signin_btn.place(x=880, y=90)

Travels=Label(root,text='Travels',font=('times new roman',14),bg='white',fg='black').place(x=120,y=150)
Radiobutton2 = Radiobutton(root, text="Super Kabeli Yatayat", variable=var, value=2, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=180)
Radiobutton2 = Radiobutton(root, text="Jam Jam Deluxe", variable=var, value=2, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=210)
Radiobutton2 = Radiobutton(root, text="Safari Yatayat", variable=var, value=2, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=240)
Radiobutton2 = Radiobutton(root, text="Banepa Super Deluxe", variable=var, value=2, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=270)


Bustype=Label(root,text='Bus Type',font=('times new roman',14),bg='white',fg='black').place(x=120,y=320)
Radiobutton2 = Radiobutton(root, text="AC", variable=var, value=2, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=350)
Radiobutton2 = Radiobutton(root, text="AC Deluxe", variable=var, value=2, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=380)
Radiobutton2 = Radiobutton(root, text="Deluxe", variable=var, value=2, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=410)




root.mainloop()