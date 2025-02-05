import tkinter
import os
from tkinter import filedialog

def file_select():
    filename=filedialog.askopenfilename(initialdir='/',title='Выберите файл',
                                        filetypes=(('Текстовый файл', '.txt'),('Все файлы','*')))
    text['text']=text['text']+' '+filename

window=tkinter.Tk()
window.title('Проводник')
window.geometry('350x250')
window.configure(bg='black')
window.resizable(False,False)
text = tkinter.Label(window,text='Файл', height=10, width=50, background='silver',fg='blue')
text.grid(column=1,row=1)
button_select=tkinter.Button(window, width=20, height=3, text='Выбрать файл',bg='silver',fg='blue',command=file_select)
button_select.grid(column=1, row=2)

window.mainloop()