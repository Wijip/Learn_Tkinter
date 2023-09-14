import tkinter as tk


root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('600x400')
"""
kode root.geometry('600x400') -> kode ini digunakan untuk mengakses objek
jendela utama atau root. kemudian menggunakan metode .geometry() untuk
mengatur ukuran jendela. pada parameter 600x400 merupakan parameter
yang diberikan ke metode .geometry(), parameter ini adalah string
yang menggambarkan dimensi jendela pada format lebar dan tinggi. dalam contoh
kali ini ukuran diatur dengan lebar 600 piksel dan tinggi 400 piksel
"""

root.resizable(False, False)
"""
kode root.resizable(False, False) -> kode ini digunakan agar jendela dapat
di ubah ukuran sesuai dengan keinginan user. pada kode tersebut dapat
diberikan parameter boolean (False/True). terdapat 2 parameter yang dapat
ditambahkan (Parameter1, Parameter2). Parameter 1 akan mengontrol
apakah jendela dapat diubah ukurannya secara horizontal (lebar). sedangkan
parameter 2 mengontrol apakah jendela dapat diubah ukurannya dalam arah vertikal
(tinggi). dalam kasus ini keduanya memiliki parameter False. dimana jika 
kedua parameter memiliki kondisi False maka jendela tidak dapat dirubah
ukurannya, baik dalam arah horizontal (lebar) maupun vertikal (tinggi) oleh
pengguna.
"""
root.mainloop()
