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
# win.iconbitmap('buss.ico')



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

fullname_label=Label(frame_login,text='Full Name',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=110)
fullname= Entry(frame_login,font=('Montserrat',15))
fullname.place(x=150,y=110)

number_label=Label(frame_login,text='Number',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=160)
number= Entry(frame_login,font=('Montserrat',15))
number.place(x=150,y=160)

address_label=Label(frame_login,text='Address',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=210)
address= Entry(frame_login,font=('Montserrat',15))
address.place(x=150,y=210)

email_label=Label(frame_login,text='E-mail',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=260)
email= Entry(frame_login,font=('Montserrat',15))
email.place(x=150,y=260)

password_label=Label(frame_login,text='Password',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=310)
password= Entry(frame_login,font=('Montserrat',15))
password.place(x=150,y=310)

retype_label=Label(frame_login,text='Re-type',font=('Montserrat',14),bg='#E7E7E7').place(x=50,y=360)
retype= Entry(frame_login,font=('Montserrat',15))
retype.place(x=150,y=360)



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
        'Full_name':fullname.get(),
        'Number':number.get(),
        'Address':address.get(),
        'Email':email.get(),
        'password':password.get(),
        'retype_password':retype.get()
    })

    messagebox.showinfo("Registration Information","Account created Successfully")
    
    conn.commit()
    conn.close()

Signup_button= Button (win,text='Register',bg='#DC143C',command=submit,font=('Montserrat',11)).place(x=950,y=420,width=120,height=40)

# def query():
#     conn = sqlite3.connect('passenger_book.db')
#     c = conn.cursor()

#     c.execute("SELECT *,oid FROM registration")

#     records = c.fetchall()
#     print(records)

#     print_record=''
#     for record in records:
#         print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'
    
#     query_label = Label(win, text = print_record)
#     query_label.grid(row = 8, column=0, columnspan=2)

#     conn.commit()
#     conn.close()

def delete():
    conn = sqlite3.connect('passenger_book.db')
    c = conn.cursor()

    c.execute("DELETE from registration WHERE oid = " + delete_box.get())
    print('Deleted Successfully')

    # c.execute("SELECT *, oid FROM registration")

    # records = c.fetchall()
    # print(records)

    # print_record=''
    # for record in records:
    #     print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'
    
    # query_label = Label(win, text = print_record)
    # query_label.grid(row = 8, column=0, columnspan=2)

    conn.commit()
    conn.close()


def update():
    conn = sqlite3.connect('passenger_book.db')

    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE registration SET
         fullname = :full,
         number = :number,
         address = :address,
         email = :email,
         password = :password,
         retype = :retype
         WHERE oid = :oid""",
         {'fullname': fullname_editor.get(),
         'number': number_editor.get(),
         'address': address_editor.get(),
         'email': email_editor.get(),
         'password':password_editor.get(),
         'retype':retype_editor.get(),
         'oid': record_id
          }
    )
    conn.commit()
    conn.close()
    editor.destroy()

def edit():

    global editor

    editor =Tk()
    editor.title('Update Data')

    editor.geometry('300x400')
    conn = sqlite3.connect('passenger_book.db')

    c = conn.cursor()
    
    record_id = delete_box.get()

    c.execute("SELECT * FROM registration WHERE oid=" + record_id)

    records = c.fetchall()
    print(records)


    #====Createing global variable for all text boxes===
    global fullname_editor
    global number_editor
    global address_editor
    global email_editor
    global password_editor
    global retype_editor

#======Create text box=========
    fullname_editor = Entry(editor,width=30)
    fullname.grid(row=0, column=1, padx=20, pady=(10, 0))

    number_editor = Entry(editor,width=30)
    number_editor.grid(row=1,column=1)

    address_editor = Entry(editor,width=30)
    address_editor.grid(row=2, column=1)

    email_editor = Entry(editor,width=30)
    email_editor.grid(row=3, column=1)

    password_editor = Entry(editor,width=30)
    password_editor.grid(row=4, column=1)

    retype_editor = Entry(editor,width=30)
    retype_editor.grid(row=5, column=1)

  #====Create textbox labels======
    fullname_label = Label(editor, text='First Name')
    fullname_label.grid(row=0, column=0, pady=(10, 0))

    number_label = Label(editor, text='Number')
    number_label.grid(row=1, column=0)

    address_label = Label(editor, text='Address')
    address_label.grid(row=2, column=0)

    email_label = Label(editor, text='email')
    email_label.grid(row=3, column=0)

    password_label = Label(editor, text='password')
    password_label.grid(row=4, column=0)

    retype_label = Label(editor, text='Retype')
    retype_label.grid(row=5,column=0)

# delete_box = Entry(win, width = 30)
# delete_box.grid(row = 9, column = 1, pady = 5)


edit_btn = Button(win, text = "Update",command=edit,bg='#FFFF00',font=('Montserrat',11)).place(x=1150,y=520,width=120,height=40)


conn.commit()
conn.close()


win.mainloop()

