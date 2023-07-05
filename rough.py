from tkinter import *
from PIL import ImageTk, Image, ImageEnhance
import mysql.connector
import io


class Rough:
        def __init__(self, root):
                self.root = root 
                self.root.geometry("950x640")
                frm1 =Frame(self.root, bg="grey")
                frm1.place(x=0, y=0, relheight=1, relwidth=1)

                image_path = "bg_img/home_bg.jpg"
                image = Image.open(image_path)
                bg_image = ImageTk.PhotoImage(image)

                bg_label = Label(frm1, text="Criminal Face Recognition System", font=("courier new", 12, "bold"), fg="black", image=bg_image, bg=None, compound="center")
                bg_label.place(x=100, y=100, height=400, width=400)
                
                frm2 = Frame(bg_label, bg=None)
                frm2.place(x=8, y=8, height=300, width=250)

                # lbl_text = Label(frm1, bg=main_color, text="Ashwin181209@ncit.edu.np\n Irajk181216@ncit.edu.np\n Ishan181217@ncit.edu.np",
                #                         font=(main_font, 18, 'bold'))
                # lbl_text.place(x=50, y=60, anchor='w')

                # ===============  frames for devs details  ==================#
                frm_ashwin = Frame(frm1, bg="blue")
                frm_ashwin.place(x=950, y=200, height=350, width=350, anchor="nw")

if __name__ == "__main__":
      root = Tk()
      rough_window = Rough(root)
      root.mainloop()
