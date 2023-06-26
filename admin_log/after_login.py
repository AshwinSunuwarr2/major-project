from tkinter import *
from tkinter import ttk, messagebox
from tkinter import messagebox, ttk, filedialog

from PIL import Image, ImageTk
import mysql.connector


main_color = "#6f86b9"
main_font = "Courier new"


class AfterLogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x850+70+0")
        title_color = "#6f86b9"
        self.root.config(bg=title_color)
        self.root.title("Criminal Face Recognition System")
        self.root.resizable(False, False)


        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        # Create File menu
        home_menu = Menu(menu_bar, tearoff=0)
        home_menu.add_command(label="Add criminal details")
        home_menu.add_command(label="Update criminal details")
        home_menu.add_command(label="Delete criminal details")
        home_menu.add_separator()
        home_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="Home", menu=home_menu)

        # Create Help menu
        data_menu = Menu(menu_bar, tearoff=0)
        data_menu.add_command(label="View criminal details")
        data_menu.add_command(label="View dataset")
        data_menu.add_separator()
        # data_menu.add_command(label="Exit", command=data_menu.quit)
        menu_bar.add_cascade(label="Datasets", menu=data_menu)

        cam_menu = Menu(menu_bar, tearoff=0)
        cam_menu.add_command(label="Recognize criminals", command=self.help)
        menu_bar.add_cascade(label="Camera", menu=cam_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Help")
        help_menu.add_command(label="About us")
        help_menu.add_cascade(label="More", menu=help_menu)



        self.var_entry_name = StringVar()
        self.var_entry_newpass = StringVar()
        self.var_entry_confirmpass = StringVar()


#-------------   functions  --------------------#

    def help(self):
        frm1 =Frame(self.root, width = 1250, height = 850, bg="yellow")
        frm1.place(x=0, y=0)
        lbl_text = Label(frm1, text="Canvas and frm_add are two different widgets in the Tkinter GUI toolkit in Python,\n and they have different purposes.",
                                font=(main_font, 18, 'bold'))
        lbl_text.place(x=30, y=60)
        




if __name__ == "__main__":
    root = Tk()
    main_window = AfterLogin(root)
    root.mainloop()





