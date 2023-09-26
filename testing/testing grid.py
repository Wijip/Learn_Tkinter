import tkinter as tk

root = tk.Tk()
root.title("Contoh penggunaan grid layout")
root.geometry('300x200')
root.resizable(False, False)

label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
label3 = tk.Label(root, text="Label 3")
label4 = tk.Label(root, text="Label 4")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1, columnspan=2)

root.mainloop()
