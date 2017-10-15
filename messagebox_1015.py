import tkinter as tk
from tkinter import messageox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    tk.messagebox.showinfo(title='Hi',message='hahahaha')
    

tk.Button(window, text='hit me', command= hit_me).pack()

window.mainloop()
