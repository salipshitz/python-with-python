from distutils.core import setup
import py2exe
import window, screens

setup(
    console = [{
        "script": "mainloop.py",
        "dest_base": "LearnPythonWithPython"
    }]
)
