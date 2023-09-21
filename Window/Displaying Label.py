import tkinter as tk

root = tk.Tk()

message = tk.Label(root, text="Hello World!")
"""
kode message = tk.Label(root, text="Hello World!") -> pada baris ini,
kita membuat objek Label dari modul tkinter. Objek ini akan digunakan
untuk menampilkan text atau gambar pada antarmuka grafis. 
parameter 'root' adalah jendela utama(main window) tempat Label akan
ditampilkan. 'text' adalah parameter yang digunakan untuk mengatur teks
yang akan ditampilkan dalam Label. pada kode ini teks yang ditampilkan 
adalah Hello World!
"""
message.pack()
"""
kode message.pack() -> pada baris ini, kita menggunakan metode pack()
untuk menempatkan objek Label di dalam jendela utama (root). metode
pack() merupakah salah satu cara untuk mengatur tata letak layout atau
elemen-elemen GUI dalam Tkinter. dalam contoh ini, Label dengan teks
Hello World! akan ditempatkan di galam jendela utama sesuai dengan
tata letak default yang ditentukan oleh metode pack()
"""

root.mainloop()
