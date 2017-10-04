from setuptools import setup

APP = ['mainloop.py']
APP_NAME = "LearnPythonWithPython"
APP_IDENTIFIER = "com.saardeveloper.python-with-python"
APP_VERSION = "1.BETA.2"
APP_VERSION_SHORT = "Beta 2"
MODULES=['window', 'screens']
DATA_FILES = []
OPTIONS = {
    'argv_emulator': True,
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleIdentifier': APP_IDENTIFIER,
        'CFBundleVersion': APP_VERSION,
        'CFBundleShortVersionString': APP_VERSION_SHORT
    }
}

setup(
    name=APP_NAME,
    py_modules=MODULES
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
