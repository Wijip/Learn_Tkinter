import tkinter as tk
from barang import Barang
from log import Log

class AplikasiCekBarang:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Cek Barang")
        self.log = Log()

        self.daftar_barang = []

        self.label_nama = tk.Label(root, text="Nama Barang:")
        self.label_harga = tk.Label(root, text="Harga Barang:")
        self.entry_nama = tk.Entry(root)
        self.entry_harga = tk.Entry(root)
        self.button_tambah = tk.Button(root, text="Tambah Barang", command=self.tambah_barang)
        self.button_tampilkan = tk.Button(root, text="Tampilkan Log", command=self.tampilkan_log)

        self.label_nama.pack()
        self.entry_nama.pack()
        self.label_harga.pack()
        self.entry_harga.pack()
        self.button_tambah.pack()
        self.button_tampilkan.pack()

    def tambah_barang(self):
        nama = self.entry_nama.get()
        harga = self.entry_harga.get()
        barang = Barang(nama, harga)
        self.daftar_barang.append(barang)
        self.log.tambah_log(f"Menambah barang: {nama} - Harga: {harga}")
        self.entry_nama.delete(0, tk.END)
        self.entry_harga.delete(0, tk.END)

    def tampilkan_log(self):
        self.log.tampilkan_log()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiCekBarang(root)
    root.mainloop()
