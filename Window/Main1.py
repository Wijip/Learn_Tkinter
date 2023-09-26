import tkinter as tk

root = tk.Tk()

root.title('Icon Example ')
icon = tk.PhotoImage(file='fdm.png')
root.iconphoto(False, icon)

root.mainloop()
