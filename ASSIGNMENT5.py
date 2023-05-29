import tkinter as tk
from tkinter import Menu

def file_new():
    print("New File")

def file_open():
    print("Open File")

def file_save():
    print("Save File")

def edit_cut():
    print("Cut")

def edit_copy():
    print("Copy")

def edit_paste():
    print("Paste")

root = tk.Tk()
root.title("Menu Bar Example")

# Create the menu bar
menu_bar = Menu(root)

# Create the File menu and its sub-items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_command(label="Save", command=file_save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create the Edit menu and its sub-items
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=edit_copy)
edit_menu.add_command(label="Paste", command=edit_paste)

# Add the File and Edit menus to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Attach the menu bar to the root window
root.config(menu=menu_bar)

root.mainloop()
