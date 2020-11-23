import random
import win32api
import os
from os import listdir
from pathlib import Path

# Get current directory
cwd = Path.cwd()

# Get list of all folders and files in directory
directories = listdir(cwd)

# Randomly select one folder/file
directory = random.choice(directories)

# Append randomly chosen folder/file to current directory
directory_path = cwd / Path(directory)

# Open it up.
os.startfile(directory_path)


