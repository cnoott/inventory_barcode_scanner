import tkinter as tk
root = tk.Tk()

#constants
HEIGHT = 700
WIDTH = 400


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

button = tk.Button(canvas, text="Select folder")
button.place(relx=0.1, rely=0.1)

root.mainloop()
