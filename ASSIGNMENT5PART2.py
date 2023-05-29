import tkinter as tk

root = tk.Tk()
root.title("Colored Labels Example")

# Create the first label with a blue background
label1 = tk.Label(root, text="Label 1", bg="black", fg="white")
label1.pack()

# Create the second label with a green background
label2 = tk.Label(root, text="Label 2", bg="green", fg="white")
label2.pack()

root.mainloop()
