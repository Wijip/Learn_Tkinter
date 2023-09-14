import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.resizable(False,False)
root.title('Label Widget Demo')

label = tk.Label(root, text="This is a label", font=('arial', 10))
"""
pada baris ini akan membuat objel label dengan menggunakan modul tkinter. Label ini akan
menampilkan teks this is a label. parameter root merupakan jendela utama dimana label akan
ditempatkan, selain itu pada kode tersebut dapat ditambahkan kode font untuk mengganti tipe font
yang akan ditampilkan serta ukuran font yang akan ditampilkan dengan menggunakan kode
'font=('arial', 14)'.
"""

label.pack(ipadx=10, ipady=10)
"""
pada baris kode ini menggunakan metode pack() untuk menempatkan label ke dalam jendela utama.
metode pack() digunakan untuk mengatur tata letak secara otomatis sesuai dengan urutan
elemen-elemen yang ditambahkan kedalamnya.
lalu terdapat parameter ipadx=10 dan ipady=10 ini adalah parameter opsional yang digunakan
untuk menambahkan padding internal (ipadx dan ipady) di sekitar label. padding internal
ini akan memberikan ruang tambahan disekitar teks dalam label sehingga label akan memiliki
lebih banyak ruang sekitarnya.
"""

root.mainloop()
