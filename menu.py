from tkinter import *
from PIL import Image,ImageTk
from requests import get
import variables

def elicitation():
    previous_state = [0,0,0,0,0,0]
    def getElicit():

        if(distance.get()==1 and previous_state[0]==0):
            variables.elicit[0]=1
            variables.rank.append(0)
            previous_state[0] = 1
            print(variables.rank)
        elif(distance.get()==0 and previous_state[0]==1):
            variables.elicit[0]=0
            variables.rank.remove(0)
            previous_state[0] = 0
            print(variables.rank)
        if(length.get()==1 and previous_state[1]==0):
            variables.elicit[1]=1
            variables.rank.append(1)
            previous_state[1] = 1
            print(variables.rank)
        elif(length.get()==0 and previous_state[1]==1):
            variables.elicit[1]=0
            variables.rank.remove(1)
            previous_state[1] = 0
            print(variables.rank)
        if(altitude.get()==1 and previous_state[2]==0):
            variables.elicit[2]=1
            variables.rank.append(2)
            previous_state[2] = 1
            print(variables.rank)
        elif(altitude.get()==0 and previous_state[2]==1):
            variables.elicit[2]=0
            variables.rank.remove(2)
            previous_state[2] = 0
            print(variables.rank)
        if(wind.get()==1 and previous_state[3]==0):
            variables.elicit[3]=1
            variables.rank.append(3)
            previous_state[3] = 1
            print(variables.rank)
        elif(wind.get()==0 and previous_state[3]==1):
            variables.elicit[3]=0
            variables.rank.remove(3)
            previous_state[3] = 0
            print(variables.rank)
        if(urban.get()==1 and previous_state[4]==0):
            variables.elicit[4]=1
            variables.rank.append(4)
            previous_state[4] = 1
            print(variables.rank)
        elif(urban.get()==0 and previous_state[4]==1):
            variables.elicit[4]=0
            variables.rank.remove(4)
            previous_state[4] = 0
            print(variables.rank)
        if(support.get()==1 and previous_state[5]==0):
            variables.elicit[5]=1
            variables.rank.append(5)
            previous_state[5] = 1
            print(variables.rank)
        elif(support.get()==0 and previous_state[5]==1):
            variables.elicit[5]=0
            variables.rank.remove(5)
            previous_state[5] = 0
            print(variables.rank)

    window = Tk()
    distance = IntVar()
    length = IntVar()
    altitude = IntVar()
    wind = IntVar()
    urban = IntVar()
    support = IntVar()

    checkbox = Checkbutton(window,text='Distance',variable=distance,onvalue=1,offvalue=0,command=getElicit)
    checkbox.pack()
    checkbox.config(font=('Arial',20)) #changes the font
    checkbox.config(fg='#000000') #foreground color
    checkbox.config(bg='#FFFFFF') #background color
    checkbox.config(activeforeground='#000000') #active foreground color
    checkbox.config(activebackground='#FFFFFF') #active background color
    #photo = new_image
    #checkbox.config(image=photo,compound='left') #sets image to photoimage
    checkbox.config(padx=60,pady=10)
    checkbox.config(anchor='w') #anchors widget to relative cardinal direction

    checkbox2 = Checkbutton(window,text='Length',variable=length,onvalue=1,offvalue=0,command=getElicit)
    checkbox2.pack()
    checkbox2.config(font=('Arial',20)) #changes the font
    checkbox2.config(fg='#000000') #foreground color
    checkbox2.config(bg='#FFFFFF') #background color
    checkbox2.config(activeforeground='#000000') #active foreground color
    checkbox2.config(activebackground='#FFFFFF') #active background color
    #photo2 = PhotoImage(file='airplane2.png')
    #checkbox2.config(image=photo2,compound='left') #sets image to photoimage
    checkbox2.config(padx=75,pady=10)
    checkbox2.config(anchor='w')

    checkbox3 = Checkbutton(window,text='Altitude',variable=altitude,onvalue=1,offvalue=0,command=getElicit)
    checkbox3.pack()
    checkbox3.config(font=('Arial',20)) #changes the font
    checkbox3.config(fg='#000000') #foreground color
    checkbox3.config(bg='#FFFFFF') #background color
    checkbox3.config(activeforeground='#000000') #active foreground color
    checkbox3.config(activebackground='#FFFFFF') #active background color
    #photo2 = PhotoImage(file='airplane2.png')
    #checkbox2.config(image=photo2,compound='left') #sets image to photoimage
    checkbox3.config(padx=70,pady=10)
    checkbox3.config(anchor='w')

    checkbox4 = Checkbutton(window,text='Wind',variable=wind,onvalue=1,offvalue=0,command=getElicit)
    checkbox4.pack()
    checkbox4.config(font=('Arial',20)) #changes the font
    checkbox4.config(fg='#000000') #foreground color
    checkbox4.config(bg='#FFFFFF') #background color
    checkbox4.config(activeforeground='#000000') #active foreground color
    checkbox4.config(activebackground='#FFFFFF') #active background color
    #photo2 = PhotoImage(file='airplane2.png')
    #checkbox2.config(image=photo2,compound='left') #sets image to photoimage
    checkbox4.config(padx=85,pady=10)
    checkbox4.config(anchor='w')

    checkbox5 = Checkbutton(window,text='Urban density',variable=urban,onvalue=1,offvalue=0,command=getElicit)
    checkbox5.pack()
    checkbox5.config(font=('Arial',20)) #changes the font
    checkbox5.config(fg='#000000') #foreground color
    checkbox5.config(bg='#FFFFFF') #background color
    checkbox5.config(activeforeground='#000000') #active foreground color
    checkbox5.config(activebackground='#FFFFFF') #active background color
    #photo2 = PhotoImage(file='airplane2.png')
    #checkbox2.config(image=photo2,compound='left') #sets image to photoimage
    checkbox5.config(padx=25,pady=10)
    checkbox5.config(anchor='w')

    checkbox6 = Checkbutton(window,text='Support',variable=support,onvalue=1,offvalue=0,command=getElicit)
    checkbox6.pack()
    checkbox6.config(font=('Arial',20)) #changes the font
    checkbox6.config(fg='#000000') #foreground color
    checkbox6.config(bg='#FFFFFF') #background color
    checkbox6.config(activeforeground='#000000') #active foreground color
    checkbox6.config(activebackground='#FFFFFF') #active background color
    #photo2 = PhotoImage(file='airplane2.png')
    #checkbox2.config(image=photo2,compound='left') #sets image to photoimage
    checkbox6.config(padx=65,pady=10)
    checkbox6.config(anchor='w')

    Button(window, text="Complete", command=window.destroy).pack()
    window.mainloop()
    return True

def chooseMethod():
    def getMethod():

        if(smarts.get()==1):
            variables.activate[0]=1
        elif(smarts.get()==0):
            variables.activate[0]=0
        if(smarter.get()==1):
            variables.activate[1]=1
        elif(smarter.get()==0):
            variables.activate[1]=0
        if(smartest.get()==1):
            variables.activate[2]=1
        elif(smartest.get()==0):
            variables.activate[2]=0

    window = Tk()
    smarts = IntVar()
    smarter = IntVar()
    smartest = IntVar()

    checkbox = Checkbutton(window,text='SMARTS',variable=smarts,onvalue=1,offvalue=0,command=getMethod)
    checkbox.pack()
    checkbox.config(font=('Arial',20)) #changes the font
    checkbox.config(fg='#000000') #foreground color
    checkbox.config(bg='#FFFFFF') #background color
    checkbox.config(activeforeground='#000000') #active foreground color
    checkbox.config(activebackground='#FFFFFF') #active background color
    #photo = new_image
    #checkbox.config(image=photo,compound='left') #sets image to photoimage
    checkbox.config(padx=50,pady=10)
    checkbox.config(anchor='w') #anchors widget to relative cardinal direction

    checkbox2 = Checkbutton(window,text='SMARTER',variable=smarter,onvalue=1,offvalue=0,command=getMethod)
    checkbox2.pack()
    checkbox2.config(font=('Arial',20)) #changes the font
    checkbox2.config(fg='#000000') #foreground color
    checkbox2.config(bg='#FFFFFF') #background color
    checkbox2.config(activeforeground='#000000') #active foreground color
    checkbox2.config(activebackground='#FFFFFF') #active background color
    #photo2 = PhotoImage(file='airplane2.png')
    #checkbox2.config(image=photo2,compound='left') #sets image to photoimage
    checkbox2.config(padx=35,pady=10)
    checkbox2.config(anchor='w')

    checkbox3 = Checkbutton(window,text='SMARTEST',variable=smartest,onvalue=1,offvalue=0,command=getMethod)
    checkbox3.pack()
    checkbox3.config(font=('Arial',20)) #changes the font
    checkbox3.config(fg='#000000') #foreground color
    checkbox3.config(bg='#FFFFFF') #background color
    checkbox3.config(activeforeground='#000000') #active foreground color
    checkbox3.config(activebackground='#FFFFFF') #active background color
    #photo2 = PhotoImage(file='airplane2.png')
    #checkbox2.config(image=photo2,compound='left') #sets image to photoimage
    checkbox3.config(padx=25,pady=10)
    checkbox3.config(anchor='w')

    Button(window, text="Complete", command=window.destroy).pack()
    window.mainloop()
    return getMethod()

