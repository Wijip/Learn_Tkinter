import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Checkbox Demo')

agreement = tk.StringVar()
"""
agreement = tk.StringVar() -> merupakan pembuatan objek StringVar yang 
disebut 'agreement','StringVar' adalah tipe varibel khusus dalam modul
tkinter yang dapat digunakan untuk menyimpan nilai string yang dapat berubah.
dalam konteks ini, 'agreement' akan digunakan untuk menyimpan nilai
dari kotak centang {checkbox) yang digunakan untuk mengumpulkan persetujuan pengguna.
"""

def agreement_changed():
    tk.messagebox.showinfo(
        title='Result',
        message=agreement.get()
    )
"""
def argreement_changed() -> merupakan deklarasi sebuah fungsi yang disebut
'agreement_changed()'. fungsi ini akan dipanggil ketika nilai kotak centang
berubah (ketika pengguna mencentang atau mencabut centang dari kotak centang)
"""


ttk.Checkbutton(
    root,
    text='I agree',
    command=agreement_changed,
    variable=agreement,
    onvalue='agree',
    offvalue='disagree'
).pack()
"""
ttk.Checkbutton(....) -> merupakan kode untuk pembuatan kotak centang dengan
menggunakan pustaka ttk. parameter yang digunakan dalam kotak centang ini
sebagai berikut:
- 'roo' : parameter pertama adalah jendela utama tempat centang akan
          ditampilkan
- text='I agree' -> ini adalah teks yang akan ditampilkan bersama dengan
kotak centang. dalam kasus ini teksnya adalah "I agree"

- 
"""

root.mainloop()
