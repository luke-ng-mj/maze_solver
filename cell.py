from graphics import Line, Point
from constants import MAZE_BG_COLOR


class Cell:
    has_left_wall = True
    has_right_wall = True
    has_top_wall = True
    has_bottom_wall = True
    visited = False

    def __init__(self, window=None, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True) -> None:
        self._win = window
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall

    def get_mid_point(self) -> Point:
        my_cell_mid_x = (self._top_left_x + self._bot_right_x)//2
        my_cell_mid_y = (self._top_left_y + self._bot_right_y)//2
        return Point(my_cell_mid_x, my_cell_mid_y)

    def draw(self, top_left_pt:Point, bot_right_pt:Point):
        if self._win is None:
            return

        self._top_left_x = top_left_pt.x
        self._top_left_y = top_left_pt.y
        self._bot_right_x = bot_right_pt.x
        self._bot_right_y = bot_right_pt.y

        bot_left_pt = Point(self._top_left_x, self._bot_right_y)
        top_right_pt = Point(self._bot_right_x, self._top_left_y)

        line_left = Line(top_left_pt, bot_left_pt)
        if self.has_left_wall:
            self._win.draw_line(line_left)
        else:
            self._win.draw_line(line_left, fill_color=MAZE_BG_COLOR)

        line_right = Line(top_right_pt, bot_right_pt)
        if self.has_right_wall:
            self._win.draw_line(line_right)
        else:
            self._win.draw_line(line_right, fill_color=MAZE_BG_COLOR)

        line_top = Line(top_left_pt, top_right_pt)
        if self.has_top_wall:
            self._win.draw_line(line_top)
        else:
            self._win.draw_line(line_top, fill_color=MAZE_BG_COLOR)

        line_bottom = Line(bot_left_pt, bot_right_pt)
        if self.has_bottom_wall:
            self._win.draw_line(line_bottom)
        else:
            self._win.draw_line(line_bottom, fill_color=MAZE_BG_COLOR)

    def draw_move(self, to_cell, undo=False):
        # draw red line if undo=False
        # else draw gray line
        if self._win is None:
            return
        
        line_color = "gray" if undo else "red"
        my_cell_mid = self.get_mid_point()
        to_cell_mid = to_cell.get_mid_point()
        
        self._win.draw_line(Line(my_cell_mid, to_cell_mid), fill_color=line_color)
        