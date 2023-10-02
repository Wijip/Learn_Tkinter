import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Treeview Demo')
        self.geometry('620x200')

        self.tree = self.create_tree_widget()

    def create_tree_widget(self):
        columns = ('first_name', 'last_name', 'email')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')

        tree.bind('<<TreeviewSelect>>', self.item_selected)
        tree.grid(row=0,column=0, sticky=tk.NSEW)

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        contact = []
        for n in range(1, 100):
            contact.append((f'first {n}', f'last{n}', f'email{n}@example.com'))

        for contact in contact:
            tree.insert('', tk.END, values=contact)

        return tree

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            showinfo(title='information', message=','.join(record))

if __name__ == '__main__':
    app = App()
    app.mainloop()
