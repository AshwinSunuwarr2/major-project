from tkinter import *
from tkinter import ttk, messagebox
from tkinter import messagebox, ttk, filedialog

from PIL import Image, ImageTk
import mysql.connector


main_color = "#6f86b9"
main_font = "Courier new"


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x850+70+0")
        title_color = "#6f86b9"
        self.root.config(bg=title_color)
        self.root.title("Criminal Face Recognition System")
        self.root.resizable(False, False)

        lbl_text = Label(self.root, text="Canvas and frm_add are two different widgets in the Tkinter GUI toolkit in Python,\n and they have different purposes.",
                                font=(main_font, 18, 'bold'))
        lbl_text.place(x=30, y=60)


if __name__ == "__main__":
    root = Tk()
    help_window = Help(root)
    root.mainloop()