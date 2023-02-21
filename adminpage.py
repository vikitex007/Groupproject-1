from tkinter import *
import sqlite3
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.geometry("1920x1108")
root.title("Bus Management Service")



# top canvas
topcan=Canvas(root,height=80,width=1800,bg="#3AAFA9")
topcan.place(x=0,y=0)


#frame for widgets 
frame1=LabelFrame(root,width=1300,height=600,bg="white")
frame1.place(x=0,y=80)
logo=ImageTk.PhotoImage(Image.open("bus3.jpg"))
logo_label=Label(frame1,image=logo,bd=0,bg="white",width=300,height=180)
logo_label.place(x=800,y=5)



# #bottom black canvas
# bottomcan=Canvas(root,height=50,width=1800,bg="black")
# bottomcan.place(x=0,y=750)


#project title on black canvas
title1=Label(root,text="BUS",bg="#3AAFA9",fg=	"#F0F0F8",font=("Times", "24", "bold"))
title1.place(x=160,y=18)

title2=Label(root,text="MANAGEMENT",bg="#3AAFA9",fg="#F0F0F8",font=("Times", "24", "bold"))
title2.place(x=250,y=18)

title3=Label(root,text="SERVICE",bg="#3AAFA9",fg="#F0F0F8",font=("Times", "24", "bold"))
title3.place(x=520,y=18)

title4=Label(root,text="ADMIN'S PORTAL",bg="#3AAFA9",fg="#F0F0F8",font=("Times", "24", "bold"))
title4.place(x=800,y=18)


#Entering problem solved username
Labe1=Label(frame1,text=" Welcome to Admin portal",font=("Helvetica 15 bold"),bg="white")
Labe1.place(x=55,y=10)

#progress indicator
# blue=Label(frame1,bg="blue",text=" ",font=("Times", "14", "bold"),padx=10)
# blue.place(x=50,y=60)
blue_mean=Label(frame1,text=" Bon Voyage and Safe Travel",font=("Times", "14", "bold"),bg="white")
blue_mean.place(x=80,y=60)

# red=Label(frame1,text=" ",bg="red",font=("Times", "14", "bold"),padx=10)
# red.place(x=50,y=100)
red_mean=Label(frame1,text="Enjoy the journey and remember us again",font=("Times", "14", "bold"),bg="white")
red_mean.place(x=80,y=100)

# green=Label(frame1,text=" ",bg="green",font=("Times", "14", "bold"),padx=10)
# green.place(x=50,y=140)
green_mean=Label(frame1,text="Let this journey brings joy to your heart and peace to your mind,thank you! ",font=("Times", "14", "bold"),bg="white")
green_mean.place(x=80,y=140)


def refresh():
    root.destroy()
    

#refresh button
ref=Button(frame1,text="REFRESH",font=("Times", "14", "bold"),command=refresh)
ref.place(x=575,y=500)

#registered user label above its table
reg_us=Label(frame1,text="Bus List",font=("Times", "14", "bold"),fg="black",bg="white")
reg_us.place(x=840,y=190)



#table for booking
def tbl():
 
    table=LabelFrame(frame1,height=580,width=950,bg='white')
    table.place(x=30,y=220)
  
    try:
        #try fetching data from database
        conn=sqlite3.connect('passenger_registration.db')
        c=conn.cursor()
        c.execute("SELECT oid ,Full_name ,Number ,Address, Email from registration")
        lst=c.fetchall()
        conn.commit()
        conn.close()
    except:
        #empty list if list doesn't exist
        lst=[]
    finally:
        #Table headings
        lst.insert(0,('ID','first_name' ,'Number', 'Address', 'Email'))
        print(lst)
    #creating a table
    total_rows =len(lst)
    total_columns=len(lst[0])
    for i in range(total_rows):
        if i==0:
            #table heading
            fontt=("Times", "10", "bold")
            jus=CENTER
            bgc ='#9cc2e5'
        else:
            #table data
            fontt=("Times", "10", "bold")
            jus=LEFT
            bgc='white'
        for j in range(total_columns):
            #width for all columns
            if j==0:
                wid=5
            elif j==1 or j==2:
                wid=17
            elif j==3:
                wid=15
            elif j==4:
                wid=20
            elif j==5:
                wid=15
            elif j==6:
                wid=15
            elif j==7:
                wid=15
            elif j==8:
                wid=15
            else:
                wid=5
            e=Entry(
                table,
                width=wid,
                font=fontt,
                justify=jus,
                disabledforeground='black',
                disabledbackground=bgc
            )
            e.grid(row=i,column=j)
            e.insert(0,lst[i][j])
            e.config(state=DISABLED)
           

#calling table function
tbl()

#database for bus details

con=sqlite3.connect("bus.db")
cur=con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS bus_sts(
    busname text,
    bus_no integer,
    bus_type text,
    bus_dep integer,
    bus_ticket integer)""")
con.commit()
con.close()

#table for  bus database
def tbl3():
    table3=LabelFrame(frame1,height=580,width=650,bg='white')
    table3.place(x=580,y=220)

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

#calling table function
tbl3()


def editbook():
    sts=Toplevel()
    sts.geometry("200x200")
    label1=Label(sts,text="ENTER THE OID")
    label1.place(x=0,y=0)
    entry1=Entry(sts,font=("Helvetica 9 bold"))
    entry1.place(x=0,y=20)
    def del_rec():
        conn=sqlite3.connect("passenger_book.db")
        c=conn.cursor()
        c.execute("DELETE from registration WHERE oid = " + entry1.get())
        conn.commit()
        conn.close()
        messagebox.showinfo("sucess","deleted sucessfully!")
    btn1=Button(sts,text="DELETE",font=("Helvetica 9 bold"),bg="red",fg="white",command=del_rec)
    btn1.place(x=0,y=40)

edit_sts=Button(root,text="Edit book table",bg="green",fg="white",font=("Helvetica 9 bold"),command=editbook)
edit_sts.place(x=480,y=540)

def editbus():
    global rept
    rept=Toplevel()
    rept.geometry("200x200")
    label1=Label(rept,text="ENTER THE OID")
    label1.place(x=0,y=0)

    label1=Label(rept,text="ENTER THE OID")
    label1.place(x=0,y=0)
    entry1=Entry(rept,font=("Helvetica 9 bold"))
    entry1.place(x=0,y=20)

    label2=Label(rept,text="ENTER THE OID")
    label2.place(x=0,y=0)
    entry2=Entry(rept,font=("Helvetica 9 bold"))
    entry2.place(x=0,y=50)

    label3=Label(rept,text="ENTER THE OID")
    label3.place(x=0,y=0)
    entry3=Entry(rept,font=("Helvetica 9 bold"))
    entry3.place(x=0,y=80)

    label4=Label(rept,text="ENTER THE OID")
    label4.place(x=0,y=0)
    entry4=Entry(rept,font=("Helvetica 9 bold"))
    entry4.place(x=0,y=110)

    label5=Label(rept,text="ENTER THE OID")
    label5.place(x=0,y=0)
    entry5=Entry(rept,font=("Helvetica 9 bold"))
    entry5.place(x=0,y=140)

    label6=Label(rept,text="ENTER THE OID")
    label6.place(x=0,y=0)
    entry6=Entry(rept,font=("Helvetica 9 bold"))
    entry6.place(x=0,y=170)



    global del_rep
    def del_rep():
        conn=sqlite3.connect("bus.db")
        c=conn.cursor()
        c.execute("DELETE from bus_sts WHERE oid = " + entry1.get())
        conn.commit()
        conn.close()
        messagebox.showinfo("sucess","deleted sucessfully!")
    btn1=Button(rept,text="DELETE",font=("Helvetica 9 bold"),bg="red",fg="white",command=del_rep)
    btn1.place(x=0,y=100)

    global add
    def add():
            conn=sqlite3.connect('bus.db')
            c=conn.cursor()
            c.execute("INSERT INTO bus_sts VALUES( :busname, :busnum, :bustype, :busdep, :bustick )",{

                    'busname':entry2.get(),
                    'busnum':entry3.get(),
                    'bustype':entry4.get(),
                    'busdep':entry5.get(),
                    'bustick':entry6.get()
                   
                
                    })
            conn.commit()
            conn.close()
            messagebox.showinfo("Success",'account created Successfully!')
   
    btn2=Button(rept,text="INSERT",font=("Helvetica 9 bold"),bg="red",fg="white",command=add)
    btn2.place(x=200,y=100)

edit_repo=Button(root,text="Edit bus table",bg="green",fg="white",font=("Helvetica 9 bold"),command=editbus)
edit_repo.place(x=1110,y=540)


# #bottom black canvas
# bottomcan=Canvas(root,height=50,width=1800,bg="black")
# bottomcan.place(x=0,y=750)


#project title on black canvas
title1=Label(root,text="BUS",bg="#3AAFA9",fg=	"#F0F0F8",font=("Times", "24", "bold"))
title1.place(x=160,y=18)

title2=Label(root,text="MANAGEMENT",bg="#3AAFA9",fg="#F0F0F8",font=("Times", "24", "bold"))
title2.place(x=250,y=18)

title3=Label(root,text="SERVICE",bg="#3AAFA9",fg="#F0F0F8",font=("Times", "24", "bold"))
title3.place(x=520,y=18)

title4=Label(root,text="ADMIN'S PORTAL",bg="#3AAFA9",fg="#F0F0F8",font=("Times", "24", "bold"))
title4.place(x=800,y=18)


#Entering problem solved username
Labe1=Label(frame1,text=" Welcome to Admin portal",font=("Helvetica 15 bold"),bg="white")
Labe1.place(x=55,y=10)

#progress indicator
# blue=Label(frame1,bg="blue",text=" ",font=("Times", "14", "bold"),padx=10)
# blue.place(x=50,y=60)
blue_mean=Label(frame1,text=" Bon Voyage and Safe Travel",font=("Times", "14", "bold"),bg="white")
blue_mean.place(x=80,y=60)

# red=Label(frame1,text=" ",bg="red",font=("Times", "14", "bold"),padx=10)
# red.place(x=50,y=100)
red_mean=Label(frame1,text="Enjoy the journey and remember us again",font=("Times", "14", "bold"),bg="white")
red_mean.place(x=80,y=100)

# green=Label(frame1,text=" ",bg="green",font=("Times", "14", "bold"),padx=10)
# green.place(x=50,y=140)
green_mean=Label(frame1,text="Let this journey brings joy to your heart and peace to your mind,thank you! ",font=("Times", "14", "bold"),bg="white")
green_mean.place(x=80,y=140)


def refresh():
    root.destroy()
    

#refresh button
ref=Button(frame1,text="REFRESH",font=("Times", "14", "bold"),command=refresh)
ref.place(x=555,y=600)

#registered user label above its table
reg_us=Label(frame1,text="Bus List",font=("Times", "14", "bold"),fg="black",bg="white")
reg_us.place(x=840,y=190)



#table for booking
def tbl():
 
    table=LabelFrame(frame1,height=580,width=950,bg='white')
    table.place(x=30,y=220)
  
    try:
        #try fetching data from database
        conn=sqlite3.connect('passenger_registration.db')
        c=conn.cursor()
        c.execute("SELECT oid ,Full_name ,Number ,Address, Email from registration")
        lst=c.fetchall()
        conn.commit()
        conn.close()
    except:
        #empty list if list doesn't exist
        lst=[]
    finally:
        #Table headings
        lst.insert(0,('ID','first_name' ,'Number', 'Address', 'Email'))
        print(lst)
    #creating a table
    total_rows =len(lst)
    total_columns=len(lst[0])
    for i in range(total_rows):
        if i==0:
            #table heading
            fontt=("Times", "10", "bold")
            jus=CENTER
            bgc ='#9cc2e5'
        else:
            #table data
            fontt=("Times", "10", "bold")
            jus=LEFT
            bgc='white'
        for j in range(total_columns):
            #width for all columns
            if j==0:
                wid=5
            elif j==1 or j==2:
                wid=17
            elif j==3:
                wid=15
            elif j==4:
                wid=20
            elif j==5:
                wid=15
            elif j==6:
                wid=15
            elif j==7:
                wid=15
            elif j==8:
                wid=15
            else:
                wid=5
            e=Entry(
                table,
                width=wid,
                font=fontt,
                justify=jus,
                disabledforeground='black',
                disabledbackground=bgc
            )
            e.grid(row=i,column=j)
            e.insert(0,lst[i][j])
            e.config(state=DISABLED)
           

#calling table function
tbl()

#database for bus details

con=sqlite3.connect("bus.db")
cur=con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS bus_sts(
    busname text,
    bus_no integer,
    bus_type text,
    bus_dep integer,
    bus_ticket integer)""")
con.commit()
con.close()

#table for  bus database
def tbl3():
    table3=LabelFrame(frame1,height=580,width=650,bg='white')
    table3.place(x=580,y=220)

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

#calling table function
tbl3()


def editbook():
    sts=Toplevel()
    sts.geometry("200x200")
    label1=Label(sts,text="ENTER THE OID")
    label1.place(x=0,y=0)
    entry1=Entry(sts,font=("Helvetica 9 bold"))
    entry1.place(x=0,y=20)
    def del_rec():
        conn=sqlite3.connect("passenger_book.db")
        c=conn.cursor()
        c.execute("DELETE from registration WHERE oid = " + entry1.get())
        conn.commit()
        conn.close()
        messagebox.showinfo("sucess","deleted sucessfully!")
    btn1=Button(sts,text="DELETE",font=("Helvetica 9 bold"),bg="red",fg="white",command=del_rec)
    btn1.place(x=0,y=40)

edit_sts=Button(root,text="Edit book table",bg="green",fg="white",font=("Helvetica 9 bold"),command=editbook)
edit_sts.place(x=480,y=540)

def editbus():
    global rept
    rept=Toplevel()
    rept.geometry("200x200")
    label1=Label(rept,text="ENTER THE OID")
    label1.place(x=0,y=0)

    label1=Label(rept,text="ENTER THE OID")
    label1.place(x=0,y=0)
    entry1=Entry(rept,font=("Helvetica 9 bold"))
    entry1.place(x=0,y=20)

    label2=Label(rept,text="ENTER THE OID")
    label2.place(x=0,y=0)
    entry2=Entry(rept,font=("Helvetica 9 bold"))
    entry2.place(x=0,y=50)

    label3=Label(rept,text="ENTER THE OID")
    label3.place(x=0,y=0)
    entry3=Entry(rept,font=("Helvetica 9 bold"))
    entry3.place(x=0,y=80)

    label4=Label(rept,text="ENTER THE OID")
    label4.place(x=0,y=0)
    entry4=Entry(rept,font=("Helvetica 9 bold"))
    entry4.place(x=0,y=110)

    label5=Label(rept,text="ENTER THE OID")
    label5.place(x=0,y=0)
    entry5=Entry(rept,font=("Helvetica 9 bold"))
    entry5.place(x=0,y=140)

    label6=Label(rept,text="ENTER THE OID")
    label6.place(x=0,y=0)
    entry6=Entry(rept,font=("Helvetica 9 bold"))
    entry6.place(x=0,y=170)



    global del_rep
    def del_rep():
        conn=sqlite3.connect("bus.db")
        c=conn.cursor()
        c.execute("DELETE from bus_sts WHERE oid = " + entry1.get())
        conn.commit()
        conn.close()
        messagebox.showinfo("sucess","deleted sucessfully!")
    btn1=Button(rept,text="DELETE",font=("Helvetica 9 bold"),bg="red",fg="white",command=del_rep)
    btn1.place(x=0,y=100)

    global add
    def add():
            conn=sqlite3.connect('bus.db')
            c=conn.cursor()
            c.execute("INSERT INTO bus_sts VALUES( :busname, :busnum, :bustype, :busdep, :bustick )",{

                    'busname':entry2.get(),
                    'busnum':entry3.get(),
                    'bustype':entry4.get(),
                    'busdep':entry5.get(),
                    'bustick':entry6.get()
                   
                
                    })
            conn.commit()
            conn.close()
            messagebox.showinfo("Success",'account created Successfully!')
   
    btn2=Button(rept,text="INSERT",font=("Helvetica 9 bold"),bg="red",fg="white",command=add)
    btn2.place(x=200,y=100)

edit_repo=Button(root,text="Edit bus table",bg="green",fg="white",font=("Helvetica 9 bold"),command=editbus)
edit_repo.place(x=1110,y=540)




root.mainloop()

