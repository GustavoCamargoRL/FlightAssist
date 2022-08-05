import tkinter
import customtkinter
x=0
y=0
z=0
r=0

pos = [x,y,z,r]

def x_slider(value):
    pos[0]=value

def y_slider(value):
    pos[1]=value

def r_slider(value):
    pos[2]=value

def z_slider(value):
    pos[3]=value

#def checkbox_event():
#    print("checkbox toggled, current value:", check_var.get())


init = customtkinter.CTk() 
slider_x = customtkinter.CTkSlider(master=init, from_=0, to=1430, command=x_slider)
slider_x.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
slider_y = customtkinter.CTkSlider(master=init, from_=0, to=713, command=y_slider)
slider_y.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
slider_z = customtkinter.CTkSlider(master=init, from_=0, to=12000, command=z_slider)
slider_z.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
slider_r = customtkinter.CTkSlider(master=init, from_=0, to=360, command=r_slider)
slider_r.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
print(pos)
check_var = tkinter.StringVar()

#checkbox = customtkinter.CTkCheckBox(master=init, text="CTkCheckBox", command=checkbox_event,
#                                     variable=check_var, onvalue="on", offvalue="off")
#checkbox.pack(padx=20, pady=10)

init.mainloop()