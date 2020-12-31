import os
from pathlib import Path
import tkinter as tk
from tkinter import PhotoImage

SUBDIRECTORIES = {
    "Documents": ['.pdf', '.rtf', '.txt', '.doc', '.docx', '.xls', '.xlsx', ".ppt", ".pptx", ".accdb"],
    "Images": ['.png', '.jpg', '.jpeg', '.heic', '.tiff', '.tif', '.jfif', '.gif', '.ico'],
    "Videos": ['.mp4', '.mov', '.avi'],
    "Audio": ['.mp3', '.m4a', '.m4b'],
    "Sharables": ['.zip', '.rar'],
    "Programming": ['.py', '.c', '.cpp', '.js', '.java', '.swift', '.php', '.html', '.css', '.pyc'],
    "Executables": ['.exe', '.ps1', '.msi'],
    "Remote Dekstop": ['.rdp']
}


def pickDir(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC"
def organizeDir():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDir(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))





root = tk.Tk()
root.title("Organizing Utility")

imagetest = PhotoImage(file="C:/Projects/File Keeper/Images/Picture2.png")



button_qwer = tk.Button(root, text="g", image=imagetest, command=organizeDir, bg='#5dbcd2')
button_qwer.pack()   # <-- don't forget to place the button in the window

root.mainloop()

