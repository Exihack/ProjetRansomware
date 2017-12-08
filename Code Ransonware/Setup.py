# import :
import sys, os
from cx_Freeze import setup, Executable

# Variables
# Needed for the GUI, to adapt if necessary !
os.environ['TCL_LIBRARY'] = r'C:\Program Files (x86)\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files (x86)\Python36-32\tcl\tk8.6'

# The dependencies are normally detected but it's better to specify them
# The .dll files are necessary for the GUI to work
build_exe_options = {"packages": ["cffi",
                                  "cryptography",
                                  "idna",
                                  "threading",
                                  "os",
                                  "ssl",
                                  "socket",
                                  "platform",
                                  "tkinter",
                                  "functools"],
                     "include_files": ["tcl86t.dll", "tk86t.dll"]}



# GUI applications require a different base on Windows.
# The default base is for console applications.
base = None
if sys.platform == "win32":
    base = "Win32GUI"


# Setup function, specifying some parameters
setup(
        name = "ransomware",
        version = "2.1",
        description = "a nasty ransomware",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Main.py", base=base)]
    )