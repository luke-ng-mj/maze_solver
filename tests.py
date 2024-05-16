import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_odd_size(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 11, 11)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_zero_cells(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )

    def test_maze_entrance_n_exit_regular(self):
        num_cols = 5
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        ent_cell = m1._cells[0][0]
        self.assertFalse(ent_cell.has_top_wall)

        exit_cell = m1._cells[4][9]
        self.assertFalse(exit_cell.has_bottom_wall)

    def test_maze_entrance_n_exit_single_col(self):
        num_cols = 1
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        ent_cell = m1._cells[0][0]
        self.assertFalse(ent_cell.has_top_wall)

        exit_cell = m1._cells[0][9]
        self.assertFalse(exit_cell.has_bottom_wall)

    def test_maze_entrance_n_exit_single_row(self):
        num_cols = 10
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        ent_cell = m1._cells[0][0]
        self.assertFalse(ent_cell.has_top_wall)

        exit_cell = m1._cells[9][0]
        self.assertFalse(exit_cell.has_bottom_wall)

    def test_reset_cell_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        m1._reset_cells_visited()
        for col in m1._cells:
            for cell in col:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()
