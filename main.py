#!/usr/bin/env python

try:
    from Tkinter import Tk
except ImportError:
    from tkinter import Tk

from palette import Palette

if __name__ == "__main__":
    root = Tk()
    app = Palette(root)

    root.mainloop()

    try:
        root.destroy()
    except:
        pass
