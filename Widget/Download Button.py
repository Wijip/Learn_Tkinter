import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Image Button Demo')

def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked'
    )
"""
def download_clicked -> merupakan deklarasi fungsi yang memiliki nama
download_clicked(). fungsi ini akan dipanggil ketika tombol download
ditekan. dalam contoh ini fungsi ini digunakan untuk menampilkan jendela
informasi saat tombol di tekan. lalu terdapat kode dengan nama showinfo()
yang dipanggil dari modul tkinter.messagebox. fungsi 'showinfo()' digunakan
untuk menampilkan jendela informasi kepada pengguna dalam kasus ini
memiliki pesan "Download button clicked" akan ditampilkan dengan judul 
"informastion" saat fungsi dipanggil. pesan akan muncul dalam bentuk
dialog sederhana
"""

download_icon = tk.PhotoImage(file='./Download_icon.png')
"""
pada kode 'download_icon' ini akan membuat objek gambar yaitu gambar_icon.png
menggunakan modul tikinter dan 'PhotoImage()' objek gambar ini digunakan
untuk menampung gambar ikon Download dan memberikan jalur ke gambar ikon
dengan menggunakan kode 'file='./Download_icon.png'. pastikan gambar
berada dalam folder yang dapat di akses
"""

download_button = ttk.Button(
    root,
    image=download_icon,
    command=download_clicked
)
"""
pada kode 'download_button = ttk.Button(....) -> pada baris ini, tombol
download akan dibuat menggunakan modul ttk. Parameter pertama, 'root'
merupakan jendela utama tempat tombol akan ditampilkan. parameter 'image'
adalah gambar ikon yang ingin ditampilkan di tombol, yang diambil dari
objek 'Download_icon' yang sudah dibuat. lalu terdapat parameter
'command' digunakan untuk menentukan fungsi yang akan dijalankan saat
tombol ditekan. dalam contoh kali ini ketika button di klik akan
memanggil fungsi 'download_clicked()'.
"""

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

"""
pada kode download_button.pack(...) -> pada kode ini terdapat fungsi
'.pack()' untuk menempatkan tombol 'Download' di dalam jendela.
lalu terdapat ipadx dan ipady serta terdapat expand.
-   ipadx dan ipady merupakan parameter opsional yang digunakan untuk menambahkan
ruang polos (padding) di sekitar tombol secara horizontal (ipadx) dan
vertikal (ipady). dalam kasus ini tombol akan memiliki ruang polos tambahan 
sebesar 5 pixel disekitarnya.

-   expand merupakan parameter opsional yang digunakan untuk memberi tahu
sistem untuk memperluas tombol agar mengisi seluruh area yang tersedia dalam
jendela. jika diberi nilai True, tombol akan memenuhi jendela secara
horizontal dika jendela diperbesar
"""

root.mainloop()
