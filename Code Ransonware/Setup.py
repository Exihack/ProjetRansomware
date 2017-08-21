# import :
import sys, os
from cx_Freeze import setup, Executable

# Variables
# Nécessaire pour l'interface graphique, à adapter au besoin !
os.environ['TCL_LIBRARY'] = r'C:\Program Files (x86)\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files (x86)\Python36-32\tcl\tk8.6'

# Les dépendances sont normalements détectées mais, il est préférable de les spécifier.
# Les fichiers .dll sont nécéssaires pour le fonctionnement de l'interface graphique.
# ils doivent se trouver dans le même répertoire que le fichier "Main.py".
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


# Les applications GUI nécéssitent une base différente sous Windows.
# La base par défaut est faite pour les applications en console.
base = None
if sys.platform == "win32":
    base = "Win32GUI"


# Fonction de setup spécifiant certains paramètres.
setup(
        name = "ransonware",
        version = "0.1",
        description = "un vilain ransonware",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Main.py", base=base)]
    )
