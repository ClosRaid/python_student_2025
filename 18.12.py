import turtle
from tkinter.ttk import Combobox

import pygame
from tkinter import *

def clicked():
    lbl.configure(text=f"Привет, {txt.get()}")

window = Tk()
window.title("Добро пожаловтаь в моё приложение")
window.geometry("400x250")
lbl = Label(window,text='Введите имя', font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
btn = Button(window, text="Ввод!", bg="black", fg="white",state="disabled",
             command=clicked,)
btn.grid(column=1, row=1)
btn.grid(column=0, row=1)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
combo=Combobox(window)
combo['values'] = [1,2,3,4,5,6,7,8,9,0]
combo.current(0)
combo.grid(column=0, row=2)
chk = Checkbutton(window, text="Выбрать")
chk.grid(column=0, row=3)
rad1 = Radiobutton(window,text="Первый",value=1)
rad2 = Radiobutton(window,text="Второй",value=2)
rad3 = Radiobutton(window,text="Третий",value=3)
rad4 = Radiobutton(window,text="Четвёртый",value=4)
rad5 = Radiobutton(window,text="Пятый",value=5)
rad6 = Radiobutton(window,text="Шестой",value=6)
rad7 = Radiobutton(window,text="Седьмой",value=7)
rad8 = Radiobutton(window,text="Восьмой",value=8)
rad9 = Radiobutton(window,text="Девятая",value=9)
rad1.grid(column=0, row=4)
rad2.grid(column=0, row=5)
rad3.grid(column=0, row=6)
rad4.grid(column=0, row=7)
rad5.grid(column=0, row=8)
rad6.grid(column=0, row=9)
rad7.grid(column=0, row=10)
rad8.grid(column=0, row=11)
rad9.grid(column=0, row=12)



window.mainloop()

