from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root=Tk()
root.title("Drawing Shapes on Canvas")
root.geometry("750x750")

canvas=Canvas(root, width = 990, height=490, bg = "white", highlightbackground="Lightgray")
canvas.pack()

label = Label(root, text = "Choose Colour")
label.place(relx=0.6,rely=0.9,anchor=CENTER)

fillcolour = ["red","green","blue","yellow"]

dropdown = ttk.Combobox(root, values = fillcolour,width = 10)
dropdown.place(relx=0.8,rely=0.9)

label_startx = Label(root,text = "Start X")
label_startx.place(relx = 0.1, rely = 0.85)
coordinates_values = [10,50,100,200,300,400,500,600,700,800,900]

dropdown2 = ttk.Combobox(root,values = coordinates_values,width = 10)
dropdown2.place(relx = 0.2,rely = 0.85)

label_starty = Label(root,text = "Start Y")
label_starty.place(relx = 0.3,rely = 0.85)

dropdown3 = ttk.Combobox(root, values = coordinates_values,width = 10)
dropdown3.place(relx = 0.4,rely=0.85)

label_endx = Label(root,text = "End X")
label_endx.place(relx = 0.5,rely = 0.85)

dropdown4 = ttk.Combobox(root,values = coordinates_values,width = 10)
dropdown4.place(relx=0.6,rely=0.85)

label_endy = Label(root,text = "End Y")
label_endy.place(relx = 0.7,rely = 0.85)

dropdown5 = ttk.Combobox(root,values = coordinates_values, width = 10)
dropdown5.place(relx = 0.8,rely=0.85)

root.mainloop()