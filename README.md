py-material-palette
===

A Material Palette color picker with Python and tkinter. Largely inspired from [mike-schultz/materialette](https://github.com/mike-schultz/materialette).

![capture](https://cloud.githubusercontent.com/assets/3540471/19632389/8c3f8f5e-99d8-11e6-88c3-ccf3db978def.png)


#### About

I stumbled upon the [materialette](https://github.com/mike-schultz/materialette) repository, and I thought it could have been a lot lighter. Since I am learning Python and have not really tried GUI with Python yet, I tried to remake something similar with Python. But honestly, one should consider using SASS or something instead of depending on an application like this for web development.


#### Features

- Supports HEX, RGB, HSV and HSL (courtesy of [Python's colorsys](https://docs.python.org/3/library/colorsys.html))
- Copies the selected color code when clicked
- Supported and tested on both Python 2.7.12 and 3.5.2
- Does not run on OS dock :^)
- No additional requirements, just vanilla Python and tkinter


#### Running

```py
# if you are on python 2
python ./main.py

# or if you are on python 3
python3 ./main.py

# there is a python shebang, but it really depends on your env's defined python version
./main.py
```


#### Credits

- materialette for the [inspiration](https://github.com/mike-schultz/materialette)
- Google for the [colors](https://material.google.com/style/color.html)
- effbot for all the [tkinter documentation](http://effbot.org/tkinterbook/)
- StackOverflow for a [simple HEX to RGB in Python](http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa)
- Michael Lange for a [tkinter Tooltip](http://tkinter.unpythonic.net/wiki/ToolTip)
