import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry('300x200')
root.resizable(False, False)
root.title('LabelFrame Demo')

lf = ttk.Label(root, text='Alignment')
"""
pada kode ini digunakan untuk membuat elemen LabelFrame('lf') didalam jendela utama
('root') LabelFrame adalah sebuah wadah yang dapat digunakan untuk mengelompokkan elemen-elemen
lainnya dan memberikan judul (dalam hal ini Alignment) disekitarnya
- root: ini adalah jendela utama 
"""

lf.grid(column=0, row=0, padx=20, pady=20)
"""
pada kode ini menggunakan metode 'grid()' untuk menempatkan elemen LabelFrame('if') ke dalam jendela utama.
lalu terdapat parameter di dalamnya yaitu:
- column=0, row=0 : ini mengatur posisi LabelFrame di kolom 0 dan barus 0 dalam tatak letak grid jendela utama
- padx=20, pady=20 : ini menambahkan padding (ruang kosong) sebanyak 20 piksel di sekitar Label Frame, Sehingga
  LabelFrame akan memiliki lebih banyak ruang kosong disekitarnya
"""


alignment_var = tk.StringVar()
"""
pada kode tersebut digunakan untuk menyimpan StringVar() yang disimpan dalam variabel alignment_var dimana yang
disimpan merupakan nilai pilihan pengguna dalam aplikasi
"""

alignments = ('Left','Center','Right')
"""
ini merupakan tuple yang berisi tiga pilihan yang akan digunakan dalam aplikasi. dalam hal ini opsi tersebut adalah
'Left','Center','Right'. Anda dapat menggunakan tuple ini sebagai opsi untuk elemen-elemen seperti tombol radio (radio button)
atau daftar pilihan"
"""

grid_column = 0
"""
baris ini merupakan penambahan variabel 'grid_column' dengan nilai 0. ini mungkin digunakan untuk mengatur kolom awal
dalam tata letak grid jika akan menempatkan elemen-elemen lain dalam kolom yang sama.
"""

for alignment in alignments:
    radio = ttk.Radiobutton(lf, text=alignment, value=alignment, variable=alignment_var)
    radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)

    grid_column += 1
"""
kode for ini akan mengiterasi melalui setiap elemen dalam tuple 'alignments'. dalam hal ini, tuple 'alignment' berisi
tiga nilai: 'Left','Center','dan Right' lalu terdapat beberapa bagian kode didalam for ini seperti,
- radio = ttk.Radiobutton didalam loop ini akan membuat sebuah element radio button('radio') dengan konfigurasi beriktu:
  - 'lf' : ini adalah LabelFrame dimana elemen Radiobuttin akan ditempatkan
  - 'tekt=alignment' :merupakan parameter yang mengatur teks yang akan ditampilkan disamping tombol radio.
     nilai 'alignment' adalah nilai yang akan diambil dari iterasi saat ini dalam loop, sehingga teks akan menjadi
     'Left','Center',atau 'Right' sesuai dengan iterasi saat ini
  - 'value=alignment' : parameter ini mengatur nilai yang akan dikatikan dengan tombol radio saat tombol ini dipilih. 
    Nilai ini juga diambil dari iterasi saat ini dalam loop, sehingga nilai yang terkait dengan tombol radio akan sesuai
    dengan 'Left', 'Center', atau 'Right' sesuai dengan iterasi saat ini.
  - 'variable=alignment_var' : parameter ini menghubungkan tombol radio dengan variabel 'alignment_var', sehingga saat pengguna
    memilih salah satu tombol radio, nilai yang terkait dengan tombol radio tersebut akan disimpan dalam variabel 'alignment_var'

- radio.grid : setelah membuat elemen Radiobutton, kita menggunakan metode grid() untuk menempatkan dalam LabelFrame
  ('lf')di Jendela utama. pengaturan tata letak ini adalah sebagai berikut:
  - 'column=grid_column' : ini mengatur kolom dimana tombol radio akan ditempatkan. nilai 'grid_column' berubah dalam setiap
    iterasi loop untuk mengatur tombol radio ke kolom yang berbeda.
  - row=0 : ini digunakan untuk mengatur berus dimana tombol radio akan ditempatkan. Nilai 'row' diatur ke 0 sehingga
    semua tombol radio akan ditempatkan pada baris yang sama
  - ipadx=10, ipady=10 : ini parameter yang digunakan untuk menambahkan padding internal sebanyak 10 piksel baik secara
    horizontal (padx) maupun secara vertikal (pady)
"""

root.mainloop()
