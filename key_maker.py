import os
import sys
import winreg as reg

# Get path of current working directory and python.exe
cwd = os.getcwd()
python_exe = sys.executable

# optional hide python terminal in windows
hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"

# Set the path of the context menu (right-click menu)
key_path = r'Directory\\Background\\shell\\Movie Selector\\' # Change 'Organiser' to the name of your project

# Create outer key
key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, "Movie Selector")  # Creates Movie Selector key
reg.SetValueEx(key, 'Icon', 0,  reg.REG_SZ, f'{cwd}\\film.ico')  # Creates icon key in Movie Selector key

# create inner key
key2 = reg.CreateKey(key, r"command")
reg.SetValue(key2, '', reg.REG_SZ, python_exe + f' "{cwd}\\movie-selector.py"') # Creates command key and assigns it the python.exe and script file paths.
