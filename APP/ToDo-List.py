from tkinter import *

class ToDoList:
    def __init__(self, root):
        self.task = []
        self.root = root
        self.listbox = Listbox(self.root)
        self.entry = Entry(self.root)
        self.addButton = Button(self.root, text="Add Task", command=self.add_task)
        self.delButton = Button(self.root, text="Delete Task", command=self.delete_task)
        self.exiButton = Button(self.root, text="Exit", command=self.root.destroy)

        # GUI Layout
        self.entry.pack()
        self.addButton.pack()
        self.listbox.pack()
        self.delButton.pack()
        self.exiButton.pack()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(END, task)
            self.entry.delete(0, END)

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.listbox.delete(task_index)
        except:
            pass




root = Tk()
root.title("Python To-Do List")
root.geometry("300x400") # Set the window size
to_do_list = ToDoList(root)
root.mainloop()