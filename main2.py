from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
import sqlite3

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


textbox1= Entry(root,font=('times new roman',14))
textbox1.place(x=120,y=90)
   
textbox2= Entry(root,font=('times new roman',14))
textbox2.place(x=320,y=90)
   
textbox3= Entry(root,font=('times new roman',14))
textbox3.place(x=520,y=90)

def query():
    conn = sqlite3.connect('main.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM mainn")

    records = c.fetchall()
    print(records)

    print_record=''
    print_record1 = ""
    print_record2 = ''
    for record in records:
        print_record += str(record[0])+''
        print_record1 += str(record[1])+''
        print_record2 += str(record[2])+''
        
    
   

   
    textbox1= Entry(root,text = print_record,font=('times new roman',14))
    textbox1.place(x=120,y=90)
   
    textbox2= Entry(root,text = print_record1,font=('times new roman',14))
    textbox2.place(x=320,y=90)
   
    textbox3= Entry(root,text = print_record2,font=('times new roman',14))
    textbox3.place(x=520,y=90)

    conn.commit()
    conn.close()



var=IntVar()
Radiobutton1 = Radiobutton(root, text="Day", variable=var, value=1, command=lambda: print(var.get()))
Radiobutton1.config(font=(14), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton1.place(x=720, y=90)

Radiobutton2 = Radiobutton(root, text="Night", variable=var, value=2, command=lambda: print(var.get()))
Radiobutton2.config(font=(14), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=800, y=90)

def passenger():
    import passenger_details

Signin_btn = tk.Button(root, text='Search Buses',command=lambda:[query,passenger()],
                       font=(14), bd=0, bg='#296d98', fg='white', activebackground='#296d98', activeforeground='white',padx=50, pady=1)
Signin_btn.place(x=880, y=90)

Travels=Label(root,text='Travels',font=('times new roman',14),bg='white',fg='black').place(x=120,y=150)
Radiobutton2 = Radiobutton(root, text="Super Kabeli Yatayat", variable=var, value=3, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=180)
Radiobutton2 = Radiobutton(root, text="Jam Jam Deluxe", variable=var, value=4, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=210)
Radiobutton2 = Radiobutton(root, text="Safari Yatayat", variable=var, value=5, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=240)
Radiobutton2 = Radiobutton(root, text="Banepa Super Deluxe", variable=var, value=6, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=270)


Bustype=Label(root,text='Bus Type',font=('times new roman',14),bg='white',fg='black').place(x=120,y=320)
Radiobutton2 = Radiobutton(root, text="AC", variable=var, value=7, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=350)
Radiobutton2 = Radiobutton(root, text="AC Deluxe", variable=var, value=8, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=380)
Radiobutton2 = Radiobutton(root, text="Deluxe", variable=var, value=9, command=lambda: print(var.get()))
Radiobutton2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Radiobutton2.place(x=120, y=410)

frame_back = Frame(root,bg='#3AAFA9', highlightbackground='WHITE', highlightthickness=2)
frame_back.place(anchor='center', relx=0.5, rely=0.5)

# # Create an object of tkinter ImageTk
# img = ImageTk.PhotoImage(Image.open("bus.png"))

# # Create a Label Widget to display the text or Image
# label = Label(frame_back, image = img)
# label.pack()
frame_back.place(x=120, y=70)
frame_back.pack_propagate(False)
frame_back.configure(height=500,width=900)



root.mainloop()

