from tkinter import *

root = Tk()
root.geometry('600x600')
root.title ('How to buy ticket?')

def textii():
    text_open = open("tutorial.txt",'r')
    stuff = text_open.read()

    text_file.insert(END,stuff)
    text_open.close()


    
text_file = Text(root,width=80,height=20,font='arial')
text_file.pack(pady=20)

but = Button(root,text='How?',padx=10,pady=10 ,command=textii)
but.place(x=100,y=500)


root.mainloop()