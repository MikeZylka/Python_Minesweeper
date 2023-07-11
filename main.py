import sys
sys.path.insert(1, './src')
from tkinter import *
from cell import Cell
import settings
import utils


root = Tk()

# Window Settings Override
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

#region Frame Creation in Window
top_frame = Frame(
    root, 
    bg='black', # Will be changed later
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root, 
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))
#endregion

#region Create Grid
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_button_object.grid(
            column=x, row=y
        )
#endregion

#region Game Setup 
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

Cell.randomize_mines()
#endregion


# Run the Window
root.mainloop()
