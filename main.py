from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        # Create the root window
        self.__root = Tk()

        # Set window title
        self.__root.title("Maze Solver")

        # Create canvas
        self.__canvas = Canvas(
            self.__root,
            bg="white",
            width=width,
            height=height
        )

        # Make canvas fill the window
        self.__canvas.pack(fill=BOTH, expand=1)

        # Running state
        self.__running = False

        # Handle window close button
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        # Refresh the window
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        # Keep window open
        self.__running = True

        while self.__running:
            self.redraw()

    def close(self):
        # Stop the loop
        self.__running = False


def main():
    win = Window(800, 600)
    win.wait_for_close()


main()
