from pyautogui import moveTo
from time import sleep
from datetime import datetime
from random import randint
from tkinter import *


def main():
    viewInfo()
    Clicker()

def viewInfo():
    label["text"] = f'Скрипт запущен на {time_ent.get()} сек.'

def Clicker():
    timer = int(time_ent.get())    
    try:
        while timer > 0:
            x, y, = randint(1, 1000), randint(1, 1000)
            moveTo(x, y, duration=2)
            timer -= 1
    except KeyboardInterrupt:
        print(f'Скрипт завершен в {datetime.now().strftime("%H:%M - %d.%m.%Y")}')


window = Tk()
window.title('Clicker 1.0')
window.geometry()
window.resizable(False, False)
frame = Frame(
    window,
    padx = 10,
    pady = 10,
)
time_lb = Label(
    frame,
    text = 'Задайте время, на которое необходимо запустить движение мыши.'
)
time_lb.grid(row = 1, column = 1)

time_ent = Entry(
    frame,
    background = '#FFFF00',
    width = 10,
    cursor = 'hand2',
    textvariable = IntVar(value='')
)

time_ent.grid(row = 1, column = 2)

time_btn = Button(
    frame,
    text = 'Ок',
    command = main
)

time_btn.grid(row = 1, column = 3)

label = Label(
    frame,

    foreground = '#FF0000',
)

label.grid(row = 2, column = 1) 

frame.pack(expand = True)
window.mainloop()
