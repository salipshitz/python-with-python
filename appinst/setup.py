from distutils import setup
import py2exe
import windows, screen

setup(
    options = {'py2exe': {'bundle_files': 1}}
    zipFile = None
    windows = [{
        "script": "mainloop",
        "icon_resources": [(1, "pycon-icon.ico")]
        "dest_base": "LearnPythonWithPython"
    }]
)
