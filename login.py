#===========importing required module==========
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

win = Tk()
#=========Title===========
win.title('Bus management system')

#======keeping icon=======
win.iconbitmap('icon.ico')

#======giving geometry of page==============
win.geometry('1199x600+100+50')
win.resizable(False,False)


#======adding backgroud image=========
image = Image.open('bus.png')
my_image = ImageTk.PhotoImage(image)
label = Label(win,image = my_image).place(x=0,y=0) 


#====adding Frame Login===
frame_login = Frame(win,bg='#E7E7E7')
frame_login.place(x=30,y=60,height=360,width=500)

#=====for title,label,entry inside frame=======
title=Label(frame_login,text='Login Here',font=('Montserrat',22),bg='#E7E7E7' ).place(x=180,y=30)
descript=Label(frame_login,text='Passengers Login Area',font=('Montserrat',17),bg='#E7E7E7').place(x=160,y=70)
Phone_number=Label(frame_login,text='Number',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=120)
textbox1= Entry(frame_login,font=('times new roman',15)).place(x=50,y=150)
password=Label(frame_login,text='Password',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=180)
textbox2= Entry(frame_login,font=('times new roman',15)).place(x=50,y=210)
forget_button= Button (frame_login,text='Forget password?',bg='#E7E7E7',bd=0,font=('times new roman',12)).place(x=50,y=240)
Login_button= Button (win,text='Login',bg='#22B100',font=('times new roman',11)).place(x=150,y=350,width=120,height=40)


#=========defining function============
def login_func():
    if password.get()=='' or Phone_number()=='':
        messagebox.showerror('Error','All fields are requied',parent=win)
    elif password.get()!='123456' or Phone_number()!='9810119909':
        messagebox.showerror('Error','Invalid phone number or password',parent=win)
    else:
        messagebox.showinfo('Welcome','succesfully logged in')

win.mainloop()