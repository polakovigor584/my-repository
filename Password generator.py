from tkinter import *
from tkinter import messagebox
from random import *

def easy():
   len = int(lens.get())
   list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
   slt = ''
   s = shuffle(list)
   for i in range(len):
      a = list[i]
      a = str(a)
      slt += a
   messagebox.showinfo('Легкий пароль', f"Ваш пароль: {slt}")

def medium():
   lenw = int(lens.get())
   list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
   alf_m = ["q", "w", "e", 'r', "t", 'y', 'u', 'i', 'o', 'p', 'a', 's' , 'd' , 'f', 'g' , 'h' , 'j' ,'k' , 'l', 'z', 'x', 'c', 'v', 'b', 'n' , "m"]
   slt = ''
   shuffle(list) 
   shuffle(alf_m)
   for i in range(lenw):
      a = list[i]
      b = alf_m[i]
      a = str(a)
      b = str(b)
      slt += a
      slt += b
   messagebox.showinfo('Средний пароль', f'Ваш пароль: {slt[:lenw]}')

def hard():
   lenw = int(lens.get())
   list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
   alf_m = ["q", "w", "e", 'r', "t", 'y', 'u', 'i', 'o', 'p', 'a', 's' , 'd' , 'f', 'g' , 'h' , 'j' ,'k' , 'l', 'z', 'x', 'c', 'v', 'b', 'n' , "m"]
   specalf = ['@', '#', '_', '-', '@', '#', '_', '-', '@', '#']
   slt = ''
   shuffle(list) 
   shuffle(alf_m)
   shuffle(specalf)
   for i in range(lenw):
      a = list[i]
      b = alf_m[i]
      c = specalf[i]
      a = str(a)
      b = str(b)
      c = str(c)
      slt += a
      slt += b
      slt += c
   messagebox.showinfo('Сложный пароль', f'Ваш пароль: {slt[:lenw]}')

window = Tk()
window.title("Генератор паролей")
window.geometry('1500x400')

frame = Frame(
   window, 
   padx = 107.5,
   pady = 16 
)
frame.pack(expand=True)

txttxt = Label(
   frame,
   text="Генератор паролей"
)
txttxt.grid(row=1, column=2)

txttxt = Label(
   frame,
   text="Выберите сложность пароля:"
)
txttxt.grid(row=2, column=2)

txtxt = Label(
   frame,
   text=" "
)
txtxt.grid(row=3, column=2)

cal_btn = Button(
   frame, 
   text='Легкий', 
   command=easy
)
cal_btn.grid(row=5, column=1)

cal_btn1 = Button(
   frame, 
   text='Средний', 
   command=medium
)
cal_btn1.grid(row=5, column=2)

cal_btn2 = Button(
   frame, 
   text='Сложный',
   command=hard 
)
cal_btn2.grid(row=5, column=3)

inf = Label(
   frame,
   text="Использование цифр"
)
inf.grid(row=6, column=1)

inf1 = Label(
   frame,
   text="Использование цифр"
)
inf1.grid(row=6, column=2) 

inf1 = Label(
   frame,
   text="и строчных букв"
)
inf1.grid(row=7, column=2)

inf2 = Label(
   frame,
   text="Использование цифр,"
)
inf2.grid(row=6, column=3)

inf1 = Label(
   frame,
   text="строчных букв и"
)
inf1.grid(row=7, column=3)

inf1 = Label(
   frame,
   text="специальных символов"
)
inf1.grid(row=8, column=3)

inf1 = Label(
   frame,
   text="Чтобы получить пароль, вам нужно ввести кол-во символов и нажать на любую кнопку"
)
inf1.grid(row=10, column=2)

inf1 = Label(
   frame,
   text="Введите кол-во символов в пароле:"
)
inf1.grid(row=11, column=2)

lens = Entry(
   frame,
)
lens.grid(row=12, column=2, pady=5)

inf1 = Label(
   frame,
   text = "Примечание: Ограничение длины пароля 10 символов!"
)
inf1.grid(row=13, column=2)

window.mainloop()