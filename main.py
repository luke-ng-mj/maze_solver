import time
from graphics import Window, Point
from cell import Cell
from maze import Maze


def main_b():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.draw(Point(10,10), Point(50,50))

    cell2 = Cell(win, top_wall=False)
    cell2.draw(Point(60,10), Point(100,50))

    cell3 = Cell(win, top_wall=False, bottom_wall=False, right_wall=False, left_wall=False)
    cell3.draw(Point(110,10), Point(150,50))

    cell4 = Cell(win, bottom_wall=False, right_wall=False)
    cell4.draw(Point(160,10), Point(200,50))

    cell5 = Cell(win)
    cell5.draw(Point(10,60), Point(50,100))
    
    win.redraw()
    time.sleep(1)
    cell1.draw_move(cell3)
    win.redraw()
    time.sleep(1)
    cell1.draw_move(cell5)
    win.redraw()
    time.sleep(1)
    cell1.draw_move(cell5, undo=True)

    win.wait_for_close()


def main():
    win = Window(800, 600)
    maze = Maze(1, 1, num_rows=12, num_cols=12, cell_size_x=40, cell_size_y=40, win=win, seed=0)
    #maze = Maze(1, 1, num_rows=10, num_cols=1, cell_size_x=40, cell_size_y=40, win=win)
    maze.solve()
    win.wait_for_close()


main()
