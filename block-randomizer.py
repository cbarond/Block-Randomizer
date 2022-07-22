from struct import pack
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.colorchooser import askcolor
import random


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('Block Randomizer')
    self.geometry('1000x500')

    tk.Grid.rowconfigure(self, 0, weight=0)
    tk.Grid.rowconfigure(self, 1, weight=0)
    tk.Grid.columnconfigure(self, 0, weight=0)

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}
        options2 = {'padx': 15, 'pady': 5}

        # label
        self.label = ttk.Label(self, text='Number of Items')
        self.label.grid(row=0, column=0, **options)

        # entry
        self.num = tk.StringVar()
        self.numbox = ttk.Entry(self, textvariable=self.num)
        self.numbox.grid(row=0, column=1)

        # button
        self.button = ttk.Button(self, text='Set')
        self.button['command'] = self.button_clicked
        self.button.grid(row=0, column=2, **options)

        # output
        self.button = ttk.Button(self, text='Output')
        self.button['command'] = self.get_ref
        self.button.grid(row=0, column=3, **options)


        self.label = ttk.Label(self, text='Name').grid(row=1, column=0, **options2)
        self.label = ttk.Label(self, text='Quantity').grid(row=1, column=1, **options2)

        self.ref = []


        # show the frame on the container
        self.grid(row=0, column=0, **options, sticky='n')

    def button_clicked(self):
        self.reset_ref

        for i in range(int(self.num.get())):
            self.newframe = Input(app, i)
            self.ref.append(self.newframe)
    
    def get_ref(self):
        for i in range(len(self.ref)):
            print(self.ref[i].get_name(), self.ref[i].get_quantity(), self.ref[i].get_color())
        return self.ref

    def reset_ref(self):
        self.ref = []

class Input(ttk.Frame):
    def __init__(self, container, row):
        super().__init__(container)

        options = {'padx': 2, 'pady': 2}

        self.quantity = 0

        self.name = tk.StringVar()
        self.namebox = ttk.Entry(self, textvariable=self.name)
        self.namebox.grid(row=0, column=0, **options)

        self.quantity_in = tk.StringVar()
        self.quantitybox = ttk.Entry(self, textvariable=self.quantity_in)
        self.quantitybox.grid(row=0, column=1, **options)

        self.color = 'gray'
        self.colorbutton = tk.Button(self, bg=self.color, width=3)
        self.colorbutton['command'] = self.choose_color
        self.colorbutton.grid(row=0, column=2, **options)

        self.set_button = ttk.Button(self, text='Set')
        self.set_button['command'] = self.set_quantity
        self.set_button.grid(row=0, column=3, **options)

        self.grid(row=row+1, column=0, sticky='n', **options)

    def choose_color(self):
        self.color = askcolor(title='Color Chooser')[1]
        self.colorbutton.configure(bg=self.color)

    def set_quantity(self):
        self.quantity = int(self.quantity_in.get())

    def get_name(self):
        return self.name.get()
    
    def get_quantity(self):
        return self.quantity
    
    def get_color(self):
        return self.color

    def use_one(self):
        self.quantity -= 1



if __name__ == "__main__":
  app = App()
  frame = MainFrame(app)
  app.mainloop()