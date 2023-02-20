#===========importing required module==========
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter.messagebox as tkMessagebox
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
image = Image.open('bussss.png')
my_image = ImageTk.PhotoImage(image)
label = Label(win,image = my_image).place(x=-200,y=-130) 



#====adding Frame Login===
frame_login = Frame(win,bg='#E7E7E7')
frame_login.place(x=800,y=0,height=600,width=500)

#=====for title,label,entry inside frame=======
title=Label(frame_login,text='Registration',font=('Montserrat',22),bg='#E7E7E7' ).place(x=180,y=30)

descript=Label(frame_login,text='Passengers Registration Area',font=('Montserrat',17),bg='#E7E7E7').place(x=120,y=70)

Full_name_label=Label(frame_login,text='Full Name',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=110)
full_name= Entry(frame_login,font=('Montserrat',15))
full_name.place(x=150,y=110)

Number_label=Label(frame_login,text='Number',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=160)
Number= Entry(frame_login,font=('Montserrat',15))
Number.place(x=150,y=160)

Address_label=Label(frame_login,text='Address',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=210)
Address= Entry(frame_login,font=('Montserrat',15))
Address.place(x=150,y=210)

Email_label=Label(frame_login,text='E-mail',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=260)
Email= Entry(frame_login,font=('Montserrat',15))
Email.place(x=150,y=260)

password_label=Label(frame_login,text='Password',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=310)
password= Entry(frame_login,font=('Montserrat',15))
password.place(x=150,y=310)

retype_password_label=Label(frame_login,text='Re-type',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=360)
retype_password= Entry(frame_login,font=('Montserrat',15))
retype_password.place(x=150,y=360)

# delete=Label(frame_login,text='Delete',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=390)
# delete_q= Entry(frame_login,font=('Montserrat',15))
# delete_q.place(x=150,y=390)

# def delete_func():
#     conn = sqlite3.connect('passenger_registration.db')
#     c = conn.cursor()

#     c.execute('DELETE from registration WHERE oid ='+ delete_q.get())
#     messagebox.showinfo('info','data deleted successfully')
#     c.execute('SELECT *,oid FROM registration')
#     record =c.fetchall()

#     print(record)
#     conn.commit()
#     conn.close()

# delete_button= Button (win,text='delete',bg='#22B100',command=delete_func,font=('Montserrat',11)).place(x=1000,y=550,width=120,height=40)


       
 


Already=Label(frame_login,text='Already Registered ?',font=('Montserrat',14),bg='#E7E7E7').place(x=130,y=480)

def log():
    import login
    """
    This function  calls the login page
    
    """



Login_button= Button (win,text='Login',bg='#22B100',command=log,font=('Montserrat',11)).place(x=950,y=520,width=120,height=40)






#=====================BACK       END====================
def Database():
    """It is the function defined for database
    Here Table named registration is created 
    """
    global c,conn
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
    # conn.commit()
    # conn.close()

def submit():
    """This function is used in the registration button.
    If all the entry are not filled then error will shown.
    Elif password and retype password didnt matched then the error will be shown.
    And if all the data are correct then data will be saved in database 
    """

    
    
    Database()
    conn = sqlite3.connect('passenger_book.db')
    if full_name.get() =="" or Number.get() =="" or Address.get()=="" or Email.get()=="" or password.get() =="" or retype_password.get()=="":
        messagebox.showerror("Error",'Please fill all the details')
    
    elif password.get() != retype_password.get():
        messagebox.showerror('Error','password not matched')
        
    

    else: 
        conn = sqlite3.connect('passenger_registration.db')
        c = conn.cursor()
        c.execute("INSERT INTO registration VALUES(:Full_name, :Number, :Address, :Email, :password, :retype_password)",{
        'Full_name':full_name.get(),
        'Number':Number.get(),
        'Address':Address.get(),
        'Email':Email.get(),
        'password':password.get(),
        'retype_password':retype_password.get()
        })
            


        messagebox.showinfo("Registration Information","Information Registered Successfully")
    
    conn.commit()
    conn.close()

Signup_button= Button (win,text='Register',bg='#DC143C',command=submit,font=('Montserrat',11))
Signup_button.place(x=950,y=420,width=120,height=40)









win.mainloop()

