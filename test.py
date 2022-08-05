from tkinter import *
from PIL import Image,ImageTk

def objectives():
    priority = [0,0,0,0,0]
    if(d1.get()==1):
        priority[0]=1
    elif(d2.get()==1):
        priority[0]=0
    if(l1.get()==1):
        priority[1]=1
    elif(l2.get()==1):
        priority[1]=0
    if(a1.get()==1):
        priority[2]=1
    elif(a2.get()==1):
        priority[2]=0
    if(w1.get()==1):
        priority[3]=1
    elif(w2.get()==1):
        priority[3]=0
    if(b1.get()==1):
        priority[4]=1
    elif(b2.get()==1):
        priority[4]=0
    return priority

window = Tk()

d1 = IntVar()
d2 = IntVar()
l1 = IntVar()
l2 = IntVar()
a1 = IntVar()
a2 = IntVar()
w1 = IntVar()
w2 = IntVar()
b1 = IntVar()
b2 = IntVar()
f = IntVar()


#Load an image in the script
#img= (Image.open("airplane.png"))

#Resize the Image using resize method
#resized_image= img.resize((50,50), Image.ANTIALIAS)
#new_image= ImageTk.PhotoImage(resized_image)


checkbox = Checkbutton(window,text='Max Distance',variable=d1,onvalue=1,offvalue=0,command=objectives)
checkbox.pack()
checkbox.config(font=('Arial',20)) #changes the font
checkbox.config(fg='#000000') #foreground color
checkbox.config(bg='#FFFFFF') #background color
checkbox.config(activeforeground='#000000') #active foreground color
checkbox.config(activebackground='#FFFFFF') #active background color
#photo = new_image
#checkbox.config(image=photo,compound='left') #sets image to photoimage
checkbox.config(padx=25,pady=10)
checkbox.config(anchor='w') #anchors widget to relative cardinal direction

checkbox2 = Checkbutton(window,text='Min Distance',variable=d2,onvalue=1,offvalue=0,command=objectives)
checkbox2.pack()
checkbox2.config(font=('Arial',20)) #changes the font
checkbox2.config(fg='#000000') #foreground color
checkbox2.config(bg='#FFFFFF') #background color
checkbox2.config(activeforeground='#000000') #active foreground color
checkbox2.config(activebackground='#FFFFFF') #active background color
#photo2 = PhotoImage(file='airplane2.png')
#checkbox2.config(image=photo2,compound='left') #sets image to photoimage
checkbox2.config(padx=25,pady=10)
checkbox2.config(anchor='w')

checkbox3 = Checkbutton(window,text='Max Lenght',variable=l1,onvalue=1,offvalue=0,command=objectives)
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

checkbox4 = Checkbutton(window,text='Min Lenght',variable=l2,onvalue=1,offvalue=0,command=objectives)
checkbox4.pack()
checkbox4.config(font=('Arial',20)) #changes the font
checkbox4.config(fg='#000000') #foreground color
checkbox4.config(bg='#FFFFFF') #background color
checkbox4.config(activeforeground='#000000') #active foreground color
checkbox4.config(activebackground='#FFFFFF') #active background color
#photo2 = PhotoImage(file='airplane2.png')
#checkbox2.config(image=photo2,compound='left') #sets image to photoimage
checkbox4.config(padx=25,pady=10)
checkbox4.config(anchor='w')

checkbox5 = Checkbutton(window,text='Max Altitude',variable=a1,onvalue=1,offvalue=0,command=objectives)
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

checkbox6 = Checkbutton(window,text='Min Altitude',variable=a2,onvalue=1,offvalue=0,command=objectives)
checkbox6.pack()
checkbox6.config(font=('Arial',20)) #changes the font
checkbox6.config(fg='#000000') #foreground color
checkbox6.config(bg='#FFFFFF') #background color
checkbox6.config(activeforeground='#000000') #active foreground color
checkbox6.config(activebackground='#FFFFFF') #active background color
#photo2 = PhotoImage(file='airplane2.png')
#checkbox2.config(image=photo2,compound='left') #sets image to photoimage
checkbox6.config(padx=25,pady=10)
checkbox6.config(anchor='w')

checkbox7 = Checkbutton(window,text='Wind in favor',variable=w1,onvalue=1,offvalue=0,command=objectives)
checkbox7.pack()
checkbox7.config(font=('Arial',20)) #changes the font
checkbox7.config(fg='#000000') #foreground color
checkbox7.config(bg='#FFFFFF') #background color
checkbox7.config(activeforeground='#000000') #active foreground color
checkbox7.config(activebackground='#FFFFFF') #active background color
#photo2 = PhotoImage(file='airplane2.png')
#checkbox2.config(image=photo2,compound='left') #sets image to photoimage
checkbox7.config(padx=25,pady=10)
checkbox7.config(anchor='w')

checkbox8 = Checkbutton(window,text='Against the wind',variable=w2,onvalue=1,offvalue=0,command=objectives)
checkbox8.pack()
checkbox8.config(font=('Arial',20)) #changes the font
checkbox8.config(fg='#000000') #foreground color
checkbox8.config(bg='#FFFFFF') #background color
checkbox8.config(activeforeground='#000000') #active foreground color
checkbox8.config(activebackground='#FFFFFF') #active background color
#photo2 = PhotoImage(file='airplane2.png')
#checkbox2.config(image=photo2,compound='left') #sets image to photoimage
checkbox8.config(padx=25,pady=10)
checkbox8.config(anchor='w')

checkbox9 = Checkbutton(window,text='Max building',variable=b1,onvalue=1,offvalue=0,command=objectives)
checkbox9.pack()
checkbox9.config(font=('Arial',20)) #changes the font
checkbox9.config(fg='#000000') #foreground color
checkbox9.config(bg='#FFFFFF') #background color
checkbox9.config(activeforeground='#000000') #active foreground color
checkbox9.config(activebackground='#FFFFFF') #active background color
#photo2 = PhotoImage(file='airplane2.png')
#checkbox2.config(image=photo2,compound='left') #sets image to photoimage
checkbox9.config(padx=25,pady=10)
checkbox9.config(anchor='w')

checkbox10 = Checkbutton(window,text='Min building',variable=b2,onvalue=1,offvalue=0,command=objectives)
checkbox10.pack()
checkbox10.config(font=('Arial',20)) #changes the font
checkbox10.config(fg='#000000') #foreground color
checkbox10.config(bg='#FFFFFF') #background color
checkbox10.config(activeforeground='#000000') #active foreground color
checkbox10.config(activebackground='#FFFFFF') #active background color
#photo2 = PhotoImage(file='airplane2.png')
#checkbox2.config(image=photo2,compound='left') #sets image to photoimage
checkbox10.config(padx=25,pady=10)
checkbox10.config(anchor='w')

Button(window, text="Complete", command=window.destroy).pack()

window.mainloop()