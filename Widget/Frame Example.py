import tkinter as tk
from tkinter import  TclError, ttk

def create_input_frame(container):
    frame = ttk.Frame(container)
    """    
    frame = ttk.Frame(container) pada kode ini akan membuat sebuah objek
    frame dengan menggunakan modul ttk. Frame ini akan ditempatkan didalam
    container yang ditentukan oleh parameter container dan saat fungsi di panggil
    dengan kata lain frame baru akan menjadi sub frame di dalam container.
    lalu terdapat kode ttk.frame(container) ini merupaka konstruktor yang
    digunakan untuk membuat frame dengan modul ttk. parameter container menunjukkan
    nama frame baru yang akan ditambahkan
    """

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)
    """
    frame.columnconfigure(0, weight=1) -> pada kode ini akan mengatur konfigurasi
    kolom pertama (kolom dengan index 0) pada frame yang disebut 'frame'.
    dengan mengatur 'weight=1', akan memberikan bobot (weight) sebesar 1
    pada kolom tersebut
    
    frame.columnconfigure(0, weight=3) -> pada kode ini akan mengatur ulang
    konfigurasi kolom pertama (kolom index 0) pada frame yang sama 'frame'.
    namun, pada baris kode ini akan mengatur weight menjadi 3.
    
    dimana pengaturan weight digunakan untuk mengendalikan sejauh mana sebuah
    kolom akan diperluas atau menyusut saat jendela (window) atau frame diubah
    ukurannya
    """

    ttk.Label(frame, text="Find What:").grid(column=0, row=0, sticky=tk.W)
    """
    pada kode ttk.Label(...) pada bari ini akan membuat sebuah label dengan teks
    'Find What:' yang akan digunakan untuk menunjukan tempat dimana pengguna
    memasukkan kata kunci pencarian. Label ini ditempatkan didalam frame
    dengan posisi kolom 0 dan baris 0. 'sticky=tk.W' digunakan untuk mengatur
    agar label melekat di sisi kiri kolom. ini berarti label akan muncul
    disisi kiri kotak input yang akan digunakan untuk memasukkan kata
    kunci perncarian
    """

    keyword = ttk.Entry(frame, width=30)
    """
    lalu terdapat keyword= ttk.Entry(...) merupakan kode yang akan membuat
    sebuah elemen input teks ('Entry') yang disimpan dalam variabel
    keyword. elemen ini akan digunakan oleh pengguna untuk memasukkan kata kunci
    pencarian. properti 'width=30' digunakan untuk mengatur lebar elemen
    input sehingga dapat menampung teks sepanjang 30 karakter.
    """

    keyword.focus()
    """
    pad kode keyword.focus akan memberikan fokus ke elemen input teks 'keyword',
    ini berarti elemen siap untuk menerima input dari pengguna tanpa perlau
    mengkliknya terlebih dahulu
    """
    keyword.grid(column=1, row=0, sticky=tk.W)
    """
    keyword.grid(column=1, row=0, sticky=tk.W) kode ini adalah elemen
    input teks yang digunakan untuk memasukkan kata kunci pencarian.
    elemen ini ditempatkan didalam frame dengan posisi kolom 1 dan baris 0
    sticky=tk.W digunakan untuk mengatur agar elemen ini melekat di sisi 
    kiri kolom 1. sehinggal emelem ini akan muncul disebelah kanan label
    "find What"
    """

    # Replace with:
    ttk.Label(frame, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
    """
    pada baris ini adalah kode yang digunakan untuk pembuatan label "Replace with"
    yang akan menunjukkan tempat dimana pengguna memasukkan kata kunci
    pengganti. Label ini ditempatkan didalam frame dengan posisi kolom 0
    dan baris 0. elemen ini akan muncul di atas elemen input untuk kata kunci pengganti
    """

    replacement = ttk.Entry(frame, width=30)
    """
    pada kode ini elemen input yang digunakan untuk memasukka kata kunci pengganti
    dengan memiliki properti width=30 untuk mengatur lebar elemen input sehingga dapat 
    menampung teks sepanjang 30 karakter
    """

    replacement.grid(column=1, row=1, sticky=tk.W)
    """
    pada baris kode ini digunakan untuk menempatkan baris elemen input teks
    replacement didalam frame dengan posisi kolom1 dan baris 1.
    ini akan muncul disebelah kanan label "replace with"
    """

    # Match Case checkbox
    match_case = tk.StringVar()
    """
    pada baris ini adalah pembuatan variabel match_case yang akan digunakan
    untuk menyimpan nilai dari kotak centang "match_case' (sesuai dengan
    huruf besar dan kecil) selanjutnya. elemen kotak centang (Checkbutton) untuk
    "Match case" dibuat dan dihubungkan dengan variabel 'match_case'.
    ketika kotak centang ini diklik aku tercentang atau centang nya di hapus
    nilai dalam match_case akan berubah juga.
    """

    match_case_check = ttk.Checkbutton(
        frame,
        text='Match case',
        variable=match_case,
        command=lambda: print(match_case.get()))
    """
    pada baris kode ini akan membuat objek kotak centang atau checkbox
    menggunakan modul ttk (Themed Tkinter). objek ini disimpan dalam
    variabel 'math_case_check' untuk kemudahan penggunaan selanjutnya.
    - lalu terdapat parameter frame diamana checkbox akan ditempatkan.
    dalam hal ini, checkbox ini akan ditempatkan di dalam frame.
    - selain itu terdapat parameter 'text=math case' yang digunakan untuk
    mengatur teks yang akan ditampilkan di samping checkbox. dalam kasus
    ini, teksnya adalah "Match Case" yang akan menjadi label untuk
    pengaturan ini.
    - kemudian terdapat parameter 'variable=match_case' parameter ini 
    menghubungkan checkbox dengan variable 'match_case'. variabel match_case
    ini yang akan menyimpan nilai dari checkbox, apakah checkbox tersebut
    tercentang atau tidak.
    - terdapat kode command=lamda:print(match_case.get()) ini merupakan
    parameter yang akan menentukan tindakan yang akan dijalankan ketika
    checkbox dicentang atau tidak dicentang. dalam hal ini fungsi lamda
    untuk mencetak nilai dari variabel 'match_case' saat checkbox
    berubah statusnya. dengan ini, dapat dilihat apakah checkbox ini
    dicentang atau tidak.
    """

    match_case_check.grid(column=0, row=2, sticky=tk.W)
    """
    pada kode ini digunakan untuk menempatkan checkbox dengan nama
    'match_case_check' di dalam frame dengan posisi kolom 0 dan baris 2.
    'sticky=tk.W' digunakan untuk mengatur agar checkbox melekat disusu
    kiri kolom 0, sehingga checkbox ini akan muncul disebelhar kiri label
    'Match Case'
    """


    # Wrap Around checkbox
    wrap_around = tk.StringVar()
    """
    wrap_around = tk.StringVar() -> pada baris kode tersebut 'wrap_around'.
    Objek ini akan digunakan untuk menyimpan nilai dari checkbox 'Wrap Around'
    (yaitu apakah checkbox dicentang atau tidak)
    """

    wrap_around_check = ttk.Checkbutton(
        frame,
        variable=wrap_around,
        text='Wrap around',
        command=lambda: print(wrap_around.get()))
    """
    pada kode pada baris 148 akan membuat sebuah objek kotak centang dengan
    menggunakan modul ttk(Themed Tkinter), Objek ini disimpan dalam variabel
    'wrao_around_check' untuk memudahkan penggunaan selanjutnya. lalu pada kode 
    tersebut terdapat beberapa parameter yaitu:
    - frame merupakan kerangka dimana checkbox akan ditempatkan. didalam hal ini
    checkbox akan ditempatkan dalam frame tersebut.
    - variable=wrap_around parameter tersebut akan menghubungkan checkbox
    dengan variabel 'warp_around' yang akan menyimpan nilai dari checkbox
    (yaitu apakah checkbox dicentang atau tidak)
    - text='Wrap around', parameter ini digunakan untuk mengatur text yang
    akan ditampilkan disamping checkbox. dalam kasus ini teksnya adalah 
    Wrap Around yang akan menjadi label untuk pengaturan ini.
    - command=lambda: print(wrap_around.get()) merupakan parameter 'command
    yang menentukan tindakkan yang akan dijalankan ketika checkbox dicentang
    atau tidak di centang. dalam hal ini, dapat menggunakan fungsi lambda untuk
    mencetak nilai variabel 'warp_around' saat kotak centang berubah statusnya
    dengan ini, pengguna dapat melihan apakah kotak centang ini dicentang atau tidak.
    """

    wrap_around_check.grid(column=0, row=3, sticky=tk.W)
    """
    wrap_around_check.grid(column=0, row=3, sticky=tk.W) pada kode ini
    menempatkan kotak centang 'wrap_around_check' di dalam frame dengan posisi
    kolom 0 dan baris 3 'sticky=tk,W' mengatur agar kotak centang "melekat" disii
    kiri kolom 0, sehingga kotak centang akan muncul disebelah kiri label
    "Warp Around"
    """

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)
    """
    pada kode loop digunakan untuk mengatur semua elemen yang merupakan anak
    dari frame dengan menabahkan sedikit padding disekitar setiap elemen,
    memberikan tampilan yang lebih rapi pada antamuka
    """

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)
    """
    frame = ttk.Frame(container) -> pada baris kode ini akan membuat objek frame('Frame')
    menggunakan modul ttk (Themed Tkinter) dan menyimpan dalam variabel 'frame'.
    frame ini akan digunakan untuk mengelompokkan tombol-tombol bersama-sama
    dalam frame yang akan ditampilkan dijendela program.
    """

    frame.columnconfigure(0, weight=1)
    """
    frame.columnconfigure(0, weight=1) -> baris ini mengkonfigurasi kolom pertama (kolom dengan index 0)
    dalam frame dengan memberikan bobot (weight) sebesar 1. ini berguna jika anda ingin
    tombol-tombol dalam frame ini merespons perubahan ukuran jendela dengan proporsional
    """

    ttk.Button(frame, text='Find Next').grid(column=0, row=0)
    """
    Baris ini mengkonfigurasi kolom pertama (kolom dengan indeks 0) dalam frame dengan memberikan bobot (weight)
    sebesar 1. dengan berguna jika anda ingin tombol-tombol dalam frame ini merespons perubahan
    ukuran jendela dengan proposional.
    """

    ttk.Button(frame, text='Replace').grid(column=0, row=1)
    """
    pada baris kode ini digunakan untuk pembuatan tombol "Replace" yang ditempatkan didalam
    frame pada kolom 0 dan baris 1.
    """

    ttk.Button(frame, text='Replace All').grid(column=0, row=2)
    """
    pada baris kode ini digunakan untuk pembuatan tombol "Replace All" yang ditempatkan didalam
    frame pada kolom 0 dan baris 2
    """

    ttk.Button(frame, text='Cancel').grid(column=0, row=3)
    """
    pada baris kode ini digunakan untuk pembuatan tombol cencel yang ditempatkan didalam frame
    pada kolom 0 dan baris 3
    """

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)
    """
    pada kode perulangan tersebut akan mengatur semua elemen yang merupakan anak-anak dari frame
    dengan menambahkan sedikit padding di sekitar setiap elemen. Padding ini memberikan tempilan
    yang lebih rapi pada antarmuka, menjaga jarak antara tombol-tombol.
    """

    return frame


def create_main_window():
    root = tk.Tk()
    root.title('Replace')
    root.resizable(False, False)
    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')
    """
    kode Try and except ini digunakan untuk menghilangkan tombol minimize dan maximize. 
    
    """

    # layout on the root window
    root.columnconfigure(0, weight=4)
    """
    pada baris ini akan mengatur kolom pertama (kolom dengan indeks 0) dalam jendela utama
    (root window) dengan memberikan bobot (weight) sebesar 4. pengaturan ini mengindikasikan
    bahwa kolom ini akan lebih fleksibel dalam menganggapi perubahan ukuran jendela. dengan bobot
    yang lebih tinggi, kolom pertama akan memperluas dirinya lebih cepat daripada kolom lainnya
    saat jendela diperbesar
    """

    root.columnconfigure(1, weight=1)
    """
    pada baris ini akan mengatur kolom kedua (kolom dengan indeks 1) dalam jendela utama dengan
    bobot sebesar 1. ini mengindikasikan bahwa kolom kedua akan kurang fleksibel dalam menanggapi 
    perubahan ukuran jendela daripada kolom pertama
    """

    input_frame = create_input_frame(root)
    """
    pada kode beris ini akan membuat frame dengan variabel 'input_frame' yang menggunakan fungsi
    'create_input_frame()'. dimana fungsi tersebut akan di simpan dalam variabel 'input_frame'
    Frame ini berisi elemen-elemen input seperti kotak teks dan kotak centang.
    """

    input_frame.grid(column=0, row=0)
    """
    pada kode beris ini akan menempatkan frame dengan variabel 'input_frame' didalam jendela
    utama pada kolom 0 (kolom pertama) dan baris 0. dengan ini, frame 'input_frame' akan ditampilkan
    dibagian kiri atas jendela utama.
    """

    button_frame = create_button_frame(root)
    """
    pada baris ini akan membuat variabel 'button_frame' yang menggunakan fungsi
    'create_button_frame()' dan akan menyimpannya dalam variabel 'button_frame'. frame ini berisi
    tombol-tombol seperti "Find Next" dan "Replace".
    """

    button_frame.grid(column=1, row=0)
    """
    kode pada baris ini akan menempatkan frame 'button_frame' di dalam jendela utama pada kolom 1 (kolom kedua)
    dan baris 0. dengan ini, frame 'button_frame' akan ditampilkan dibagian kanan atas jendela.
    """

    root.mainloop()
    """
    pada baris kode ini akan memulai loop utaman aplikasi tkinter yang akan menjaga jendela utama
    tetap terbuka dan merespon interaksi pengguna. seluruh aplikasi akan terus berjalan sampai
    pengguna menutup jendela
    """


if __name__ == "__main__":
    create_main_window()
