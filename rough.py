from tkinter import Frame, Tk, Label, Button, Canvas
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

class Application:
    def __init__(self, root):
        self.root = root
        root.state("zoomed")
        self.root.resizable(False, False)
        self.root.config(bg="grey")

        # frm1 = Frame(self.root, bg="black")
        # frm1.place(x=0, y=0)

        # img = Image.open("bg_img/transparent.png")
        # resized = img.resize((220,215), Image.LANCZOS)
        # enhancer = ImageEnhance.Brightness(resized)
        # dark_image = enhancer.enhance(0.45)
        # self.btn_img = ImageTk.PhotoImage(dark_image)

        # lbl = Label(self.root, text="label for transparent", highlightbackground=1)
        
        canvas = Canvas(root, width=400, height=200, highlightthickness=0, highlightbackground=root["bg"])
        canvas.pack()

        label_text = "Hello, Transparent Label!"

        label = canvas.create_text(200, 100, text=label_text, font=("Arial", 18), fill="black", anchor="center")

        
if __name__=="__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
