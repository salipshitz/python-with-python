from distutils import setup
import py2exe
import windows, screen

setup(
    windows = [{
        "script": "mainloop.py",
        "dest_base": "LearnPythonWithPython"
    }]
)
