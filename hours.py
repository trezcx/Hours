# Для начала импортируем все элементы из модуля

from  tkinter import *

from tkinter.ttk import *

# импорт модуля для преобразования кортежей через format
from  time import  strftime


# создание экземпляра класса Tk(), для отображенния окна приложения
root = Tk()
root.resizable(0, 0)
# добавление заголовка к окну
root.title('Часы')

# создание текстовой метки в окне прилржения, для отображения цифровых знаков. Цифры будут белыми на черном фоне
lable = Label(root, font=('aerial', 30), background='black', foreground='white')


# функция отображения времени
def time():
    string = strftime('%H:%M:%S %p')
    lable.config(text=string)
    lable.after(1000, time)


# азмещение метки времени по центру
lable.pack(anchor='center')
time()


# запуск цикла программы
mainloop()