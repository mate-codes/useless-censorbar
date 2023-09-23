import tkinter as tk
from tkinter import font

def center_label(event=None):
    x = (root.winfo_width() - label.winfo_reqwidth()) // 2
    y = (root.winfo_height() - label.winfo_reqheight()) // 2
    label.place(x=x, y=y)

root = tk.Tk()
root.geometry("300x70")
root.title('Useless Censor Bar')
root.configure(bg='black')
root.attributes("-topmost", True)

root.pack_propagate(False)

custom_font = font.Font(family="Helvetica", size=25, weight="bold")

label = tk.Label(root, text="CENCORED", font=custom_font, justify="center", bg="black", fg="white")
label.pack(fill="both", expand=True)

center_label()

root.bind("<Configure>", center_label)

root.mainloop()
