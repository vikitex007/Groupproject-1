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

services = []

def showInfo():
    for i in range(len(services)):
        selected=""
        if services(i).get()>=1:
            selected += str(i)



for i in range(9):
    option = IntVar()
    option.set(0)
    services.append(option)
Travels=Label(root,text='Travels',font=('times new roman',14),bg='white',fg='black').place(x=120,y=150)
Checkbox1 = Checkbutton(root, text="Super Kabeli Yatayat", variable=services[0])
Checkbox1.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Checkbox1.place(x=120, y=180)
Checkbox2 = Checkbutton(root, text="Jam Jam Deluxe", variable=services[1])
Checkbox2.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Checkbox2.place(x=120, y=210)
Checkbox3 = Checkbutton(root, text="Safari Yatayat", variable=services[2])
Checkbox3.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Checkbox3.place(x=120, y=240)
Checkbox4 = Checkbutton(root, text="Banepa Super Deluxe", variable=services[3])
Checkbox4.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Checkbox4.place(x=120, y=270)



Bustype=Label(root,text='Bus Type',font=('times new roman',14),bg='white',fg='black').place(x=120,y=320)
Checkbox5 = Checkbutton(root, text="AC", variable=services[4])
Checkbox5.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Checkbox5.place(x=120, y=350)
Checkbox6 = Checkbutton(root, text="AC Deluxe", variable=services[5])
Checkbox6.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Checkbox6.place(x=120, y=380)
Checkbox7 = Checkbutton(root, text="Deluxe", variable=services[6])
Checkbox7.config(font=(6), bd=0, bg='white', fg='black', activebackground='white', activeforeground='white')
Checkbox7.place(x=120, y=410)

frame_back = Frame(root,bg='white', highlightbackground='WHITE', highlightthickness=2)
frame_back.place(anchor='center', relx=0.5, rely=0.5)

def tbl3():
    table3=LabelFrame(frame_back,height=580,width=650,bg='white')
    table3.place(x=0,y=0)

    try:
        #try fetching data from database
        conn=sqlite3.connect('bus.db')
        c=conn.cursor()
        c.execute("SELECT  oid, busname,bus_no,bus_type,bus_dep,bus_ticket from bus_sts")
        lst3=c.fetchall()
        conn.commit()
        conn.close()
    except:
        #empty list if list doesn't exist
        lst3=[]
    finally:
        #Table headings
        lst3.insert(0,('ID','bus name','Bus number' , 'Bus type' , 'bus departure', 'Ticket price'))
        print(lst3)
    #creating a table
    total_rows3 =len(lst3)
    total_columns3=len(lst3[0])
    for i in range(total_rows3):
        if i==0:
            #table heading
            fontt=('Arial',10,'bold')
            jus=CENTER
            bgc ='#9cc2e5'
        else:
            #table data
            fontt=('Arial',10)
            jus=LEFT
            bgc='white'
        for j in range(total_columns3):
            #width for all columns
            if j==0:
                wid=10
            elif j==1:
                wid=12
            elif j==2:
                wid=12
            elif j==3:
                wid=14
            elif j==4:
                wid=15
            elif j==5:
                wid=30
            elif j==6:
                wid=10
            elif j==7:
                wid=10
            elif j==8:
                wid=10
            else:
                wid=5
            f=Entry(
                table3,
                width=wid,
                font=fontt,
                justify=jus,
                disabledforeground='black',
                disabledbackground=bgc
            )
            f.grid(row=i,column=j)
            f.insert(0,lst3[i][j])
            f.config(state=DISABLED)

tbl3()
#calling table function
# # Create an object of tkinter ImageTk
# img = ImageTk.PhotoImage(Image.open("bus.png"))

# # Create a Label Widget to display the text or Image
# label = Label(frame_back, image = img)
# label.pack()
frame_back.place(x=150, y=60)
frame_back.pack_propagate(False)
frame_back.configure(height=500,width=900)



root.mainloop()

