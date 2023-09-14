import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x200')
# root.resizable(False,False)
root.title('Label Widget Image')

photo = tk.PhotoImage(file='./Instagram.png')
image_label = ttk.Label(root,image=photo, padding=5, text='Cat', compound='top')
image_label.pack()

root.mainloop()
