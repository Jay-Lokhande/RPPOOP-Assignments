import tkinter as tk

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Menu Example")

        # create a menu bar
        menubar = tk.Menu(self.window)

        # create a file menu and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # display the menu bar
        self.window.config(menu=menubar)

        self.window.mainloop()

if __name__ == "__main__":
    MainWindow()
