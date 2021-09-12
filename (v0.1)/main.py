""" @name Filenames Handler
    @version 0.1
    @description Helps in generating a list of the files in a directory (with multiple files). Warm regards, LiTBRo! ;)
    @author LiTBRo
    @source https://github.com/LiT-BRo
    @date 07 Sep 2021
"""

from tkinter import filedialog, Label, Frame, Tk, LabelFrame, Canvas, TOP, LEFT, Button, BOTTOM
from os import path, listdir

def addFolder():
    global files, directories
    file_dir = filedialog.askdirectory(initialdir="/", title="Select Folder")
    dir_files = listdir(file_dir)
    if len(dir_files) > 0:
        for file in dir_files:
            label = Label(main_frame, text=file, bg="grey")
            label.pack()
            files.append(file)
        directories.append(file_dir)
    else:
        print("\nALERT: Folder contains no files.\n")

def writeFile(filename, files, directories):
    if len(files) > 0:
        with open(filename, "a") as f:
            for dic in directories:
                f.write(f"{dic}\n")
            f.write("\n\n")
            for file in files:
                f.write(file+"\n")
        print("\nALERT: File write complete!\n")
    else:
        print("\nALERT: No files found to export.\n")

def fileCounterChecker():
    file_dir = path.normpath(path.expanduser("~/Desktop"))
    file_name = "\File_Names.txt"
    filename = file_dir+file_name
    counter = 1
    if path.exists(filename) == True:
        while True:
            filename = file_dir+f"\File_Names({counter}).txt"
            if path.exists(filename) == True:
                counter += 1
                pass
            else:
                writeFile(filename, files, directories)
                break
    else:
        writeFile(filename, files, directories)

def make_frame():
    global main_frame, files, directories
    files = []
    directories = []
    main_frame = Frame(misc_canvas, bg="white")
    main_frame.place(relwidth=1, relheight=1)

# # # # # # # # # #

# # Main-Window # #

# # # # # # # # # #

root = Tk()
root.title("Filenames Handler")
root.geometry("550x800")

root_wrapper = LabelFrame(root)
root_wrapper.pack(fill="both", expand="yes")

root_canvas = Canvas(root_wrapper, bg="#263D42") 
root_canvas.pack(fill="both", expand="yes")

misc_wrapper = LabelFrame(root_canvas) 
misc_wrapper.pack(side=TOP, fill="both", expand="yes", padx=27, pady=30)

misc_canvas = Canvas(misc_wrapper, bg="blue") 
misc_canvas.pack(fill="both", expand="yes")

make_frame()

# # # # # # # # # #

# # # Buttons # # #

# # # # # # # # # #

footer_frame = Frame(root)
footer_frame.pack(side=BOTTOM, padx=10, pady=6)

openf = Button(footer_frame, text="Open Folder", padx=7, pady=7, fg="white", bg="#263D42", command=addFolder)
openf.pack(side=LEFT)

execute = Button(footer_frame, text="Run", padx=15, pady=7, fg="white", bg="#263D42", command=fileCounterChecker)
execute.pack(side=LEFT, padx=70)

clear = Button(footer_frame, text="Clear Pane", padx=10, pady=7, fg="white", bg="#263D42", command=make_frame)
clear.pack(side=LEFT)

root.mainloop()