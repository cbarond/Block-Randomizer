from genericpath import exists
from struct import pack
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.colorchooser import askcolor
import random

#from matplotlib import container


class App(tk.Tk):
    def __init__(self):
        super().__init__()
    
        # configure the root window
        self.title('Block Randomizer')
        self.geometry('1000x500')
        self.minsize(width=800, height=500)
    
        tk.Grid.rowconfigure(self, 0, weight=0)
        tk.Grid.rowconfigure(self, 1, weight=0)
        tk.Grid.columnconfigure(self, 0, weight=0)
        tk.Grid.columnconfigure(self, 1, weight=0)
    
    # Find and return current size of the window
    def win_size(self):
        x = self.winfo_width()
        y = self.winfo_height()
        return [x, y]
    
    # Find and return current position of the window
    def win_pos(self):
        x = self.winfo_rootx()
        y = self.winfo_rooty()
        return [x, y]

    # Return grid size
    def app_grid_size(self):
        x = self.grid_size()
        return x


class Settings(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}
        options2 = {'padx': 10, 'pady': 5}

        # label
        self.label = ttk.Label(self, text='Number of Items')
        self.label.grid(row=0, column=0, **options)

        # entry
        self.num = tk.StringVar()
        self.numbox = ttk.Entry(self, textvariable=self.num)
        self.numbox.grid(row=0, column=1)

        # set number of items
        self.button = ttk.Button(self, text='Set')
        self.button['command'] = self.set_items
        self.button.grid(row=0, column=2, **options)

        # output
        self.button = ttk.Button(self, text='Output')
        self.button['command'] = self.get_items
        self.button.grid(row=0, column=3, **options)

        # Label columns
        self.label = ttk.Label(self, text='Name').grid(row=1, column=0, **options2)
        self.label = ttk.Label(self, text='Quantity').grid(row=1, column=1, **options2)

        # create empty list for items
        self.items = []


        # show the frame on the container
        self.grid(row=0, column=0, **options, sticky='n')

    # create item objects and load into item list
    def set_items(self):
        self.reset_items()

        for i in range(int(self.num.get())):
            self.newframe = Input(app, i)
            self.items.append(self.newframe)
    
    # return list of items
    def get_items(self):
        #for i in range(len(self.items)):
        #    print(self.items[i].get_name(), self.items[i].get_quantity(), self.items[i].get_color())
        return self.items

    # reset list of items
    def reset_items(self):

        if len(app.winfo_children()) > 6:
            app.winfo_children()[-1].destroy()

        for i in range(len(self.items)):
            self.items[i].destroy()
        self.items = []



class Input(ttk.Frame):
    def __init__(self, container, row):
        super().__init__(container)

        options = {'padx': 2, 'pady': 2}

        # set initial quantity
        self.quantity = 0
        self.total = 0

        # entry box for name
        self.name = tk.StringVar()
        self.namebox = ttk.Entry(self, textvariable=self.name)
        self.namebox.grid(row=0, column=0, **options)

        # entry box for quantity
        self.quantity_in = tk.StringVar()
        self.quantitybox = ttk.Entry(self, textvariable=self.quantity_in)
        self.quantitybox.grid(row=0, column=1, **options)

        # color selector
        self.color = 'gray'
        self.colorbutton = tk.Button(self, bg=self.color, width=3)
        self.colorbutton['command'] = self.choose_color
        self.colorbutton.grid(row=0, column=2, **options)

        # save quantity into list
        self.set_button = ttk.Button(self, text='Set')
        self.set_button['command'] = self.set_quantity
        self.set_button.grid(row=0, column=3, **options)

        self.grid(row=row+1, column=0, sticky='n', **options)

    # create color picker
    def choose_color(self):
        self.color = askcolor(title='Color Chooser')[1]
        self.colorbutton.configure(bg=self.color)

    # save input quantity to class variable
    def set_quantity(self):
        self.quantity = int(self.quantity_in.get())
        self.total = int(self.quantity_in.get())

    # return name of item
    def get_name(self):
        return self.name.get()
    
    # return quantity of item
    def get_quantity(self):
        return self.quantity

    def get_total(self):
        return self.total
    
    # return color of item
    def get_color(self):
        return self.color

    # subtract 1 from quantity
    def use_one(self):
        self.quantity -= 1


class Dimensions(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 2, 'pady': 2}

        # labels
        self.label = ttk.Label(self, text='Rows').grid(row=0, column=0, **options)
        self.label = ttk.Label(self, text='Columns').grid(row=0, column=1, **options)

        # entry box for rows
        self.rows = tk.StringVar()
        self.rowsbox = ttk.Entry(self, textvariable=self.rows)
        self.rowsbox.grid(row=1, column=0, **options)

        # entry box for columns
        self.columns = tk.StringVar()
        self.columnsbox = ttk.Entry(self, textvariable=self.columns)
        self.columnsbox.grid(row=1, column=1, **options)

        # button to create grid
        self.set_button = ttk.Button(self, text='Draw')
        self.set_button['command'] = self.draw
        self.set_button.grid(row=1, column=2, **options)

        # temporary variable for draw function
        self.canvas = ttk.Frame(self)

        self.grid(row=0, column=1, sticky='w')
    
    # delete previous canvas and redraw
    def draw(self):

        # delete used/remaining list
        if len(app.winfo_children()) > 6:
            app.winfo_children()[-1].destroy()

        self.canvas.destroy()
        self.canvas = Grid(app)
        App.win_size(app)

    # return number of rows
    def get_rows(self):
        return int(self.rows.get())
    
    # return number of columns
    def get_cols(self):
        return int(self.columns.get())


class Grid(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 2, 'pady': 2}

        # create local size and position variables
        win_size = App.win_size(app)
        win_pos = App.win_pos(app)
        self.x = self.winfo_rootx()
        self.y = self.winfo_rooty()
        self.max_width = win_size[0]-410
        self.max_height = win_size[1]-107

        # calculate size of blocks
        self.block_size_max_x = self.max_width / int(Dimensions.get_cols(draw_frame))
        self.block_size_max_y = self.max_height / int(Dimensions.get_rows(draw_frame))

        if self.block_size_max_x < self.block_size_max_y:
            self.block_size = self.block_size_max_x
        else:
            self.block_size = self.block_size_max_y

        self.canvas_width = self.block_size * int(Dimensions.get_cols(draw_frame))
        self.canvas_height = self.block_size * int(Dimensions.get_rows(draw_frame))

        # create canvas to draw on; sized to ensure square blocks
        self.grid_canvas = tk.Canvas(self, bg='white', width=self.canvas_width, height=self.canvas_height)
        self.grid_canvas.grid(row=0, column=0)

        # print(win_size, win_pos, self.x, self.y)
        # print(self.winfo_rootx()-win_pos[0], self.winfo_rooty()-win_pos[1])

        self.grid_canvas.delete('all')
        # create randomized grid
        self.randomize()

        # display color coded grid
        self.display()

        # display used items
        self.used = Quantities(app)

        self.grid(row=1, column=1, rowspan=100, sticky='n')

    # randomizer function
    def randomize(self):
        self.items = Settings.get_items(input_items)

        # Reset item quantities
        for i in self.items:
            i.set_quantity()

        self.layout = []
        for i in range(Dimensions.get_rows(draw_frame)):
            self.layout.append([])
            for j in range(Dimensions.get_cols(draw_frame)):
                above = self.layout[i-1][j] if ((i-1) >= 0) else -1
                #below = self.layout[i+1][j] if ((i+1) < Dimensions.get_rows(draw_frame)) else -1
                left = self.layout[i][j-1] if ((j-1) >= 0) else -1
                #right = self.layout[i][j+1] if ((j+1) >= Dimensions.get_cols(draw_frame)) else -1
                value = -1
                while value in [above, left, -1]:
                    check = random.randint(0, len(self.items)-1)
                    value = check if (self.items[check].get_quantity() > 0) else -1
                self.layout[i].append(value)
                self.items[value].use_one()

    # displays colored grid; iterates through randomized grid
    def display(self):
        for i in range(len(self.layout)):
            for j in range(len(self.layout[i])):
                self.grid_canvas.create_rectangle(self.block_size * j, self.block_size * i, self.block_size * (j+1), self.block_size * (i+1), fill=self.items[self.layout[i][j]].get_color())
    

# displays used and remaining quantities of items
class Quantities(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 2, 'pady': 2}

        self.rows = App.app_grid_size(app)[1]
        self.items = Settings.get_items(input_items)

        self.used_label = ttk.Label(self, text="Used").grid(row=0, column=1, **options)
        self.remaining_label = ttk.Label(self, text="Remaining").grid(row=0, column=2, **options)

        for i, item in enumerate(self.items):
            self.name = ttk.Label(self, text=item.get_name()).grid(row=i+1, column=0, **options)
            self.used = ttk.Label(self, text=item.get_total()-item.get_quantity()).grid(row=i+1, column=1, **options)
            self.remain = ttk.Label(self, text=item.get_quantity()).grid(row=i+1, column=2, **options)

        

        self.grid(row=self.rows+2, column=0, sticky='n', **options)
        

 
if __name__ == "__main__":
    app = App()
    input_items = Settings(app)
    draw_frame = Dimensions(app)
    app.mainloop()