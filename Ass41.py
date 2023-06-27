import tkinter as tk

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Two Labels Example")

        self.label1 = tk.Label(self.window, text="Label 1", bg="red")
        self.label1.pack()

        self.label2 = tk.Label(self.window, text="Label 2", bg="blue")
        self.label2.pack()

        self.window.mainloop()

if __name__ == "__main__":
    MainWindow()
