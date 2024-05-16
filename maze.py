import time
import random
from graphics import Point
from cell import Cell

class Maze:

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.maze_origin_x = x1
        self.maze_origin_y = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        # Generate a matrix of cells
        for _ in range(self.num_cols):
            cell_col = []
            for _ in range(self.num_rows):
                cell_col.append(Cell(self._win))
            self._cells.append(cell_col)

        for i, cell_cols in enumerate(self._cells):
            for j, _ in enumerate(cell_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        m_cell = self._cells[i][j]
        cell_top_left_x = self.maze_origin_x + (i * self.cell_size_x)
        cell_top_left_y = self.maze_origin_y + (j * self.cell_size_y)
        cell_bot_right_x = cell_top_left_x + self.cell_size_x
        cell_bot_right_y = cell_top_left_y + self.cell_size_y

        m_cell.draw(Point(cell_top_left_x, cell_top_left_y), Point(cell_bot_right_x, cell_bot_right_y))
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        ent_cell_i = 0
        ent_cell_j = 0
        try:
            ent_cell = self._cells[ent_cell_i][ent_cell_j]
        except IndexError:
            return
        ent_cell.has_top_wall = False
        self._draw_cell(ent_cell_i, ent_cell_j)

        exit_cell_i = self.num_cols - 1
        exit_cell_j = self.num_rows - 1
        try:
            exit_cell = self._cells[exit_cell_i][exit_cell_j]
        except IndexError:
            return
        exit_cell.has_bottom_wall = False
        self._draw_cell(exit_cell_i, exit_cell_j)

    def _break_walls_r(self, i, j):
        try:
            curr_cell = self._cells[i][j]
            curr_cell.visited = True
            #print(f"Visited cell {i},{j}. Breaking walls")
        except IndexError:
            return
        
        while True:
            adj_cells_ij = []
            # Look for non-visited adjacent cells
            if j-1 >= 0:
                top_cell = self._cells[i][j-1]
                if not top_cell.visited:
                    adj_cells_ij.append((i, j-1))

            try:
                bot_cell = self._cells[i][j+1]
                if not bot_cell.visited:
                    adj_cells_ij.append((i, j+1))
            except IndexError:
                pass

            if i-1 >= 0:
                left_cell = self._cells[i-1][j]
                if not left_cell.visited:
                    adj_cells_ij.append((i-1, j))

            try:
                right_cell = self._cells[i+1][j]
                if not right_cell.visited:
                    adj_cells_ij.append((i+1, j))
            except IndexError:
                pass

            if not adj_cells_ij:
                self._draw_cell(i, j)
                return
            
            next_cell_ij = random.choice(adj_cells_ij)
            next_cell = self._cells[next_cell_ij[0]][next_cell_ij[1]]
            if next_cell_ij[0] == i:
                # Its either a top or bottom cell
                if next_cell_ij[1] == j+1:
                    # Its a bottom cell
                    curr_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                else:
                    # Its a top cell
                    curr_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
            elif next_cell_ij[1] == j:
                # Its either a left or right cell
                if next_cell_ij[0] == i+1:
                    # Its a right cell
                    curr_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                else:
                    # Its a left cell
                    curr_cell.has_left_wall = False
                    next_cell.has_right_wall = False
            else:
                raise Exception("Unexpected cell coordinates")

            self._draw_cell(i, j)
            self._draw_cell(next_cell_ij[0], next_cell_ij[1])
            self._break_walls_r(next_cell_ij[0], next_cell_ij[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _solve_r(self, i, j):
        self._animate()
        try:
            curr_cell = self._cells[i][j]
            curr_cell.visited = True
            #print(f"Visited cell {i},{j}.")
        except IndexError:
            return
        
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            # Reached the exit
            return True
        
        adj_cells_ij = []

        if j-1 >= 0:
            top_cell = self._cells[i][j-1]
            if not curr_cell.has_top_wall and not top_cell.visited:
                adj_cells_ij.append((i, j-1))

        try:
            bot_cell = self._cells[i][j+1]
            if not curr_cell.has_bottom_wall and not bot_cell.visited:
                adj_cells_ij.append((i, j+1))
        except IndexError:
            pass

        if i-1 >= 0:
            left_cell = self._cells[i-1][j]
            if not curr_cell.has_left_wall and not left_cell.visited:
                adj_cells_ij.append((i-1, j))

        try:
            right_cell = self._cells[i+1][j]
            if not curr_cell.has_right_wall and not right_cell.visited:
                adj_cells_ij.append((i+1, j))
        except IndexError:
            pass

        for adj_cell_i, adj_cell_j in adj_cells_ij:
            curr_cell.draw_move(self._cells[adj_cell_i][adj_cell_j])
            success = self._solve_r(adj_cell_i, adj_cell_j)
            if success:
                return True
            curr_cell.draw_move(self._cells[adj_cell_i][adj_cell_j], undo=True)

        return False


    def solve(self):
        return self._solve_r(0, 0)
