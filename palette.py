try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from os.path import join
from tooltip import ToolTip
import colorsys
import json
import sys


class Palette:
    master = None

    mode_options = [
        'hex',
        'rgb',
        'hsv',
        'hsl',
    ]

    mode_var = None
    status_text = None

    def __init__(self, master):
        self.master = master
        self.res_path = join(sys.path[0], 'res')

        self.master.wm_title('Material Palette')
        self.master.iconbitmap(default=join(self.res_path, 'transparent.ico'))
        self.master.resizable(width=False, height=False)

        self.init_color_frame()
        self.init_mode_frame()
        self.init_status_frame()

    def init_color_frame(self):
        colors_filepath = join(self.res_path, 'colors.json')

        with open(colors_filepath) as f:
            colors = json.load(f)

        color_frame = tk.Frame(self.master)

        for row_count, color in enumerate(colors):
            main_color = color['mainColor']
            sub_colors = color['children']

            for col_count, sub_color in enumerate(sub_colors):
                sub_color_label = tk.Label(
                    color_frame, bg=sub_color['subColor'], width=3, bd=1, relief=tk.RIDGE,
                )

                sub_color_label.grid(row=row_count, column=col_count)

                tooltip_text = '\n'.join([
                    main_color,
                    sub_color['subColor'],
                ])

                tooltip_color = 'white'
                if sub_color['isTextDark']:
                    tooltip_color = 'black'

                ToolTip(
                    sub_color_label, follow_mouse=1, text=tooltip_text, delay=0,
                    padx=40, pady=20, bg=sub_color['subColor'], fg=tooltip_color,
                    justify='center'
                )

                sub_color_label.bind("<Button-1>", self.label_onclick)

        color_frame.pack()

    def init_mode_frame(self):
        mode_frame = tk.Frame(self.master)
        self.mode_var = tk.StringVar()
        self.mode_var.set('hex')

        for col, option in enumerate(self.mode_options):
            tk.Radiobutton(
                mode_frame, text=option.upper(), variable=self.mode_var,
                value=option, padx=6
            ).grid(row=0, column=col)

        mode_frame.pack()

    def init_status_frame(self):
        status_frame = tk.Frame(self.master, bd=1, relief=tk.SUNKEN)
        self.status_text = tk.StringVar()
        self.status_text.set('Ready')

        tk.Label(status_frame, textvariable=self.status_text).grid()
        status_frame.pack(fill=tk.X)

    def label_onclick(self, event):
        color = event.widget.cget("bg")
        mode = self.mode_var.get()

        if mode == 'rgb':
            color = self.hex_to_rgb(color)
            color = ', '.join(str(i) for i in color)
            color = 'rgb(' + color + ')'
        elif mode == 'hsv':
            color = self.hex_to_rgb(color, decimal=True)
            color = colorsys.rgb_to_hsv(*color)

            color = 'hsv({h:.0f}, {s:.0f}%, {v:.0f}%)'.format(
                h=(color[0] * 360),
                s=(color[1] * 100),
                v=(color[2] * 100),
            )
        elif mode == 'hsl':
            color = self.hex_to_rgb(color, decimal=True)
            color = colorsys.rgb_to_hls(*color)

            color = 'hsl({h:.0f}, {s:.0f}%, {li:.0f}%)'.format(
                h=(color[0] * 360),
                li=(color[1] * 100),
                s=(color[2] * 100),
            )

        self.status_text.set('Copied "{}" to clipboard'.format(color))

        self.master.clipboard_clear()
        self.master.clipboard_append(color)

    def hex_to_rgb(self, value, decimal=False):
        # http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa
        value = value.lstrip('#')
        lv = len(value)

        # return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        rgb = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

        if decimal:
            rgb = [i / 255.0 for i in rgb]

        return rgb
