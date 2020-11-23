import os, sys, ctypes
import winreg as reg

# Get path of current working directory and python.exe
cwd = os.getcwd()
python_exe = sys.executable

# Set the path of the context menu (right-click menu)
key_path = r'Directory\\Background\\shell\\Movie Selector\\' # Change 'Organiser' to the name of your project

# Checks if key make is run in admin mode. If not, re-run key-maker.py as admin.
if ctypes.windll.shell32.IsUserAnAdmin():
    # Create outer key
    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
    reg.SetValue(key, '', reg.REG_SZ, "Movie Selector")  # Creates Movie Selector key
    reg.SetValueEx(key, 'Icon', 0,  reg.REG_SZ, f'{cwd}\\film.ico')  # Creates icon key in Movie Selector key

    # create inner key
    key2 = reg.CreateKey(key, r"command")
    reg.SetValue(key2, '', reg.REG_SZ, python_exe + f' "{cwd}\\movie-selector.py"') # Creates command key and assigns it the python.exe and script file paths.
else:
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, 'key-maker.py', None, 1)








