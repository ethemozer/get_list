import os

from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()

current_directory = filedialog.askdirectory()
file_path = os.path.join(current_directory)
folder, directory = os.path.split(file_path)

try:
    list = os.listdir(file_path)

    desktop_file = os.path.join(os.environ['USERPROFILE'], 'Desktop\\list')
    if not os.path.exists(desktop_file):
        os.makedirs(desktop_file)

    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop\\list', directory + '.txt')
    file = open(desktop, "w")
    for x in list:
        file.write(x + "\n")
    file.close()
except Exception as ex:
    print(ex)