from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

root = tk.Tk()
root.geometry('900x500')
root.title('Bus Sewa')

image = Image.open('bus.png')
my_image = ImageTk.PhotoImage(image)
label = Label(root,image = my_image).place(x=0,y=0)


def toggle_menu():

    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='☰')
        toggle_btn.config(command= toggle_menu)

    toggle_menu_fm = tk.Frame(root, bg='#3AAFA9')

    Vehicle_btn = tk.Button(toggle_menu_fm, text='Vehicle hire',
                        font = (20), bd=0, bg='#3AAFA9', fg='white', 
                        activebackground='#3AAFA9', activeforeground='white')

    Vehicle_btn.place(x=20,y=20)

    # placelist = ['Kathmandu','Hetauda','Pokhara']
    # cmb=ttk.Combobox(root,value=placelist,width=0)
    # cmb.place(x=20, y=100, width=100)


    Bushire_btn = tk.Button(toggle_menu_fm, text='Bus Hire',
                        font = (20), bd=0, bg='#3AAFA9', fg='white', 
                        activebackground='#3AAFA9', activeforeground='white')

    Bushire_btn.place(x=20,y=60)


    window_height= root.winfo_height()

    toggle_menu_fm.place(x=0, y=50, height=window_height, width=200)

    toggle_btn.config(text = 'X')
    toggle_btn.config(command=collapse_toggle_menu)


head_frame = tk.Frame(root,bg='#3AAFA9', highlightbackground='WHITE', highlightthickness=1)

toggle_btn = tk.Button(head_frame, text='☰', bg='#3AAFA9', fg='white',
                       font=('Bold', 20), bd=0,
                       activebackground='#3AAFA9', activeforeground='white',
                       command = toggle_menu)
 
toggle_btn.pack(side=tk.LEFT, anchor=tk.W)
 
title_lb = tk.Label(head_frame, text='Bus Sewa', bg='#3AAFA9', fg='white',
                       font=('Bold', 20))

title_lb.pack(side=tk.LEFT)

Register_btn = tk.Button(head_frame, text='Register',
                        font = (14), bd=0, bg='#3AAFA9', fg='white', 
                        activebackground='#3AAFA9', activeforeground='white')
Register_btn.pack(side=tk.RIGHT, anchor=tk.W)

Signin_btn = tk.Button(head_frame, text='Sign in',
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

frame_login = Frame(root,bg='#3AAFA9', highlightbackground='WHITE', highlightthickness=2)

leaving=Label(frame_login,text='Leaving From',font=('times new roman',25),bg='#3AAFA9',fg='white').place(x=40,y=40)
textbox1= Entry(frame_login,font=('times new roman',25)).place(x=40,y=90)
going=Label(frame_login,text='Going Destination',font=('times new roman',25),bg='#3AAFA9',fg='white').place(x=40,y=150)
textbox2= Entry(frame_login,font=('times new roman',25)).place(x=40,y=200)
Travel=Label(frame_login,text='Travel Date',font=('times new roman',25),bg='#3AAFA9',fg='white').place(x=40,y=260)
textbox2= Entry(frame_login,font=('times new roman',25)).place(x=40,y=310)

frame_login.pack(side=tk.RIGHT, anchor=tk.W)
frame_login.pack_propagate(False)
frame_login.configure(height=600,width=500)

# frame_back = Frame(root,bg='#3AAFA9', highlightbackground='WHITE', highlightthickness=2)

# frame_back.pack(side=tk.LEFT, anchor=tk.W)
# frame_back.pack_propagate(False)
# frame_back.configure(height=600,width=1025)


root.mainloop()