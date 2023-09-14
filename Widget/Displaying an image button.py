import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

"""
from tkinter.messagebox import showinfo -> pada baris ini kita mengimpor
fungsi 'showinfo' secara spesifik dari modul 'tkinter.messagebox'
fungsi ini digunakan unutk menampilkan kotak pesan informasi
(information message box) kepada pengguna. kotak pesan informasi biasanya
berisi pesan singkat yang memberi tahu pengguna tentang sesuatu.
"""

root = tk.Tk()
root.geometry('300x200')
root.resizable(True, True)
root.title('Image Button Demo')

def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'
    )

download_icon = tk.PhotoImage(file='./Download_icon.png')

download_button = ttk.Button(
    root,
    image=download_icon,
    text='Download',
    compound=tk.LEFT,
    command=download_clicked
)

"""
pada kode diatas memiliki beberapa parameter, seperti root,image,text
compound dan command. pada kode tersebut terdapat kode yang berbeda dari
percobaan sebelumnya yaitu kode compound dan text.
- pada kode 'text='Download' merupakan parameter yang digunakan untuk
menentukan teks yang akan ditampilkan di tombol. dalam hal ini, teks tombol
adalah Download.
- pada kode compound=tk.LEFT merupakan parameter yang digunakan untuk
mengatur posisi gambar terhadap teks di tombol. Nilai 'tk.LEFT' berarti
bahwa gambar akan ditempatkan disebelah kiri teks
"""

download_button.pack(
    ipadx=5,
    ipady=2,
    expand=True
)


root.mainloop()
