""" @name Filenames Handler
    @version 0.0.1
    @description Helps in generating a list of the files in a directory (with multiple files). Warm regards, LiTBRo! ;)
    @author LiTBRo
    @source https://github.com/LiT-BRo
    @date 31 Aug 2021
"""

import tkinter as tk
from tkinter import filedialog
import os

# # # # # # # # # #

# # Main-Window # #

# # # # # # # # # #

root = tk.Tk()
files = []

def addFolder():
    file_dir = filedialog.askdirectory(initialdir="/", title="Select Folder")
    global files 
    files = os.listdir(file_dir)
    for file in files:
        label = tk.Label(frame, text=file, bg="grey")
        label.pack()

def writeFile(filename, files):
    with open(filename, "a") as f:
        for file in files:
            f.write(file+"\n")
    print("File Write Complete!")

def fileChecker():
    file_dir = os.path.normpath(os.path.expanduser("~/Desktop"))
    file_name = "\File_Names.txt"
    filename = file_dir+file_name
    counter = 1
    if os.path.exists(filename) == True:
        while True:
            filename = file_dir+f"\File_Names({counter}).txt"
            if os.path.exists(filename) == True:
                counter += 1
                pass
            else:
                writeFile(filename, files)
                break
    else:
        writeFile(filename, files)

# # # # # # # # # #

# # # Buttons # # #

# # # # # # # # # #

canvas = tk.Canvas(root,height=700, width=550, bg="#263D42", scrollregion=(0,0,500,500))
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.9, relheight=0.82, relx=0.05, rely=0.04)

openf = tk.Button(root, text="Open Folder", padx=15, pady=7, fg="white", bg="#263D42", command=addFolder)
openf.place(relwidth=0.2,relheight=0)
openf.pack()

execute = tk.Button(root, text="Run", padx=15, pady=7, fg="white", bg="#263D42", command=fileChecker)
execute.place(relwidth=0.2,relheight=0)
execute.pack()

root.mainloop()