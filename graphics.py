from tkinter import Tk, BOTH, Canvas


class Point:
    x=0
    y=0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, start_pt:Point, end_pt:Point) -> None:
        self.__start = start_pt
        self.__end = end_pt

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__start.x, self.__start.y,
            self.__end.x, self.__end.y,
            fill=fill_color, width=2
        )


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, line:Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

