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
image = Image.open('bus.png')
my_image = ImageTk.PhotoImage(image)
label = Label(win,image = my_image).place(x=0,y=0,relheight=1,relwidth=1) 


#====adding Frame Login===#
frame_login = Frame(win,bg='white')
frame_login.place(x=600,y=60,height=450,width=400)

#=====for title,label,entry inside frame=======#
# title=Label(frame_login,text='Hello',font=('Alegreya',22,'bold'),bg='white' ).place(x=125,y=30)
descript=Label(frame_login,text='Welcome to our login page',font=('Alegreya',17),bg='white').place(x=60,y=40)

Phone_number=Label(frame_login,text='Number',font=('Goudy old style',14,'bold'),bg='white').place(x=140,y=120)
textbox1= Entry(frame_login,font=('times new roman',15)).place(x=90,y=150)

password=Label(frame_login,text='Password',font=('Goudy old style',14,'bold'),bg='white').place(x=140,y=180)
textbox2= Entry(frame_login,font=('times new roman',15),show='*').place(x=90,y=210)

check = Checkbutton(frame_login,text='Remember details?',bg='white').place(x=90,y=240)
 
or_b = Label(frame_login,text="Don't have account?",bg = 'white',font =('Goudy old style',12,'bold') ).place(x=90,y=320)

signup_button= Button (frame_login,text='Sign Up',bg='white',font=('italic',11)).place(x=230,y=320,width=120,height=0)

#=========defining function============#
def login_func():
    if textbox1=='' or textbox2()=='':
        messagebox.showerror('Error','All fields are requied',parent=win)
    elif textbox2()!='123456' or textbox1!='9810119909':
        messagebox.showerror('Error','Invalid phone number or password',parent=win)
    else:
        messagebox.showinfo('Welcome','succesfully logged in')
    return()
        
Login_button= Button (frame_login,text='Login',bg='white',command=login_func,font=('italic',11)).place(x=90,y=270,width=120,height=40)

win.mainloop()



