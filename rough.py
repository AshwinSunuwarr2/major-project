from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

import mysql.connector
from admin_log.forgotp import ForgetPass
from admin_log.after_login import AfterLogin
from admin_log.signup import SignUp


class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x850+70+0")
        title_color = "#6f86b9"
        self.root.config(bg=title_color)
        self.root.title("Criminal Face Recognition System")
        self.root.resizable(False, False)

        my_color = "#6f86b9"

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

        btn_login = Button(frm2, text="AUTHORITY ACCESS", width=20, cursor='hand2', fg="white", font=("Verdana", 16),
                           relief="flat", bg="#e13746", command=self.signin)
        btn_login.pack(side='left', padx=(0, 28))

        self.load_gif_frames()
        self.animate_gif()

    def signin(self):
        self.root.withdraw()
        self.signin_window = Toplevel(self.root)
        self.login_win = Logging(self.signin_window)

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


######################3##3     SIGNUP  ---------------

class SignUp:
    def __init__(self, root, log_win):
        self.root = root
        self.log_win = log_win
        self.root.geometry("1250x850+70+0")
        title_color = "#6f86b9"
        self.root.config(bg=title_color)
        self.root.title("Criminal Face Recognition System")
        self.root.resizable(False, False)

        my_color = "#6f86b9"

        style = ttk.Style()
        style.configure('TRoundedFrame.TFrame', background=my_color, borderwidth=5, relief='flat')

        lbl_title = Label(self.root, text="AUTHORITY ACCESS", font=("Courier new", 24, 'bold'), bg=title_color)
        lbl_title.pack(pady=20, ipadx=5, ipady=5)

        lbl_details = Label(self.root,
                            text="Create an account to access the Criminal Face Recognition System.\nFor authorized personnel only.",
                            font=("Verdana", 16), bg=my_color)
        lbl_details.pack(padx=5, ipadx=30, ipady=30)

        lbl_user = Label(self.root, text="USERNAME:", font=("Verdana", 16), bg=my_color)
        lbl_user.pack(pady=10)
        self.txt_user = Entry(self.root, font=("Verdana", 14))
        self.txt_user.pack(pady=10, ipady=3)

        lbl_pass = Label(self.root, text="PASSWORD:", font=("Verdana", 16), bg=my_color)
        lbl_pass.pack(pady=10)
        self.txt_pass = Entry(self.root, font=("Verdana", 14), show="*")
        self.txt_pass.pack(pady=10, ipady=3)

        lbl_confirm_pass = Label(self.root, text="CONFIRM PASSWORD:", font=("Verdana", 16), bg=my_color)
        lbl_confirm_pass.pack(pady=10)
        self.txt_confirm_pass = Entry(self.root, font=("Verdana", 14), show="*")
        self.txt_confirm_pass.pack(pady=10, ipady=3)

        btn_login = Button(self.root, text="LOGIN", width=20, cursor='hand2', fg="white", font=("Verdana", 16),
                           relief="flat", bg="#e13746", command=self.login)
        btn_login.pack(pady=(40, 10))

        lbl_forget = Label(self.root, text="Forgot Password?", font=("Verdana", 14), bg=my_color)
        lbl_forget.pack()
        lbl_forget.bind("<Button-1>", self.forgot_password)

        self.root.mainloop()

    def login(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()
        confirm_password = self.txt_confirm_pass.get()

        if username == '' or password == '' or confirm_password == '':
            messagebox.showerror("Error", "All fields are required!")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="criminaldb")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                conn.commit()
                messagebox.showinfo("Success", "Account created successfully!")
                self.root.destroy()
                self.log_win.root.deiconify()
            except mysql.connector.Error as e:
                messagebox.showerror("Error", str(e))

    def forgot_password(self, event):
        self.root.withdraw()
        self.fp_win = Toplevel(self.root)
        self.fp = ForgetPass(self.fp_win, self.log_win)


class Logging:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x850+70+0")
        title_color = "#6f86b9"
        self.root.config(bg=title_color)
        self.root.title("Criminal Face Recognition System")
        self.root.resizable(False, False)

        my_color = "#6f86b9"

        style = ttk.Style()
        style.configure('TRoundedFrame.TFrame', background=my_color, borderwidth=5, relief='flat')

        lbl_title = Label(self.root, text="AUTHORITY ACCESS", font=("Courier new", 24, 'bold'), bg=title_color)
        lbl_title.pack(pady=20, ipadx=5, ipady=5)

        lbl_details = Label(self.root, text="Log in to the Criminal Face Recognition System.\nFor authorized personnel only.",
                            font=("Verdana", 16), bg=my_color)
        lbl_details.pack(padx=5, ipadx=30, ipady=30)

        lbl_user = Label(self.root, text="USERNAME:", font=("Verdana", 16), bg=my_color)
        lbl_user.pack(pady=10)
        self.txt_user = Entry(self.root, font=("Verdana", 14))
        self.txt_user.pack(pady=10, ipady=3)

        lbl_pass = Label(self.root, text="PASSWORD:", font=("Verdana", 16), bg=my_color)
        lbl_pass.pack(pady=10)
        self.txt_pass = Entry(self.root, font=("Verdana", 14), show="*")
        self.txt_pass.pack(pady=10, ipady=3)

        btn_login = Button(self.root, text="LOGIN", width=20, cursor='hand2', fg="white", font=("Verdana", 16),
                           relief="flat", bg="#e13746", command=self.login)
        btn_login.pack(pady=(40, 10))

        lbl_signup = Label(self.root, text="Sign up for an account", font=("Verdana", 14), bg=my_color)
        lbl_signup.pack()
        lbl_signup.bind("<Button-1>", self.signup)

        self.root.mainloop()

    def login(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()

        if username == '' or password == '':
            messagebox.showerror("Error", "Username and password are required!")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="criminaldb")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
                row = cursor.fetchone()

                if row is not None:
                    self.root.destroy()
                    self.al = AfterLogin()
                else:
                    messagebox.showerror("Error", "Invalid username or password!")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", str(e))

    def signup(self, event):
        self.root.withdraw()
        self.signup_win = Toplevel(self.root)
        self.signup = SignUp(self.signup_win, self)


root = Tk()
FaceRecognitionAppGUI = FaceRecognitionApp(root)
root.mainloop()






# import tkinter as tk


# class Window1:
#     def __init__(self, master):
#         self.master = master
#         master.title("Window 1")
#         self.button = tk.Button(master, text="Go to Window 2", command=self.open_window2)
#         self.button.pack(pady=10)

#     def open_window2(self):
#         self.master.withdraw()
#         self.new_window = tk.Toplevel(self.master)
#         self.app = Window2(self.new_window, self)

        
# class Window2:
#     def __init__(self, master, window1):
#         self.master = master
#         self.window1 = window1
#         master.title("Window 2")
#         self.button = tk.Button(master, text="Go to Window 1", command=self.open_window1)
#         self.button.pack(pady=10)

#     def open_window1(self):
#         self.master.destroy()
#         self.window1.master.deiconify()


# root = tk.Tk()
# app = Window1(root)
# root.mainloop()
