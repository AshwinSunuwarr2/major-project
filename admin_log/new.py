# import tkinter as tk
# from tkinter import ttk, Toplevel
# from PIL import Image, ImageTk

# root = tk.Tk()
# root.geometry("1190x700")

# title_color = "#6f86b9"
# root.config(bg=title_color, padx=20, pady=20)
# root.title("Criminal Face Recognition System")

# my_color = "#6f86b9"

# style = ttk.Style()
# style.configure('TRoundedFrame.TFrame', background=my_color, borderwidth=5, relief='flat')


# ############## signup window  ############
# def nav_signup():

#     root.withdraw()
#     import signup as signup

# ##############  login window  ############
# def nav_login():
#     root.destroy()
#     import login as login

#     '''root.withdraw()
    
#     log_w = tk.Toplevel(root)
#     log_w.geometry("720x560")
#     log_w.resizable(False, False)
    
#     my_font = "Courier new"
#     frm = tk.Frame(log_w, width=850, height=660, bg="white")
#     frm.place(x=0, y=0)

#     lbl_head = tk.Label(frm, text="Sign in", bg="white", fg="orange", font=(my_font, 28, "bold"))
#     lbl_head.place(x=170, y=80)


#     def on_enter(e):
#         user.delete(0, "end")

#     def on_leave(e):
#         name = user.get()
#         if name == '':
#             user.insert(0, "Username")

#     # username label
#     user = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(my_font, 18))
#     user.place(x=170, y=170)
#     user.insert(0, "Username")
#     user.bind('<FocusIn>', on_enter)
#     user.bind('<FocusOut>', on_leave)

#     tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=203)

#     def on_enter(e):
#         psw.delete(0, "end")

#     def on_leave(e):
#         name = psw.get()
#         if name == '':
#             psw.insert(0, "Password")

#     # password label
#     psw = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(my_font, 18))
#     psw.place(x=170, y=270)
#     psw.insert(0, "Password")
#     psw.bind('<FocusIn>', on_enter)
#     psw.bind('<FocusOut>', on_leave)

#     tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=303)

#     btn_log = tk.Button(frm, text="SIGN IN", width=18, bg="orange", cursor='hand2', fg="white", font=(my_font, 16, "bold"),relief="flat", border=0)
#     btn_log.place(x=200, y=350)

#     # sign up or forgot pass
#     lbl_signup = tk.Label(frm, text="Don't have an account?", bg="white", fg="black", font=(my_font, 12))
#     lbl_signup.place(x=165, y=440)
#     btn_signup = tk.Button(frm, text="Sign up", border=0, cursor="hand2", font=(my_font, 12, "italic"), relief="flat", fg="red", bg="white")
#     btn_signup.place(x=390, y=439)


#     log_w.deiconify()'''

# #########  Root Contd  ###############
# def animate_gif():
#     global frame_index

#     frame = gif_frames[frame_index]
#     disp_frame = ImageTk.PhotoImage(frame)
#     lbl_icon.configure(image=disp_frame)
#     lbl_icon.image = disp_frame

#     frame_index = (frame_index + 1) % len(gif_frames)
#     root.after(100, animate_gif)

# # Load the animated GIF frames
# gif = Image.open("icon_img/eye.gif")
# gif_frames = []
# try:
#     while True:
#         frame = gif.copy()
#         frame.thumbnail((250, 250))
#         gif_frames.append(frame)
#         # Seek next frame
#         gif.seek(len(gif_frames))
# except EOFError:
#     pass

# frame_index = 0

# lbl_title = tk.Label(root, text="CRIMINAL FACE RECOGNITION SYSTEM", font=("Courier new", 24, 'bold'), bg=title_color)
# lbl_title.pack(pady=20, ipadx=5, ipady=5)

# # #canvas 
# # canvas = tk.Canvas(root, bg="white")
# # canvas.pack(fill='both', expand=True, ipadx=40, ipady=0)

# #frame 1
# frm1 = ttk.Frame(root, style='TRoundedFrame.TFrame')
# frm1.pack()

# lbl_icon = tk.Label(frm1, bg=my_color)
# lbl_icon.pack()

# lbl_details = tk.Label(frm1, text="Detects human faces through live footage and recognize them.\nBetter than other biometric scanners which require very close physical presence.\nLearn more about us below.",
#                        font=("Verdana", 16), bg=my_color)
# lbl_details.pack(padx=5, ipadx=30, ipady=30)

# #frame 2
# frm2 = tk.Frame(frm1)
# frm2.pack(padx=10, pady=50)
# frm2.configure(background=my_color)

# btn_login = tk.Button(frm2, text="LOGIN", width=14, cursor='hand2', fg="white", font=("Verdana", 16), relief="flat", bg="#e13746", command=nav_login)
# btn_login.pack(side='left', padx=(0, 20))

# btn_signup = tk.Button(frm2, text="SIGN UP", width=14, cursor='hand2', fg="white", font=("Verdana", 16), relief="flat", bg="#432771", command=nav_signup)
# btn_signup.pack(side='right', padx=(20, 0))

# btn_learn_more = tk.Button(frm1, text="Learn more about us.", cursor='hand2',fg="black", border=0, font=("Verdana", 11, "italic", "underline"), relief="flat", bg=my_color)
# btn_learn_more.pack(pady=5)

# animate_gif()

# root.mainloop()


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from login import Logging



class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x850+70+0")
        title_color = "#6f86b9"
        self.root.config(bg=title_color)
        self.root.title("Criminal Face Recognition System")
        self.root.resizable(False, False)

        my_color = "#6f86b9"


        outmenu_bar = Menu(self.root)
        self.root.config(menu=outmenu_bar)

        home_menu = Menu(outmenu_bar, tearoff=0)
        home_menu.add_command(label='Home page')
        home_menu.add_separator()
        home_menu.add_command(label="Exit", command=self.root.quit)
        outmenu_bar.add_cascade(label="HOME", menu=home_menu)

        user_menu = Menu(outmenu_bar, tearoff=0)
        user_menu.add_command(label="Sign in")
        user_menu.add_separator()
        user_menu.add_command(label="Sign up")
        outmenu_bar.add_cascade(label="USER", menu=user_menu)



        style = ttk.Style()
        style.configure('TRoundedFrame.TFrame', background=my_color, borderwidth=5, relief='flat')

        lbl_title = Label(self.root, text="CRIMINAL FACE RECOGNITION SYSTEM", font=("Courier new", 24, 'bold'),
                          bg=title_color)
        lbl_title.pack(pady=20, ipadx=5, ipady=5)

        self.gif_frames = []

        self.lbl_icon = Label(self.root, bg=my_color)
        self.lbl_icon.pack()

        lbl_details = Label(self.root,
                            text="Detects human faces through live footage and recognizes them.\nBetter than other biometric scanners which require very close physical presence.\nLearn more about us below.",
                            font=("Verdana", 16), bg=my_color)
        lbl_details.pack(padx=5, ipadx=30, ipady=30)

        frm2 = Frame(self.root)
        frm2.pack(padx=10, pady=50)
        frm2.configure(background=my_color)

        btn_login = Button(frm2, text="LOGIN", width=14, cursor='hand2', fg="white", font=("Verdana", 16),
                           relief="flat", bg="#e13746", command=self.signin)
        btn_login.pack(side='left', padx=(0, 20))

        btn_signup = Button(frm2, text="SIGN UP", width=14, cursor='hand2', fg="white", font=("Verdana", 16),
                            relief="flat", bg="#432771")
        btn_signup.pack(side='right', padx=(20, 0))

        self.load_gif_frames()
        self.animate_gif()

    def signin(self):
            self.new_window = Toplevel(self.root)
            self.login_win = Logging(self.new_window)     

    def load_gif_frames(self):
        gif = Image.open("icon_img/eye.gif")
        try:
            while True:
                frame = gif.copy()
                frame.thumbnail((250, 250))
                self.gif_frames.append(frame)
                gif.seek(len(self.gif_frames))
        except EOFError:
            pass

    def animate_gif(self):
        if self.gif_frames:
            frame_index = getattr(self, 'frame_index', 0)
            frame = self.gif_frames[frame_index]
            disp_frame = ImageTk.PhotoImage(frame)
            self.lbl_icon.configure(image=disp_frame)
            self.lbl_icon.image = disp_frame

            frame_index = (frame_index + 1) % len(self.gif_frames)
            setattr(self, 'frame_index', frame_index)
            self.root.after(100, self.animate_gif)


if __name__ == "__main__":
    root = Tk()
    outbase = FaceRecognitionApp(root)
    root.mainloop()





