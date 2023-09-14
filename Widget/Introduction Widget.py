import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x200')
root.resizable(False, False)

tk.Label(root, text='Classic Label').pack()
"""
tk.Label(root, text='Classic Label').pack() -> pada kode ini dapat membuat
sebuah objek label menggunakan kelas Label dari modul tkinter. objek ini
memiliki teks Classic Label. root merupakan jendela utama tempat label
akan ditempatkan dan kemudian anda menggunakan metode .pack() untuk 
menempatkan label ke dalam jendela .pack(). metode .pack() digunakan untuk mengatur
tata letak elemen-elemen GUI dalam jendela. ini akan menempatkan label
dalam jendela dengan tata letak default
"""
ttk.Label(root, text='Themed Label').pack()
"""
ttk.Label(root, text='Themed Label').pack() -> pada baris kode ini, dapat
membuat objek label yang sama dengan teks Themed Label. tetapi menggunakan
modul ttk (Themed Tkinter) dengan kelas Label. seperti sebelumnya fungsi ini dapat
menggunakan metode .pack() untuk menempatkan Label ini didalam jendela
"""

"""
dari kedua kode program tersebut memiliki perbedaan yaitu pada visualnya.
Label yang dibuat menggunakan module ttk (Themed Tkinter) cenderung
memiliki tampilan yang lebih moderen dan lebih konsisten dengan tema GUI
pada sistem operasi, sementara label dari modul Tkinter memiliki tampilan
yang lebih klasik atau standar
"""

root.mainloop()
