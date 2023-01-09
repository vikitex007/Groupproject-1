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
win.geometry('1400x700+100+50')
win.resizable(False,False)


#======adding backgroud image=========
image = Image.open('bus.png')
my_image = ImageTk.PhotoImage(image)
label = Label(win,image = my_image).place(x=0,y=0) 



#====adding Frame Login===
frame_login = Frame(win,bg='#E7E7E7')
frame_login.place(x=30,y=80,height=600,width=500)

#=====for title,label,entry inside frame=======
title=Label(frame_login,text='Registration',font=('Montserrat',22),bg='#E7E7E7' ).place(x=180,y=30)
descript=Label(frame_login,text='Passengers Registration Area',font=('Montserrat',17),bg='#E7E7E7').place(x=160,y=70)
Full_name=Label(frame_login,text='Full Name',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=110)
textbox1= Entry(frame_login,font=('Montserrat',15)).place(x=150,y=110)
number=Label(frame_login,text='Number',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=160)
textbox1= Entry(frame_login,font=('Montserrat',15)).place(x=150,y=160)
Address=Label(frame_login,text='Address',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=210)
textbox1= Entry(frame_login,font=('Montserrat',15)).place(x=150,y=210)
E_mail=Label(frame_login,text='E-mail',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=260)
textbox1= Entry(frame_login,font=('Montserrat',15)).place(x=150,y=260)
Password=Label(frame_login,text='Password',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=310)
textbox1= Entry(frame_login,font=('Montserrat',15)).place(x=150,y=310)
Re_type=Label(frame_login,text='Re-type',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=360)
textbox2= Entry(frame_login,font=('Montserrat',15)).place(x=150,y=360)
Signup_button= Button (win,text='Create Account',bg='#DC143C',font=('Montserrat',11)).place(x=140,y=500,width=120,height=40)
Already=Label(frame_login,text='Already Registered ?',font=('Montserrat',14),bg='#E7E7E7').place(x=130,y=480)
Regestration_button= Button (win,text='Login',bg='#22B100',font=('Montserrat',11)).place(x=180,y=600,width=120,height=40)


#=========defining function============
def login_func():
    if Password.get()=='' :
        messagebox.showerror('Error','All fields are requied',parent=win)
    elif Password.get()!='123456' :
        messagebox.showerror('Error','Invalid phone number or password',parent=win)
    else:
        messagebox.showinfo('Welcome','succesfully logged in')

win.mainloop()


