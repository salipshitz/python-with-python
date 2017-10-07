from distutils.core import setup
import py2exe
import window, screens

setup(
    console = [{
        "script": "mainloop.py",
        "icon_resources": [(1, "pycon-icon.ico")],
        "dest_base": "LearnPythonWithPython"
    }]
)
