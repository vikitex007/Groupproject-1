


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


passenger = Label(frame_back, text='Passenger Details', font=('times new roman', 20), bg='white', fg='black').place(x=40,
                                                                                                                y=40)

mandatory = Label(frame_back, text='All fields are mandatory', font=('times new roman', 11), bg='white', fg='black').place(x=60,
                                                                                                                y=80)
nameof = Label(frame_back, text='Name of Passenger', font=('times new roman', 14), bg='white', fg='black').place(x=40,
                                                                                                                y=120)
passenger_name = Entry(frame_back, font=('times new roman', 25))
passenger_name.place(x=40, y=150)

email = Label(frame_back, text='E-mail', font=('times new roman', 14), bg='white', fg='black').place(x=40,
                                                                                                                y=210)
passenger_email = Entry(frame_back, font=('times new roman', 25))
passenger_email.place(x=40, y=240)

number = Label(frame_back, text='Mobile Number', font=('times new roman', 14), bg='white', fg='black').place(x=40,
                                                                                                                y=300)
passenger_number = Entry(frame_back, font=('times new roman', 25))
passenger_number.place(x=40, y=330)

address = Label(frame_back, text='Pickup Address', font=('times new roman', 14), bg='white', fg='black').place(x=420,
                                                                                                                y=120)
passenger_address = Entry(frame_back, font=('times new roman', 25))
passenger_address.place(x=420, y=150)

payment = Label(frame_back, text='Payment Method', font=('times new roman', 20), bg='white', fg='black').place(x=420,
                                                                                                                y=220)

var = IntVar()
Radiobutton1 = Radiobutton(frame_back, text="E-sewa", variable=var, value=1, command=lambda: print(var.get()))
Radiobutton1.config(font=(14), bd=0, bg='white', fg='black', activebackground='white', activeforeground='black')
Radiobutton1.place(x=420, y=270)

Radiobutton2 = Radiobutton(frame_back, text="KHALTI", variable=var, value=2, command=lambda: print(var.get()))
Radiobutton2.config(font=(14), bd=0, bg='white', fg='black', activebackground='white', activeforeground='black')
Radiobutton2.place(x=580, y=270)

Radiobutton3 = Radiobutton(frame_back, text="iPay", variable=var, value=3, command=lambda: print(var.get()))
Radiobutton3.config(font=(14), bd=0, bg='white', fg='black', activebackground='white', activeforeground='black')
Radiobutton3.place(x=420, y=320)

Radiobutton4 = Radiobutton(frame_back, text="Fone Pay", variable=var, value=4, command=lambda: print(var.get()))
Radiobutton4.config(font=(14), bd=0, bg='white', fg='black', activebackground='white', activeforeground='black')
Radiobutton4.place(x=580, y=320)


goback = tk.Button(frame_back, text='Go Back',
                       font=(14), bd=0, bg='grey', fg='white', activebackground='grey', activeforeground='white',padx=7, pady=4)
goback.place(x=40, y=510)


frame_back.place(x=5, y=10)
frame_back.pack_propagate(False)
frame_back.configure(height=600, width=800)



# conn = sqlite3.connect('passenger_ticket.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE p_details(
#             N_O_P text,
#             Email text,
#             Number int,
#             pickup text
#     )""")
# print('Table created succesfully')
# conn.commit()
# conn.close()

def add ():

    conn = sqlite3.connect('passenger_ticket.db')
    if passenger_name.get() == "" or passenger_email.get() == "" or passenger_number.get() == "" or passenger_address.get() == '':
        messagebox.showerror('error','Please fill all the details')
    
    else:
        conn = sqlite3.connect('passenger_ticket.db')
        c = conn.cursor()
        c.execute("INSERT INTO p_details VALUES(:N_O_P, :Email, :Number, :pickup)",{
        'N_O_P':passenger_name.get(),
        'Email':passenger_email.get(),
        'Number':passenger_number.get(),
        'pickup':var.get(),
            
        })
        messagebox.showinfo('Congratulations','Your ticket has been booked')

conformation = tk.Button(frame_back, text='Confirmation',command=add,font=(14), bd=0, bg='#296d98', fg='white', activebackground='#296d98', activeforeground='white',padx=100, pady=10)
conformation.place(x=320, y=500)


root.mainloop()