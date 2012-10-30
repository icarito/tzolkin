import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "tzolkin"], 
                    "include_files": ['tzolkin/images', 'tzolkin/images_big', 'tzolkin/tonos'],
                    "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Tzolkin",
        version = "0.1",
        description = "Sincronario de las 13 lunas",
        options = {"build_exe": build_exe_options},
        package_data={
        '': ['images/*.png', 'images_big/*.png', 'tonos/*.png'],
        },
        executables = [Executable("/home/icarito/Proyectos/tzolkin/tzolkin-applet.py", base=base)])


