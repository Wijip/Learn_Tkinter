import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x200')
# root.resizable(False,False)
root.title('Label Widget Image')

photo = tk.PhotoImage(file='./Instagram.png')
"""
pada baris ini digunakan untuk membaca gambar dengan nama file "Instagram.png" dari lokasi yang
diberikan. dalam contoh ini gambar memiliki lokasi yang relif, artinya gambar tersebut
dalam satu direktori yang sama dengan file program. kemudian gambar tersebut di konversi
menjadi objek PhotoImage Tkinter dan disimpan dalam variabel photo.
"""

image_label = ttk.Label(root,image=photo, padding=5, text='Instagram', compound='top')
"""
pada baris ini akan membuat elemen Label dengan konfigurasi seperti berikut
- 'roo': ini adalah jendela utama atau frame dimana elemen Label akan ditempatkan
- image=photo : parameter in digunakan untuk menyatakan bahwa gambat yang telah di load
  sebelumnya akan ditampilkan di elemen Label
- padding=5 : parameter ini menambahkan padding (ruang kosong) sebanyak 5 piksel
  disekitar gambar didalam elemen Label. ini akan membantu untuk mengatur jarak antara gambar
  dan teks yang akan ditambahkan nanti.
- teks='Instagram' : parameter ini digunakan untuk menambahkan teks "Instagram" dibawah gambar
  dalam elemen Label
- compound='top' : parameter ini mengatur posisi teks terhadap gambar. dengan nilai top. 
  teks akan ditempatkan diatas gambar.

"""

image_label.pack()
"""
beris ini menggunakan metode '.pack()" ke dalam jendela utama. ini akan membuat elemen
Label dengan gambar dan teks ditampilkan dalam jendela sesuai dengan tata letak default
yang disediakan oleh metode 'pack()'
"""

root.mainloop()
