from tkinter import Button, Label
import settings
import random

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    #region magic methods override 
    def __init__(self, x, y,  is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.cell_button_object = None
        self.x = x
        self.y = y
        
        # Append Object to Call.all list
        Cell.all.append(self)

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

    #endregion

    #region tkinter object instantiation
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_button_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left: {Cell.cell_count}",
            font=("", 25)
        )
        Cell.cell_count_label_object = lbl
    #endregion 
    
    #region left and right click functions
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_cells_mines_length == 0:
                for cell_obj in self.surrounding_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")
    #endregion

    def get_cell_by_axis(self, x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounding_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x , self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),

        ]
        cells = [x for x in cells if x is not None]
        return cells

    @property
    def surrounding_cells_mines_length(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1
        
        return counter

    def show_mine(self):
        self.cell_button_object.configure(bg='red')

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1
            self.cell_button_object.configure(text=self.surrounding_cells_mines_length)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f'Cells Left: {Cell.cell_count}')
        
        # Mark the cell as open
        self.is_open = True
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, 
            settings.MINES_COUNT 
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True


