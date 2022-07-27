from tkinter import *
from PIL import Image,ImageTk
import customtkinter


#window = Tk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def button_event():
    init.destroy()

init = customtkinter.CTk()   
init.title("Flight Assist")   
canvas = Canvas(init, width = 654, height = 574)      
canvas.pack()      
img = PhotoImage(file="intro.png")    
canvas.create_image(0,0, anchor=NW, image=img) 
button_1 = customtkinter.CTkButton(master=init, text="Start", width=80, height=30, command=button_event)
button_1.pack(pady=0,padx=0)
button_1.place(relx=0.5, rely=0.99, anchor="s")   
init.mainloop()



#window.mainloop()