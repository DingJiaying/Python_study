import tkinter as tk

window = tk.Tk()
window.title ('My window')
window.geometry('200x100')

l = tk.Label(window,text = 'OMG! This is TK!',bg = 'green',font = ('Arial',12),width=15,
             height=2)
l.pack()

b = tk.Botton(window,text='hit me')

window.mainloop()
