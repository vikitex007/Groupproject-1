#===========importing required module=============#
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

win = Tk()
#=========Title===========#
win.title('Bus management system')

#======keeping icon=======
win.iconbitmap('buss.ico')

#======giving geometry of page==============#
win.geometry('1199x600+100+50')
win.resizable(False,False)


#======adding backgroud image=========#
image = Image.open('buss.png')
my_image = ImageTk.PhotoImage(image)
label = Label(win,image = my_image).place(x=0,y=0,relheight=1,relwidth=1) 


#====adding Frame Login===#
frame_login = Frame(win,bg='#90a8bd')
frame_login.place(x=450,y=80,height=360,width=500)

#=====for title,label,entry inside frame=======#
title=Label(frame_login,text='Login Here',font=('ariel',22,'bold'),bg='#90a8bd' ).place(x=180,y=30)
descript=Label(frame_login,text='Passengers Login Area',font=('Goudy old style',17,'bold'),bg='#90a8bd').place(x=160,y=70)

Phone_number=Label(frame_login,text='Number',font=('Goudy old style',14,'bold'),bg='#90a8bd').place(x=50,y=120)
textbox1= Entry(frame_login,font=('times new roman',15)).place(x=50,y=150)

password=Label(frame_login,text='Password',font=('Goudy old style',14,'bold'),bg='#90a8bd').place(x=50,y=180)
textbox2= Entry(frame_login,font=('times new roman',15),show='*').place(x=50,y=210)






#=========defining function============#
def login_func():
    if textbox1=='' or textbox2()=='':
        messagebox.showerror('Error','All fields are requied',parent=Tk)
    elif textbox2()!='123456' or textbox1!='9810119909':
        messagebox.showerror('Error','Invalid phone number or password',parent=Tk)
    else:
        messagebox.showinfo('Welcome','succesfully logged in')
        
Login_button= Button (win,text='Login',bg='#90a8bd',command=login_func,font=('times new roman',11)).place(x=650,y=420,width=120,height=40)

win.mainloop()



