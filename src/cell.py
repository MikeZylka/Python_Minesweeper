from tkinter import Button
import settings
import random

class Cell:
    all = []
    def __init__(self, x, y,  is_mine=False):
        self.is_mine = is_mine
        self.cell_button_object = None
        self.x = x
        self.y = y
        
        # Append Object to Call.all list
        Cell.all.append(self)

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_button_object = btn

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
        self.cell_button_object.configure(text=self.surrounding_cells_mines_length)

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, 
            settings.MINES_COUNT 
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True


