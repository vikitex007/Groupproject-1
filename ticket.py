from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from tkinter import messagebox
import sqlite3


root = tk.Tk()
root.geometry('1500x760')
root.title('Bus Sewa')

head_frame = tk.Frame(root, bg='#3AAFA9', highlightbackground='WHITE', highlightthickness=1)
passenger = Label(head_frame, text='Call Us:9847344775', font=('times new roman', 14), bg='#3AAFA9', fg='black',)
passenger.place(x=40,y=20,)
def reg():
    import registration

Register_btn = tk.Button(head_frame, text='Register',command=reg,
                         font=(14), bd=0, bg='#3AAFA9', fg='black',
                         activebackground='#3AAFA9', activeforeground='white')
Register_btn.pack(side=tk.RIGHT, anchor=tk.W)

def login():
    import login
        
        
Signin_btn = tk.Button(head_frame, text='Login',command=login,
                       font=(14), bd=0, bg='#3AAFA9', fg='black',
                       activebackground='#3AAFA9', activeforeground='white')
Signin_btn.pack(side=tk.RIGHT, anchor=tk.W)


howto_btn = tk.Button(head_frame, text='How to buy ticket?',
                      font=(14), bd=0, bg='#3AAFA9', fg='black',
                      activebackground='#3AAFA9', activeforeground='white')
howto_btn.pack(side=tk.RIGHT, anchor=tk.W)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=70)

frame_back = Frame(root, bg='white', highlightbackground='black', highlightthickness=2)
frame_back.place(anchor='center', relx=0.5, rely=0.5)

Ticket = Label(frame_back, text='Ticket', font=('times new roman', 25), bg='white', fg='black').place(x=40,
                                                                                                                y=40)

nameof = Label(frame_back, text='Ticket No.', font=('times new roman', 14), bg='white', fg='black').place(x=40,
                                                                                                                y=120)
textbox3 = Entry(frame_back, font=('times new roman', 25)).place(x=40, y=150)

email = Label(frame_back, text='Mobile Number', font=('times new roman', 14), bg='white', fg='black').place(x=40,
                                                                                                                y=210)
textbox3 = Entry(frame_back, font=('times new roman', 25)).place(x=40, y=240)

conformation = tk.Button(frame_back, text='Print Ticket',
                       font=(14), bd=0, bg='#296d98', fg='white', activebackground='#296d98', activeforeground='white',padx=100, pady=10)
conformation.place(x=320, y=400)


frame_back.place(x=5, y=10)
frame_back.pack_propagate(False)
frame_back.configure(height=600, width=800)


root.mainloop()