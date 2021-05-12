from tkinter import *

# Colors

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (255, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Functions


def create_display(width=600, height=600, caption="readyGame window"):
    window = Tk()
    window.geometry(f"{width}x{height}")
    window.title(caption)
    window.mainloop()


create_display()
