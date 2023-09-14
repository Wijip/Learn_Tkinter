# import tkinter as tk
#
# root = tk.Tk()
# root.title("Tkinter Window Demo")
#
# window_width = 300
# window_height = 200
#
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
#
# center_x = int(screen_width / 2 - window_width / 2)
# center_y = int(screen_height / 2 - window_height / 2)
#
# root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# root.mainloop()


import tkinter as tk


# root = tk.Tk()
# root.title('Tkinter Window Demo')
# root.geometry('600x400')
# """
# kode root.geometry('600x400') -> kode ini digunakan untuk mengakses objek
# jendela utama atau root. kemudian menggunakan metode .geometry() untuk
# mengatur ukuran jendela. pada parameter 600x400 merupakan parameter
# yang diberikan ke metode .geometry(), parameter ini adalah string
# yang menggambarkan dimensi jendela pada format lebar dan tinggi. dalam contoh
# kali ini ukuran diatur dengan lebar 600 piksel dan tinggi 400 piksel
# """
#
# root.resizable(False, True)
# root.mainloop()

root = tk.Tk()

# root.geometry('800x600')
# top_frame = tk.Frame(root)
# top_frame.pack()
#
# bottom_frame = tk.Frame(root)
# bottom_frame.place(x=0, y=0, anchor='nw')
#
# root.mainloop()


