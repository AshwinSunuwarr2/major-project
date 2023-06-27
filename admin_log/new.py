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
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

import mysql.connector
from forgotp import ForgetPass
from after_login import AfterLogin
from signup import SignUp


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

        # btn_signup = Button(frm2, text="SIGN UP", width=14, cursor='hand2', fg="white", font=("Verdana", 16),
        #                     relief="flat", bg="#432771", command=self.sign_reg)
        # btn_signup.pack(side='right', padx=(20, 0))

        self.load_gif_frames()
        self.animate_gif()

    def signin(self):
        self.root.withdraw()
        self.signin_window = Toplevel(self.root)
        self.login_win = Logging(self.signin_window)   

    # def sign_reg(self):
    #     self.root.withdraw()
    #     self.signup_window = Toplevel(self.root)
    #     self.signup_win = SignUp(self.signup_window)

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

        signup_color = "#432771"
        signup_font = "Courier new"

        self.var_user = StringVar()
        self.var_psw = StringVar()
        self.var_cpsw = StringVar()

        frm_color = "#6f86b9"

        frm = Frame(self.root, width=800, height=550, bg=frm_color)
        frm.place(x=200, y=100)

        lbl_head = Label(frm, text="Sign up", bg=frm_color, fg=signup_color, font=(signup_font, 28, "bold"))
        lbl_head.place(x=170, y=80)


        def on_enter(e):
            user.delete(0, "end")

        def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0, "Username")

        # username label
        user = Entry(frm, textvariable=self.var_user, width=32, fg="black", border=0, bg=frm_color, font=(signup_font, 16))
        user.place(x=170, y=158)
        user.insert(0, "Username")
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        Frame(frm, width=350, height=2, bg="black").place(x=169, y=183)

        def on_enter(e):
            psw.delete(0, "end")

        def on_leave(e):
            name = psw.get()
            if name == '':
                psw.insert(0, "Password")

        # password label
        psw = Entry(frm, textvariable=self.var_psw, width=32, fg="black", border=0, bg=frm_color, font=(signup_font, 16))
        psw.place(x=170, y=225)
        psw.insert(0, "Password")
        psw.bind('<FocusIn>', on_enter)
        psw.bind('<FocusOut>', on_leave)

        Frame(frm, width=350, height=2, bg="black").place(x=169, y=250)

        def on_enter(e):
            c_psw.delete(0, "end")

        def on_leave(e):
            name = c_psw.get()
            if name == '':
                c_psw.insert(0, "Confirm Password")

        # confirm password label
        c_psw = Entry(frm, textvariable=self.var_cpsw, width=32, fg="black", border=0, bg=frm_color, font=(signup_font, 16))
        c_psw.insert(0, "Confirm Password")
        c_psw.place(x=170, y=295)
        c_psw.bind('<FocusIn>', on_enter)
        c_psw.bind('<FocusOut>', on_leave)

        Frame(frm, width=350, height=2, bg="black").place(x=169, y=320)

        btn_signup = Button(frm, text="SIGN UP", width=18, bg=signup_color, cursor='hand2', fg=frm_color, font=(signup_font, 16, "bold"),relief="flat", border=0, command=self.signup_db)
        btn_signup.place(x=200, y=360)

        # sign up btn
        lbl_signup = Label(frm, text="Already have an account?", bg=frm_color, fg="black", font=(signup_font, 12))
        lbl_signup.place(x=160, y=440)
        btn_log = Button(frm, text="Sign in", border=0, cursor="hand2", font=(signup_font, 12, "italic bold"), relief="flat", fg="#e13746", bg=frm_color, command=self.signin)
        btn_log.place(x=407, y=439)


    def signin(self):
        self.root.destroy()
        self.log_win.root.deiconify()
        
        # self.root.withdraw()
        # self.signin_window = Toplevel(self.root)
        # self.signin_win = Logging(self.signup_window)
    
# sign up confiramtion
    def signup_db(self):
        name = self.var_user.get()
        passw = self.var_psw.get()
        c_passw = self.var_cpsw.get()


        if name ==  'Username' or passw == 'Password' or c_passw == 'Confirm password':
            messagebox.showerror('Invalid', 'Please fill fields properly', parent=self.root)
            return

        if passw != c_passw:
            messagebox.showerror('Invalid', 'Both password should match.', parent=self.root)
            return

        if len(passw) < 8:
            messagebox.showerror('Invalid', 'Password must be atleast of 8 characters.', parent=self.root)
            return

        conn = mysql.connector.connect(
        host  = 'localhost',
        user = 'root',
        password = '',
        database = 'mydb',
        port = '3306'
         )

        c = conn.cursor()
        insert_admin = "insert into admins(user, password) values (%s, %s)"
        vals = (name, passw)
        
        try:
            c.execute(insert_admin, vals)
            conn.commit()
            conn.close()
            messagebox.showinfo('Success', "You're now registered.", parent=self.root)
            self.root.withdraw()
            self.signin_window = Toplevel(self.root)
            self.signin_win = Logging(self.signin_window) 
            
            return
        
        except mysql.connector.Error as error:
            messagebox.showerror('Database error', str(error), parent=self.root)

        self.var_user.delete(0, END)
        self.var_psw.delete(0, END)
        self.var_cpsw.delete(0, END)









##########################3    LOGIN -------------



class Logging:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x850+70+0")
        title_color = "#6f86b9"
        self.root.config(bg=title_color)
        self.root.title("Criminal Face Recognition System")
        self.root.resizable(False, False)

        login_color = "#e13746"
        login_font = "Courier new"
        self.var_user = StringVar()
        self.var_psw = StringVar()


        frm = Frame(self.root, width=800, height=550, bg="white")
        frm.place(x=200, y=100)

        lbl_head = Label(frm, text="Sign in", bg="white", fg=login_color, font=(login_font, 28, "bold"))
        lbl_head.place(x=170, y=80)


        def on_enter(e):
            user.delete(0, "end")


        def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0, "Username")


        user = Entry(frm, textvariable=self.var_user, width=32, fg="black", border=0, bg="white", font=(login_font, 18))
        user.place(x=170, y=170)
        user.insert(0, "Username")
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        Frame(frm, width=350, height=2, bg="black").place(x=169, y=203)


        def on_enter(e):
            psw.delete(0, "end")


        def on_leave(e):
            passw = psw.get()
            if passw == '':
                psw.insert(0, "Password")


        psw = Entry(frm, textvariable=self.var_psw, width=32, fg="black", border=0, bg="white", font=(login_font, 18))
        psw.place(x=170, y=270)
        psw.insert(0, "Password")
        psw.bind('<FocusIn>', on_enter)
        psw.bind('<FocusOut>', on_leave)

        Frame(frm, width=350, height=2, bg="black").place(x=169, y=303)

        btn_log = Button(
            frm, text="SIGN IN", width=18, bg=login_color, cursor='hand2', fg="white", font=(login_font, 16, "bold"),
            relief="flat", border=0, command=self.signin_db
        )
        btn_log.place(x=200, y=350)

        lbl_signup = Label(frm, text="Don't have an account?", bg="white", fg="black", font=(login_font, 12))
        lbl_signup.place(x=165, y=440)
        btn_signup = Button(
            frm, text="Sign up", border=0, cursor="hand2", font=(login_font, 12, "italic bold"), relief="flat",
            fg="#432771", bg="white", command=self.signup
        )
        btn_signup.place(x=390, y=439)

        btn_fgpass = Button(
            frm, text="Forgot password?", border=0, cursor="hand2", font=(login_font, 12, "italic bold"), relief="flat",
            fg="#432771", bg="white", command=self.forgot_psw
        )
        btn_fgpass.place(x=220, y=480)

    def forgot_psw(self):
        self.root.withdraw()
        self.psw_window = Toplevel(self.root)
        self.psw_win = ForgetPass(self.psw_window)

    def signup(self):
        self.root.withdraw()
        self.signup_window = Toplevel(self.root)
        self.signup_win = SignUp(self.signup_window, self)



    ###----------  login check db =-----------############

    def signin_db(self):
        username = self.var_user.get()
        passw = self.var_psw.get()

        if username == '' or passw == '':
            messagebox.showerror('Invalid', 'You must fill all fields', parent=self.root)
            return
        
        conn = mysql.connector.connect(
        host  = 'localhost',
        user = 'root',
        password = '',
        database = 'mydb',
        port = '3306'
         )
        c = conn.cursor()

        db_info = "select user, password from admins where user=%s and password=%s"
        vals = (username, passw)
        c.execute(db_info, vals)
        result = c.fetchone()
        conn.close()

        if result:
            #---------   main app display here  --------------#

            self.root.withdraw()
            self.main_window = Toplevel(self.root)
            self.main_win = AfterLogin(self.main_window)


        else:
            messagebox.showerror("Invalid", "Username or password not correct.", parent=self.root)


main_color = "#6f86b9"
main_font = "Courier new"




#=====----------------  forget password  ------------------=#


class ForgetPass:    
    def __init__(self, root):
        self.root = root
        self.root.title("Reset password")
        self.root.geometry("1250x850+70+0")
        self.root.resizable(False, False)
        self.root.config(bg=main_color)


        self.var_entry_name = StringVar()
        self.var_entry_newpass = StringVar()
        self.var_entry_confirmpass = StringVar()


        forgot_color = "red"
        forgot_font = "Courier new"

        frm = Frame(self.root, width=800, height=550, bg="white")
        frm.place(x=200, y=100)

        lbl_head = Label(frm, text="Password reset", bg="white", fg=forgot_color, font=(forgot_font, 28, "bold"))
        lbl_head.place(x=140, y=86)


        def on_enter(e):
            entry_name.delete(0, "end")

        def on_leave(e):
            user = entry_name.get()
            if user == '':
                entry_name.insert(0, 'Enter your Username')

        entry_name = Entry(frm, textvariable=self.var_entry_name, width=32, fg="black", border=0, bg="white", font=(forgot_font, 16))
        entry_name.place(x=140, y=195)
        entry_name.insert(0, "Enter your Username")
        entry_name.bind('<FocusIn>', on_enter)
        entry_name.bind('<FocusOut>', on_leave)

        Frame(frm, width=350, height=2, bg="black").place(x=140, y=222)

        def on_enter(e):
            entry_newpass.delete(0, "end")

        def on_leave(e):
            newpsw = entry_newpass.get()
            if newpsw == '':
                entry_newpass.insert(0, 'Enter new password')

        entry_newpass = Entry(frm, textvariable=self.var_entry_newpass, width=32, fg="black", border=0, bg="white", font=(forgot_font, 16))
        entry_newpass.place(x=140, y=255)
        entry_newpass.insert(0, "Enter new password")
        entry_newpass.bind('<FocusIn>', on_enter)
        entry_newpass.bind('<FocusOut>', on_leave)

        Frame(frm, width=350, height=2, bg="black").place(x=140, y=282)

        def on_enter(e):
            entry_confirmpass.delete(0, "end")

        def on_leave(e):
            c_newpsw = entry_confirmpass.get()
            if c_newpsw == '':
                entry_confirmpass.insert(0, 'Confirm new password')

        entry_confirmpass = Entry(frm, textvariable=self.var_entry_confirmpass, width=32, fg="black", border=0, bg="white", font=(forgot_font, 16))
        entry_confirmpass.place(x=140, y=315)
        entry_confirmpass.insert(0, "Confirm new password")
        entry_confirmpass.bind('<FocusIn>', on_enter)
        entry_confirmpass.bind('<FocusOut>', on_leave)

        Frame(frm, width=350, height=2, bg="black").place(x=140, y=342)

        btn_confirm = Button(
            frm, text="CONFIRM", width=16, bg=forgot_color, cursor='hand2', fg="white", font=(forgot_font, 16, "bold"),
            relief="flat", border=0, command=self.confirmuser
        )
        btn_confirm.place(x=180, y=385)



    def confirmuser(self):
        user = self.var_entry_name.get()
        newp = self.var_entry_newpass.get()
        c_newp = self.var_entry_confirmpass.get()

        if user == '' or newp == '' or c_newp == '':
            messagebox.showerror('Invalid', 'Please fill all fields.', parent=self.root)
            return
        if newp != c_newp:
            messagebox.showerror('Invalid', 'Both password must match.', parent=self.root)
            return
        if len(newp) < 8:
            messagebox.showerror('Invalid', 'Password must be atleast of 8 characters.', parent=self.root)
            return


        conn = mysql.connector.connect(
        host  = 'localhost',
        user = 'root',
        password = '',
        database = 'mydb',
        port = '3306'
         )
        c = conn.cursor()

        db_info = "select user from admins where user=%s"
        vals = (user,)
        c.execute(db_info, vals)
        yesuser = c.fetchone()

        if yesuser:
                insert_newpsw = "update admins set password=%s where user=%s"
                vals = (newp, user)

                try:
                    c.execute(insert_newpsw, vals)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Password reset successful.")

                    self.root.withdraw()
                    self.signin_window = Toplevel(self.root)
                    self.signin_win = Logging(self.signin_window) 

                    

                except mysql.connector.Error as error:
                    messagebox.showerror("Error", str(error), parent=self.root)

        else:
            messagebox.showerror('Invalid', 'User does not exist.', parent=self.root)


        self.var_entry_name.delete(0, END)
        self.var_entry_newpass.delete(0, END)
        self.var_entry_confirmpass.delete(0, END)












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
    app = FaceRecognitionApp(root)
    root.mainloop()






