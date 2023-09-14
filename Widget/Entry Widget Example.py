import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# window
root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title('Sign In Demo')

email = tk.StringVar()
password = tk.StringVar()
"""
kode 'email = tk.StringVar()' dan 'password = tk.StringVar()' merupakan
kode pembuatan 2 objek 'StringVar' yang digunakan untuk menyimpan imput
yang dimasukkan oleh pengguna. dalam contoh ini merupakan email dan
password. Objek-Objek ini akan memungkinkan untuk mengakses dan mengelola
nilai-nilai yang dimasukkan oleh pengguna.
"""


def login_clicked():
    msg = f'You entered email: {email.get()} and password : {password.get()}'
    showinfo(
        title='Informastion',
        message=msg
    )
"""
kode 'def login_clicked():' ini merupakan kode untuk deklarasi fungsi
dengan nama 'login_clicked()'. fungsi ini akan dipanggil ketika
tombol 'Login' pada program ditekan. fungsi ini juga dapat menambil nilai
dari objek 'StringVar' 'email' dan 'password', lalu menggabungkannya dalam
pesan yang akan ditampilkan kepada pengguna melalui fungsi 'showinfo()'.
pada fungsi show info terdapat kode 'msg' yang merupakan fungsi untuk menampilkan
pesan kepada pengguna pesan ini berisikan alamat email dan password
yang dimasukkan pengguna. dimana nilai dari StringVar enail dan password
yang dimasukkan pengguna akan diambil oleh kode program {email.get()}
dan {password.get()}. pada kode tersebut pengambilan nilai menggunakan
metode '.get()'.
"""

signin = ttk.Frame(root)
"""
kode signin = ttk.Frame(root) digunakan untuk pembuatan objek frame dari modul
ttk yang disebut dengan signin. frame yang digunakan untuk
mengelompokan elemen-elemen GUI bersama-sama
"""

signin.pack(padx=10, pady=10, fill='x', expand=True)
"""
kode signin.pack(padx=10, pady=10, fill='x', expand=True) ini merupakan metode
'.pack()' yang digunakan untuk menempatkan Frame signin didalam jendela
utama (root). metode ini mengatur tampilan Fram dalam jendela, termasuk
padding ('padx' dan 'pady'), dan cara mengisi fill dan memperluas ('expand')
ruang yang tersedia
"""

#email
email_label = ttk.Label(signin, text="Email Address : ")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

#password
password_label = ttk.Label(signin, text="Password")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)
"""
pada bagian email dan password terdapat kata objek Label dan entry.
digunakan untuk membuat objek label dengan menggunakan modul ttk. lalu
pada kode yang memiliki objek Entry yang digunakan untuk membuat objek Entry
dimana objek tersebut akan menerima input dari pengguna. kemudian pada
password_entry = .... terdapat kode show="*" yang digunakan agar ketika
pengguna memasukkan input. maka pada program akan menampilan tanda * di
saat pengguna memasukkan password.
"""

#login Button
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)
"""
pada baris awal merupakan pembuatan objek button dengan text Login. dimana
ketika button login di klik maka akan memanggil fungsi 'login_clicked'.
lalu pada button tersebut memiliki parameter signin yang merupakan frame
atau kerangka dimana tombol tersebut akan ditempatkan.

lalu terdapat kode .pack() yang memiliki 3 parameter. metode pack ini yang akan
digunakan unutk menetapkan posisi tombol login di dalam fram yang dinamakan
signin. lalu terdapat parameter sebagi berikut 
- fill='x' parameter ini digunakan untuk mengatur agar tombol memenuhi
seluruh lebar frame ('signin'). ini akan membuat tombol memanjang sejauh mungkin
secara horizontal

- expand=True para parameter ini akan memberitahu sistem untuk memperluas
tombol secara horizontal jika ukuran frame diperbesar. dengan kata lain
tombol akan mengikuti perubahan ukuran frame.
"""


root.mainloop()
