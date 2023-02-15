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
# image = Image.open('bus.png')
# my_image = ImageTk.PhotoImage(image)
# label = Label(win,image = my_image)
# label.place(x=0,y=0,relheight=1,relwidth=1) 

#=====================defining login function=============================================


    
#====adding Frame Login===#
frame_login = Frame(win,bg='white')
frame_login.place(x=600,y=60,height=450,width=400)

#=====for title,label,entry inside frame=======#
# title=Label(frame_login,text='Hello',font=('Alegreya',22,'bold'),bg='white' ).place(x=125,y=30)
descript=Label(frame_login,text='Welcome to our login page',font=('Alegreya',17),bg='white')
descript.place(x=60,y=40)

Phone_number=Label(frame_login,text='Number',font=('Goudy old style',14,'bold'),bg='white')
Phone_number.place(x=140,y=120)
textbox1= Entry(frame_login,font=('times new roman',15))
textbox1.place(x=90,y=150)

password=Label(frame_login,text='Password',font=('Goudy old style',14,'bold'),bg='white')
password.place(x=140,y=180)
textbox2= Entry(frame_login,font=('times new roman',15),show='*')
textbox2.place(x=90,y=210)

check = Checkbutton(frame_login,text='Remember details?',bg='white')
check.place(x=90,y=240)
    
or_b = Label(frame_login,text="Don't have account?",bg = 'white',font =('Goudy old style',12,'bold') )
or_b.place(x=90,y=320)

def reg():
    import registration

signup_button= Button (frame_login,text='Sign Up',command=reg,bg='white',font=('italic',11))
signup_button.place(x=90,y=350,width=120,height=40)

    


win.mainloop()



