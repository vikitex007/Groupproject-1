#===========importing required module==========
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3





#=========================FRONT     END =========================================#
win = Tk()
#=========Title===========
win.title('Bus management system')

#======keeping icon=======
win.iconbitmap('buss.ico')



#======giving geometry of page==============
win.geometry('1400x600+100+50')
win.resizable(False,False)


#======adding backgroud image=========
image = Image.open('buss.png')
my_image = ImageTk.PhotoImage(image)
label = Label(win,image = my_image).place(x=0,y=0) 



#====adding Frame Login===
frame_login = Frame(win,bg='#E7E7E7')
frame_login.place(x=800,y=0,height=600,width=500)

#=====for title,label,entry inside frame=======
title=Label(frame_login,text='Registration',font=('Montserrat',22),bg='#E7E7E7' ).place(x=180,y=30)

descript=Label(frame_login,text='Passengers Registration Area',font=('Montserrat',17),bg='#E7E7E7').place(x=120,y=70)

Full_name=Label(frame_login,text='Full Name',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=110)
Full_name1= Entry(frame_login,font=('Montserrat',15)).place(x=150,y=110)

Number=Label(frame_login,text='Number',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=160)
Number1= Entry(frame_login,font=('Montserrat',15)).place(x=150,y=160)

Address=Label(frame_login,text='Address',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=210)
Address1= Entry(frame_login,font=('Montserrat',15)).place(x=150,y=210)

Email=Label(frame_login,text='E-mail',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=260)
Email1= Entry(frame_login,font=('Montserrat',15)).place(x=150,y=260)

password=Label(frame_login,text='Password',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=310)
password1= Entry(frame_login,font=('Montserrat',15)).place(x=150,y=310)

retype_password=Label(frame_login,text='Re-type',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=360)
retype_password1= Entry(frame_login,font=('Montserrat',15)).place(x=150,y=360)



Already=Label(frame_login,text='Already Registered ?',font=('Montserrat',14),bg='#E7E7E7').place(x=130,y=480)

Regestration_button= Button (win,text='Login',bg='#22B100',font=('Montserrat',11)).place(x=950,y=520,width=120,height=40)






#=====================BACK       END====================
conn = sqlite3.connect('passenger_book.db')
c = conn.cursor()

# c.execute("""CREATE TABLE registration(
#     Full_name text,
#     Number integer,
#     Address text,
#     Email varchar,
#     password varchar,
#     retype_password varchar
# )""")
# print('Table created succesfully')

def submit():
    conn = sqlite3.connect('passenger_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO registration VALUES(:Full_name, :Number, :Address, :Email, :password, :retype_password)",{
        'Full_name':Full_name1.get(),
        'Number':Number1.get(),
        'Address':Address1.get(),
        'Email':Email1.get(),
        'password':password1.get(),
        'retype_password':retype_password1.get()

        
    })

    messagebox.showinfo("Registration Information","Account created Successfully")
    
    conn.commit()
    conn.close()

Signup_button= Button (win,text='Create Account',bg='#DC143C',command=submit,font=('Montserrat',11)).place(x=950,y=420,width=120,height=40)



conn.commit()
conn.close()


win.mainloop()

