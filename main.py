from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from tkinter import messagebox
import sqlite3
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter.messagebox as tkMessagebox
import sqlite3




root = tk.Tk()
# root.geometry('900x500')
root.title('Bus Sewa')





# image = Image.open('bussss.png')
# my_image = ImageTk.PhotoImage(image)
# label = Label(root,image = my_image).place(x=0,y=0)


def toggle_menu():
    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='☰')
        toggle_btn.config(command=toggle_menu)

    toggle_menu_fm = tk.Frame(root, bg='#3AAFA9')

    Vehicle_btn = tk.Button(toggle_menu_fm, text='Vehicle hire',
                            font=(20), bd=0, bg='#3AAFA9', fg='white',
                            activebackground='#3AAFA9', activeforeground='white')

    Vehicle_btn.place(x=20, y=20)

    def ticket():
        import ticket

    Bushire_btn = tk.Button(toggle_menu_fm, text='Bus Ticket',command=ticket,
                            font=(20), bd=0, bg='#3AAFA9', fg='white',
                            activebackground='#3AAFA9', activeforeground='white')

    Bushire_btn.place(x=20, y=60)

    window_height = root.winfo_height()

    toggle_menu_fm.place(x=0, y=50, height=window_height, width=200)

    toggle_btn.config(text='X')
    toggle_btn.config(command=collapse_toggle_menu)


head_frame = tk.Frame(root, bg='#3AAFA9', highlightbackground='WHITE', highlightthickness=1)

toggle_btn = tk.Button(head_frame, text='☰', bg='#3AAFA9', fg='white',
                       font=('Bold', 20), bd=0,
                       activebackground='#3AAFA9', activeforeground='white',
                       command=toggle_menu)

toggle_btn.pack(side=tk.LEFT, anchor=tk.W)

title_lb = tk.Label(head_frame, text='Bus Sewa', bg='#3AAFA9', fg='white',
                    font=('Bold', 20))

title_lb.pack(side=tk.LEFT)

def reg():
    import registration



Register_btn = tk.Button(head_frame, text='Register',command=reg,
                         font=(14), bd=0, bg='#3AAFA9', fg='white',
                         activebackground='#3AAFA9', activeforeground='white')
Register_btn.pack(side=tk.RIGHT, anchor=tk.W)

def login():
    import login
        
        
Signin_btn = tk.Button(head_frame, text='Login',command=login,
                       font=(14), bd=0, bg='#3AAFA9', fg='white',
                       activebackground='#3AAFA9', activeforeground='white')
Signin_btn.pack(side=tk.RIGHT, anchor=tk.W)


def buy():
    import tutorial
    

howto_btn = tk.Button(head_frame, text='How to buy ticket?',command=buy,
                      font=(14), bd=0, bg='#3AAFA9', fg='white',
                      activebackground='#3AAFA9', activeforeground='white')
howto_btn.pack(side=tk.RIGHT, anchor=tk.W)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=70)

frame_login = Frame(root, bg='#3AAFA9', highlightbackground='WHITE', highlightthickness=2)

leaving = Label(frame_login, text='From', font=('times new roman', 25), bg='#3AAFA9', fg='white').place(x=40,y=40)
leaving_entry = Entry(frame_login, font=('times new roman', 25))
leaving_entry.place(x=40, y=90)

going = Label(frame_login, text='To', font=('times new roman', 25), bg='#3AAFA9', fg='white').place(x=40, y=150)
going_entry = Entry(frame_login, font=('times new roman', 25))
going_entry.place(x=40, y=200)

Travel = Label(frame_login, text='Travel Date', font=('times new roman', 25), bg='#3AAFA9', fg='white').place(x=40,y=260)
travel_entry = Entry(frame_login, font=('times new roman', 25))
travel_entry.place(x=40, y=310)

shift = Label(frame_login, text='Select Shift', font=('times new roman', 25), bg='#3AAFA9', fg='white').place(x=40, y=370)
var = IntVar()
Radiobutton1 = Radiobutton(frame_login, text="Day", variable=var, value=1, command=lambda: print(var.get()))
Radiobutton1.config(font=(14), bd=0, bg='#3AAFA9', fg='black', activebackground='#3AAFA9', activeforeground='white')
Radiobutton1.place(x=50, y=420)


Radiobutton3 = Radiobutton(frame_login, text="Night", variable=var, value=3, command=lambda: print(var.get()))
Radiobutton3.config(font=(14), bd=0, bg='#3AAFA9', fg='black', activebackground='#3AAFA9', activeforeground='white')
Radiobutton3.place(x=200, y=420)


frame_login.pack(side=tk.RIGHT, anchor=tk.W)
frame_login.pack_propagate(False)
frame_login.configure(height=600, width=500)

frame_back = Frame(root, bg='#3AAFA9', highlightbackground='WHITE', highlightthickness=2)
frame_back.place(anchor='center', relx=0.5, rely=0.5)


# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("bussss.png"))

# Create a Label Widget to display the text or Image
label = Label(frame_back, image=img)
label.pack()

frame_back.pack(side=tk.LEFT, anchor=tk.W)
frame_back.pack_propagate(False)
frame_back.configure(height=600, width=1025)

from time import strftime


def my_time():
    time_string = strftime('%H:%M:%S %p \n %A \n %x')  # time format
    l1.config(text=time_string)
    l1.after(1000, my_time)  # time delay of 1000 milliseconds


my_font = ('times', 12, 'bold')  # display size and style

l1 = tk.Label(head_frame, font=my_font, bg='#3AAFA9', fg='white')
l1.pack(side=TOP, ipadx=10, ipady=0)

my_time()



##################################################databse#############################
# conn = sqlite3.connect('main.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE mainn(
#             leave text,
#             going text,
#             travel int,
#             radio text
#     )""")
# print('Table created succesfully')
# conn.commit()
# conn.close()

def add():
    if leaving_entry.get()=='' or going_entry.get()=='' or travel_entry.get()=='' or var.get()=='':
        messagebox.showerror('error','Please fill all details')
        

    else:
        conn = sqlite3.connect('main.db')
        c = conn.cursor()
        c.execute("INSERT INTO mainn VALUES(:leave, :going, :travel,:radio)",{
        'leave':leaving_entry.get(),
        'going':going_entry.get(),
        'travel':travel_entry.get(),
        'radio':var.get()
        })
        conn.commit()
        conn.close()
    # messagebox.showinfo('info','your  data has been saved')

def main():
    import main2

# def query():
#     import main2
#     conn = sqlite3.connect('main.db')
#     c = conn.cursor()

#     c.execute("SELECT *,oid FROM mainn")

#     records = c.fetchall()
#     print(records)

#     print_record=''
#     for record in records:
#         print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[3]) + '\n'
    
#     query_label = Label(root, text = print_record)
#     query_label.pack(x = 100, y=200, columnspan=2)

#     conn.commit()
#     conn.close()



    
Signin_btn = tk.Button(frame_login, text='Search Buses',
                       font=(14), bd=0, bg='#296d98', fg='white', activebackground='#296d98',command=lambda:[add(),main()], activeforeground='white',padx=100, pady=10)
Signin_btn.place(x=80, y=500)

root.mainloop()