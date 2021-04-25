import tkinter as tk  
from tkinter import *

Bg_color ="#6096BA"
Text_color ="#8B8C89"

Font= "HELVETICA 14"
nombre = ""
#configuracion de la ventana
window = tk.Tk()
window.title("Dulas: Menthal Health App")
window.configure(bg=Bg_color)

txt=Text(window)
txt.grid(row=0, column=0,columnspan=2)
resp = Entry(window,width=100)
resp.grid(row=1, column=0)

#texto de bienvendia
txt.insert(END,"\n"+"Dulas:Hola yo soy Dulas, estoy aquí para saber como te sientes")
txt.insert(END,"\n"+"Dulas:¿Cuál es tu nombre compeleto?")

def click(variable):
  send= "Yo:" + resp.get()
  variable = resp.get()
  txt.insert(END,"\n"+send)
  resp.delete(0,END)

send = Button(window, text= "Envíar", command = click(nombre), width=20).grid(row=1, column=1)

window.mainloop()