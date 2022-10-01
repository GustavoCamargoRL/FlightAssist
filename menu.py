from logging import raiseExceptions
from tkinter import *
from PIL import Image,ImageTk
from requests import get
import variables
import customtkinter
import gc
import threading


def thread_method():
    chooseMethod()


def choice():
    Thr.start()

Thr = threading.Thread(target=thread_method)


def swing():
    previous_state = [0,0,0,0,0,0]
    def getSwing():

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
    window.title('Criterion')
    distance = IntVar()
    length = IntVar()
    altitude = IntVar()
    wind = IntVar()
    urban = IntVar()
    support = IntVar()

    checkbox = Checkbutton(window,text='Distance',variable=distance,onvalue=1,offvalue=0,command=getSwing)
    checkbox.pack()
    checkbox.config(font=('Arial',20)) #changes the font
    checkbox.config(fg='#000000') #foreground color
    checkbox.config(bg='#FFFFFF') #background color
    checkbox.config(activeforeground='#000000') #active foreground color
    checkbox.config(activebackground='#FFFFFF') #active background color
    checkbox.config(padx=60,pady=10)
    checkbox.config(anchor='w') #anchors widget to relative cardinal direction

    checkbox2 = Checkbutton(window,text='Length',variable=length,onvalue=1,offvalue=0,command=getSwing)
    checkbox2.pack()
    checkbox2.config(font=('Arial',20)) #changes the font
    checkbox2.config(fg='#000000') #foreground color
    checkbox2.config(bg='#FFFFFF') #background color
    checkbox2.config(activeforeground='#000000') #active foreground color
    checkbox2.config(activebackground='#FFFFFF') #active background color
    checkbox2.config(padx=75,pady=10)
    checkbox2.config(anchor='w')

    checkbox3 = Checkbutton(window,text='Altitude',variable=altitude,onvalue=1,offvalue=0,command=getSwing)
    checkbox3.pack()
    checkbox3.config(font=('Arial',20)) #changes the font
    checkbox3.config(fg='#000000') #foreground color
    checkbox3.config(bg='#FFFFFF') #background color
    checkbox3.config(activeforeground='#000000') #active foreground color
    checkbox3.config(activebackground='#FFFFFF') #active background color
    checkbox3.config(padx=70,pady=10)
    checkbox3.config(anchor='w')

    checkbox4 = Checkbutton(window,text='Wind',variable=wind,onvalue=1,offvalue=0,command=getSwing)
    checkbox4.pack()
    checkbox4.config(font=('Arial',20)) #changes the font
    checkbox4.config(fg='#000000') #foreground color
    checkbox4.config(bg='#FFFFFF') #background color
    checkbox4.config(activeforeground='#000000') #active foreground color
    checkbox4.config(activebackground='#FFFFFF') #active background color
    checkbox4.config(padx=85,pady=10)
    checkbox4.config(anchor='w')

    checkbox5 = Checkbutton(window,text='Urban density',variable=urban,onvalue=1,offvalue=0,command=getSwing)
    checkbox5.pack()
    checkbox5.config(font=('Arial',20)) #changes the font
    checkbox5.config(fg='#000000') #foreground color
    checkbox5.config(bg='#FFFFFF') #background color
    checkbox5.config(activeforeground='#000000') #active foreground color
    checkbox5.config(activebackground='#FFFFFF') #active background color
    checkbox5.config(padx=25,pady=10)
    checkbox5.config(anchor='w')

    checkbox6 = Checkbutton(window,text='Support',variable=support,onvalue=1,offvalue=0,command=getSwing)
    checkbox6.pack()
    checkbox6.config(font=('Arial',20)) #changes the font
    checkbox6.config(fg='#000000') #foreground color
    checkbox6.config(bg='#FFFFFF') #background color
    checkbox6.config(activeforeground='#000000') #active foreground color
    checkbox6.config(activebackground='#FFFFFF') #active background color
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
    window.title('Methods')
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
    checkbox.config(padx=50,pady=10)
    checkbox.config(anchor='w') #anchors widget to relative cardinal direction

    checkbox2 = Checkbutton(window,text='SMARTER',variable=smarter,onvalue=1,offvalue=0,command=getMethod)
    checkbox2.pack()
    checkbox2.config(font=('Arial',20)) #changes the font
    checkbox2.config(fg='#000000') #foreground color
    checkbox2.config(bg='#FFFFFF') #background color
    checkbox2.config(activeforeground='#000000') #active foreground color
    checkbox2.config(activebackground='#FFFFFF') #active background color
    checkbox2.config(padx=35,pady=10)
    checkbox2.config(anchor='w')

    checkbox3 = Checkbutton(window,text='SMARTEST',variable=smartest,onvalue=1,offvalue=0,command=getMethod)
    checkbox3.pack()
    checkbox3.config(font=('Arial',20)) #changes the font
    checkbox3.config(fg='#000000') #foreground color
    checkbox3.config(bg='#FFFFFF') #background color
    checkbox3.config(activeforeground='#000000') #active foreground color
    checkbox3.config(activebackground='#FFFFFF') #active background color
    checkbox3.config(padx=25,pady=10)
    checkbox3.config(anchor='w')

    Button(window, text="Complete", command=window.destroy).pack()
    window.mainloop()
    return getMethod()

def init_weights():
    fields = 'Distance', 'Length', 'Altitude', 'Wind', 'Urban density', 'Support'
    def fetch(entries):
        j = 0
        for i in variables.rank:
            variables.weights_smarts[i] = int(entries[j][1].get())
            j += 1
        print(variables.weights_smarts) 

    def makeform(weigths, fields):
        entries = []
        print(variables.rank)
        for i in variables.rank:
            row = Frame(weigths)
            lab = Label(row, width=15, text=fields[i], anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((fields[i], ent))
        return entries

    weigths = Tk()
    weigths.title('Weigths')
    T = Text(weigths, height=5, width=43)
    T.pack()
    T.insert(END, "Please, insert the values for initial\nweights in each criterion.The criteria are in order of the elicitation.\nPress Save to record data.\nPress Complete when finished.")
    ents = makeform(weigths, fields)
    weigths.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = Button(weigths, text='Save', command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    Button(weigths, text="Complete", command=weigths.destroy).pack()
    weigths.mainloop()

def init_st():
    fields = 'Distance', 'Length', 'Altitude', 'Wind', 'Urban density', 'Support'
    def fetch(entries):
        for i in range(len(entries)):
            variables.st_smartest[i] = int(entries[i][1].get())
        print(variables.st_smartest) 

    def makeform(St, fields):
        entries = []
        for field in fields:
            row = Frame(St)
            lab = Label(row, width=15, text=field, anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((field, ent))
        return entries

    St = Tk()
    St.title('St')
    T = Text(St, height=5, width=50)
    T.pack()
    T.insert(END, "Please, insert the values for sensitivity\nthreshold in each criterion.It means the minimum value in that criteria that the initial weights are valid.\nPress Save to record data.\nPress Complete when finished.")
    ents = makeform(St, fields)
    St.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = Button(St, text='Save', command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    Button(St, text="Complete", command=St.destroy).pack()
    St.mainloop()


#test design 
def cust():
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
    

    init = customtkinter.CTk() 
    smarts = IntVar()
    smarter = IntVar()
    smartest = IntVar()
    close = IntVar()
    checkbox = customtkinter.CTkCheckBox(master=init, text="SMARTS", command=getMethod, variable=smarts, onvalue=1, offvalue=0)
    checkbox.pack(padx=20, pady=10)
    checkbox = customtkinter.CTkCheckBox(master=init, text="SMARTER", command=getMethod, variable=smarter, onvalue=1, offvalue=0)
    checkbox.pack(padx=20, pady=15)
    checkbox = customtkinter.CTkCheckBox(master=init, text="SMARTEST", command=getMethod, variable=smartest, onvalue=1, offvalue=0)
    checkbox.pack(padx=20, pady=20)
    checkbox = customtkinter.CTkCheckBox(master=init, text="Close", command=lambda: init.destroy(), variable=close, onvalue=1, offvalue=0)
    checkbox.pack(padx=20, pady=40)
    
    init.mainloop()
    init = None
    gc.collect()
    return None



