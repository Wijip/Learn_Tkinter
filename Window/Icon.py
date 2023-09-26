import tkinter as tk

#in Linux
root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('800x600')
root.resizable(False, False)
icon = tk.PhotoImage(file="fdm.png")
root.iconphoto(True, icon)

#in Windows
# root = tk.Tk()
# root.title('Tkinter Window Demo')
# root.geometry('800x600')
# root.resizable(False, False)
# root.iconbitmap('./fdm.png')

root.mainloop()
