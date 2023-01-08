
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
win = Tk()
win.title('Bus management system')
#keeping title name
win.iconbitmap('icon.ico')
#inserting icon
win.geometry('700x350')

image = Image.open('bus2.png')

my_image = ImageTk.PhotoImage(image)
label = Label(win,image = my_image).pack()

head = Label(win,text='Registration page')
head.pack(side='top')
body = Label(win,text='Welcome to siddhartha Bus travel',font='Rockwell 12').place(x=500,y=40)
#adding text in login page
Phone_Number = Label(win,text='Phone Number',bg='black',fg='white').place(x=100,y=100)
e1=Entry(win).place(x=200,y=100)
Password= Label(win,text='Password',bg='black',fg='white').place(x=100,y=150)
e2=Entry(win).place(x=200,y=150)

def click():
    a = messagebox.showinfo('congratulations','You are sucessfully logged in')

btn=Button(win,text='Login',command=click).place(x=150,y=230)

win.mainloop()