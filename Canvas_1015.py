import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')



canvas = tk.Canvas(window, bg = 'blue', height = 100, width = 200)

image_file = tk.PhotoImage(file='a.gif')
image = canvas.create_image(0,0, anchor = 'nw',image = image_file)
canvas.pack()


b = tk.Button(window,text='move',command = moveit).pack()

window.mainloop()
