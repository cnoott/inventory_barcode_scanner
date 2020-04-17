import tkinter as tk
root = tk.Tk()

#constants
HEIGHT = 700
WIDTH = 800
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
button = tk.Button(root, text="BUDDON")
button.pack()

root.mainloop()
