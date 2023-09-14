import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('600x400+50+50')
root.resizable(False, False)
root.attributes('-alpha', 0.5)
"""
kode root.attributes('-alpha',0.5) -> kode ini digunakan untuk mengakses
objek root dengan menggunakan metode .attributes() untuk mengatur atribut
pada jendela. lalu terdapat kode -alpha yang merupakan parameter pertama
yang diberikan kepada metode .attributes(). parameter ini mengindikasi
bahwa anda ingin mengatur atribut transparansi (aplha) dari jendela.
lalu ada parametee 0.5, ini adalah parameter kedua yang diberikan pada
metode .attributes(). parameter ini adalah nilai transparansi yang diterapkan
pada jendela. dalam hal ini nilai yang diberikan yaitu 0.5 yang menunjukkan
bahwa transparansi jendela memiliki tingkat sebesar 50%. dimana jika nilai
yang dimasukkan 1.0 merupakan transparansi penuh (tidak transparan) dan 
angka 0.0 adalah transparansi total (tidak terlihat)
"""

# message = tk.Label(root, text='Testing Transparent Window')
# message.pack()

root.mainloop()
