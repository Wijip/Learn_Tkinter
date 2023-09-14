import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title("Button Demo")

#exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)
"""
pada kode diatas exit_button merupakan kode untuk membuat objek tombol(button)
dengan menggunakan pustaka ttk. parameter awal root adalah jendela utama tempat
tombol akan ditampilkan. parameter kedua 'text' adalah teks yang akan ditampilkan
di tombol, pada kode ini text yang digunakan yaitu Exit. parameter ketiga
yaitu command, merupakan perintah yang akan dieksekusi saat tombol ditekan.
lalu pada kode tersebut dapat menggunakan fungsi lambda untuk membuat fungsi
anonim yang akan menjalakan kode 'root.quit()'. kode 'root.quit()' di gunakan
untuk mengakhiri program atau menutup jendela aplikasi
"""


exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
"""
pada kode exit_button.pack() menggunakan metode '.pack()' untuk menempatkan
tombol ke dalam jendela. lalu terdapat parameter 'ipadx=5' dan 'ipady=5'
merupakan parameter opsional yang digunakan untuk menambahkan ruang polos (padding)
disekitar tombol secara horizontal (ipadx) dan vertikal (ipady). dalam kode
kali ini tombol akan memiliki ruang polos tambahan sebesar 5 piksel di sekitarnya.
"""


root.mainloop()
