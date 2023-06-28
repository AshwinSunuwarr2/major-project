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
#     btn_signup = tk.Button(frm, text="Sign up", border=0, cursor="hand2", font=(my_font, 12, "italic"), relief="flat", fg="#dd4b3f", bg="white")
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
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import Image, ImageTk

import mysql.connector



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
        # self.root.withdraw()
        # self.signin_window = Toplevel(self.root)
        # self.login_win = Logging(self.signin_window)   
        self.root.withdraw()
        self.back_window = Toplevel(self.root)
        self.back_win = Logging(self.back_window, self)


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
    def __init__(self, root, back_win):
        self.root = root
        self.root.geometry("1250x850+70+0")
        self.back_win = back_win
        title_color = "#6f86b9"
        self.root.config(bg=title_color)
        self.root.title("Criminal Face Recognition System")
        self.root.resizable(False, False)

        login_color = "#e13746"
        login_font = "Courier new"
        self.var_user = StringVar()
        self.var_psw = StringVar()


        frm = Frame(self.root, width=800, height=550, bg=title_color)
        frm.place(x=200, y=100)

        lbl_head = Label(frm, text="Sign in", bg=title_color, fg=login_color, font=(login_font, 28, "bold"))
        lbl_head.place(x=170, y=80)

        btn_back = Button(
            self.root, text="Back", width=8, bg="black", cursor='hand2', fg="white", font=(login_font, 12),
            relief="ridge", border=1, command=self.back
        )
        btn_back.place(x=150, y=150)  


        def on_enter(e):
            user.delete(0, "end")


        def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0, "Username")


        user = Entry(frm, textvariable=self.var_user, width=32, fg="black", border=0, bg=title_color, font=(login_font, 18))
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


        psw = Entry(frm, textvariable=self.var_psw, width=32, fg="black", border=0, bg=title_color, font=(login_font, 18))
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

        lbl_signup = Label(frm, text="Don't have an account?", bg=title_color, fg="black", font=(login_font, 12))
        lbl_signup.place(x=165, y=440)
        btn_signup = Button(
            frm, text="Sign up", border=0, cursor="hand2", font=(login_font, 12, "italic bold"), relief="flat",
            fg="#432771", bg=title_color, command=self.signup
        )
        btn_signup.place(x=390, y=439)

        btn_fgpass = Button(
            frm, text="Forgot password?", border=0, cursor="hand2", font=(login_font, 12, "italic bold"), relief="flat",
            fg="#432771", bg=title_color, command=self.forgot_psw
        )
        btn_fgpass.place(x=220, y=480)

    def forgot_psw(self):
        self.root.withdraw()
        self.psw_window = Toplevel(self.root)
        self.psw_win = ForgetPass(self.psw_window, self)

    def signup(self):
        self.root.withdraw()
        self.signup_window = Toplevel(self.root)
        self.signup_win = SignUp(self.signup_window, self)


    def back(self):
        self.root.withdraw()
        self.back_win.root.deiconify()
        # def back(self):
        #     self.root.withdraw()
        #     self.back_window = Toplevel(self.root)
        #     self.back_win = FaceRecognitionApp(self.back_window, self)



    ###----------  login check db =-----------############

    def signin_db(self):
        username = self.var_user.get()
        passw = self.var_psw.get()

        if username == '' or passw == '' or username == "Username" or passw == "Password":
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
            return


main_color = "#6f86b9"
main_font = "Courier new"




#=====----------------  forget password  ------------------=#


class ForgetPass:    
    def __init__(self, root, back_win):
        self.root = root
        self.root.title("Reset password")
        self.root.geometry("1250x850+70+0")
        self.back_win = back_win
        self.root.resizable(False, False)
        self.root.config(bg=main_color)


        self.var_entry_name = StringVar()
        self.var_entry_newpass = StringVar()
        self.var_entry_confirmpass = StringVar()


        forgot_color = "#e13746"
        forgot_font = "Courier new"

        frm = Frame(self.root, width=800, height=550, bg=main_color)
        frm.place(x=200, y=100)

        lbl_head = Label(frm, text="Password reset", bg=main_color, fg=forgot_color, font=(forgot_font, 28, "bold"))
        lbl_head.place(x=140, y=86)
        
        btn_back = Button(
            self.root, text="Back", width=8, bg="black", cursor='hand2', fg="white", font=(forgot_font, 12),
            relief="ridge", border=1, command=self.back
        )
        btn_back.place(x=150, y=150) 


        def on_enter(e):
            entry_name.delete(0, "end")

        def on_leave(e):
            user = entry_name.get()
            if user == '':
                entry_name.insert(0, 'Enter your Username')

        entry_name = Entry(frm, textvariable=self.var_entry_name, width=32, fg="black", border=0, bg=main_color, font=(forgot_font, 16))
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

        entry_newpass = Entry(frm, textvariable=self.var_entry_newpass, width=32, fg="black", border=0, bg=main_color, font=(forgot_font, 16))
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

        entry_confirmpass = Entry(frm, textvariable=self.var_entry_confirmpass, width=32, fg="black", border=0, bg=main_color, font=(forgot_font, 16))
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

    def back(self):
            self.root.withdraw()
            self.back_win.root.deiconify()







main_color = "#6f86b9"
main_font = "Courier new"


class AfterLogin:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1250x850+70+0")
        root.state('zoomed')

        title_color = "#b2bedc"
        self.root.config(bg=title_color)
        self.root.title("Criminal Face Recognition System")
        # self.root.resizable(False, False)


        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        # Create File menu
        home_menu = Menu(menu_bar, tearoff=0)
        home_menu.add_command(label="Register Criminal", command=self.criminal_reg)
        home_menu.add_separator()
        home_menu.add_command(label="Update Criminal Details", command=self.update_criminal)
        home_menu.add_separator()
        home_menu.add_command(label="Delete Criminal Details", command=self.criminal_details)
        home_menu.add_separator()
        home_menu.add_command(label="Exit", command=self.root.quit)
        home_menu.add_separator()
        menu_bar.add_cascade(label="Home", menu=home_menu)


        data_menu = Menu(menu_bar, tearoff=0)
        data_menu.add_command(label="View Criminal Details")
        data_menu.add_separator()
        data_menu.add_command(label="View Dataset")
        data_menu.add_separator()
        menu_bar.add_cascade(label="Datasets", menu=data_menu)

        cam_menu = Menu(menu_bar, tearoff=0)
        cam_menu.add_command(label="Recognize Criminals")
        cam_menu.add_separator()
        menu_bar.add_cascade(label="Camera", menu=cam_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Get help", command=self.help)
        help_menu.add_separator()
        help_menu.add_command(label="About us", command=self.aboutus)
        help_menu.add_separator()
        menu_bar.add_cascade(label="More", menu=help_menu)





#-------------   functions  --------------------=============================================================================================#


    def help(self):
        frm1 =Frame(self.root, width = 1250, height = 850, bg=main_color)
        frm1.place(x=135, y=0)
        lbl_text = Label(frm1, bg=main_color, text="Ashwin181209@ncit.edu.np\n Irajk181216@ncit.edu.np\n Ishan181217@ncit.edu.np",
                                font=(main_font, 18, 'bold'))
        lbl_text.place(x=50, y=60, anchor='w')

    def aboutus(self):
        frm1 =Frame(self.root, width = 1250, height = 850, bg=main_color)
        frm1.place(x=135, y=0)
        lbl_text = Label(frm1, bg=main_color, text="Canvas and frm_add are two different widgets in the Tkinter GUI toolkit in Python,\n and they have different purposes.",
                                font=(main_font, 18, 'bold'))
        lbl_text.place(x=30, y=60)
        

    def criminal_reg(self):
        add_color = "#b2bedc"
        add_font = "Courier new"
        self.front_file = StringVar()
        self.left_file = StringVar()
        self.right_file = StringVar()

        self.var_name_entry = StringVar()
        self.var_father_entry = StringVar()
        self.var_mother_entry = StringVar()
        self.var_age_entry = StringVar()
        self.var_gender_entry = StringVar()
        self.var_nationality_entry = StringVar()


         #------------------  registeration fxns ------------#

        def add_image(label, image_variable):
                f_types = [('PNG files', '*.png'), ('JPEG files', '*.jpg;*.jpeg')]
                file_path = filedialog.askopenfilename(filetypes=f_types)
                
                if file_path:
                    img = Image.open(file_path)
                    img.thumbnail((200, 200))  # Resize the image for preview
                    photo = ImageTk.PhotoImage(img)
                    label.configure(image=photo)
                    label.image = photo  # Store a reference to the image

                    image_variable.set(file_path)

        def submit():
            name = name_entry.get().strip()
            father_name = father_entry.get().strip()
            mother_name = mother_entry.get().strip()
            age = age_entry.get().strip()
            nationality = nationality_entry.get().strip()
            gender = gender_entry.get().strip()
            crime = crime_entry.get("1.0", END).strip()
            
            if name == '' or age == '' or gender == '' or nationality == '' or crime == '':
                messagebox.showerror("Error", "Please fill all required * fields.")
                return 

            try:
                age = int(age) 
            except ValueError:
                messagebox.showerror("Error", "Age must be valid.")
                return
            if age <= 16:
                messagebox.showerror("Error", "Age must be above 16.")
                return

            image_paths = [self.front_file.get(), self.left_file.get(), self.right_file.get()]
            image_data = []

            for path in image_paths:
                if path:
                    with open(path, 'rb') as file:
                        image_data.append(file.read())
                else:
                    messagebox.showerror("Error", "Please select all three images.")
                    return
                

            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                port='3306',
                database='mydb'
            )
            c = connection.cursor()

            data_insert = "INSERT INTO `criminal_reg`(`name`, `father_name`, `mother_name`, `age`, `gender`, `nationality`, `crime`, `front_img`, `left_img`, `right_img`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            vals = (name, father_name, mother_name, age, gender, nationality, crime, image_data[0], image_data[1], image_data[2])
                
            try:
                c.execute(data_insert, vals)
                connection.commit()
                fetch_id = "select id from criminal_reg where name=%s and crime=%s"
                values  = (name, crime)
                c.execute(fetch_id, values)
                crim_id = c.fetchone()
                connection.close()

                messagebox.showinfo("Success", f"Criminal with ID: {crim_id[0]} is now registered.")

            except mysql.connector.Error as error:
                messagebox.showerror("Database Error", str(error))

            name_entry.delete(0, END)
            father_entry.delete(0, END)
            mother_entry.delete(0, END)
            age_entry.delete(0, END)
            gender_entry.delete(0, END)
            nationality_entry.delete(0, END)
            crime_entry.delete("1.0", END)
            front_image_label.configure(image=None)  
            left_image_label.configure(image=None)      
            right_image_label.configure(image=None)
            front_image_label.image = None  # Clear reference to front image
            left_image_label.image = None  # Clear ref
            right_image_label.image = None  # Clear ref
            self.front_file.set("")
            self.left_file.set("")
            self.right_file.set("")






        frm_add = Frame(self.root, bg=add_color, width=1250, height=850)
        frm_add.place(x=135, y=0)

        lbl_head = Label(frm_add, text='Register Criminals', bg=add_color, font=(add_font, 28, 'bold'))
        lbl_head.place(x=380, y=30)

        #name label
        asterisk_label = Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=200, y=100, anchor='nw')

        text_label = Label(frm_add, text="Name:", font=('Courier New', 18, 'bold'), bg=add_color, fg="#383838")
        text_label.place(x=300, y=100, anchor='ne')

        name_entry = Entry(frm_add, textvariable=self.var_name_entry, width=40, font=('Courier New', 16))
        name_entry.place(x=380, y=100)

        #father name
        father_label = Label(frm_add, fg='#383838', text="Father's Name:", font=('Courier New', 18, 'bold'), bg=add_color)
        father_label.place(x=300, y=160, anchor='ne')
        father_entry = Entry(frm_add, textvariable=self.var_father_entry, width=40, font=('Courier New', 16))
        father_entry.place(x=380, y=160)

        #mother name
        mother_label = Label(frm_add, fg='#383838', text="Mother's Name:", font=('Courier New', 18, 'bold'), bg=add_color)
        mother_label.place(x=300, y=220, anchor='ne')
        mother_entry = Entry(frm_add, textvariable=self.var_mother_entry, width=40, font=('Courier New', 16))
        mother_entry.place(x=380, y=220)

        #age
        asterisk_label = Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=210, y=280, anchor='nw')

        text_label = Label(frm_add, text="Age:", font=('Courier New', 18, 'bold'), bg=add_color, fg="#383838")
        text_label.place(x=300, y=280, anchor='ne')

        age_entry = Entry(frm_add, textvariable=self.var_age_entry, width=40, font=('Courier New', 16))
        age_entry.place(x=380, y=280)

        #gender
        asterisk_label = Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=168, y=340, anchor='nw')

        text_label = Label(frm_add, text="Gender:", font=('Courier New', 18, 'bold'), bg=add_color, fg="#383838")
        text_label.place(x=300, y=340, anchor='ne')

        gender_entry = Entry(frm_add, textvariable=self.var_gender_entry, width=40, font=('Courier New', 16))
        gender_entry.place(x=380, y=340)

        #nationality
        asterisk_label = Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=94, y=400, anchor='nw')

        text_label = Label(frm_add, text="Nationality:", font=('Courier New', 18, 'bold'), bg=add_color, fg="#383838")
        text_label.place(x=300, y=400, anchor='ne')

        nationality_entry = Entry(frm_add,textvariable=self.var_nationality_entry, width=40, font=('Courier New', 16))
        nationality_entry.place(x=380, y=400)

        #crime
        asterisk_label = Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=42, y=460, anchor='nw')

        text_label = Label(frm_add, text="Crime Committed:", font=('Courier New', 18, 'bold'), bg=add_color, fg="#383838")
        text_label.place(x=300, y=460, anchor='ne')

        crime_entry = Text(frm_add, width=40, height=1, font=('Courier New', 16))
        crime_entry.place(x=380, y=460)


        #image display garna labels haru
        front_image_label = Label(frm_add, bg=add_color)
        front_image_label.place(x=240, y=505)

        left_image_label = Label(frm_add, bg=add_color)
        left_image_label.place(x=600, y=505)

        right_image_label = Label(frm_add, bg=add_color)
        right_image_label.place(x=950, y=505)

        # image selection 
        browse_btn1 = Button(frm_add, cursor="hand2", text="Select Front Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(front_image_label, self.front_file))
        browse_btn1.place(x=140, y=610)

        browse_btn2 = Button(frm_add, cursor="hand2", text="Select Left Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(left_image_label, self.left_file))
        browse_btn2.place(x=495, y=610)

        browse_btn3 = Button(frm_add, cursor="hand2", text="Select Right Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(right_image_label, self.right_file))
        browse_btn3.place(x=830, y=610)
            
        # Apply hover effect
        def on_enter(e):
            e.widget.config(bg="#ffc168")
            
        def on_leave(e):
            e.widget.config(bg="#ffb067")

        browse_btn1.configure(bg='#ffb067', fg='#383838')
        browse_btn1.bind("<Enter>", on_enter)
        browse_btn1.bind("<Leave>", on_leave)

        browse_btn2.configure(bg='#ffb067', fg='#383838')
        browse_btn2.bind("<Enter>", on_enter)
        browse_btn2.bind("<Leave>", on_leave)

        browse_btn3.configure(bg='#ffb067', fg='#383838')
        browse_btn3.bind("<Enter>", on_enter)
        browse_btn3.bind("<Leave>", on_leave)


        # Confirm Button
        confirm_btn = Button(frm_add, text="Confirm", font=('Courier New', 16, 'bold'), fg ="#383838", bg="#ffb067", command= submit)
        confirm_btn.place(x=570, y=685)

        # Configure button styling options
        confirm_btn.config(relief=RAISED, bd=3, width=14)

        confirm_btn.bind("<Enter>", on_enter)
        confirm_btn.bind("<Leave>", on_leave)

       
    def update_criminal(self):
        add_color = "#b2bedc"
        frm_add = Frame(self.root, width=1250, height=850, bg=add_color)
        frm_add.place(x=135, y=0)

        def add_image(label, image_variable):
            f_types = [('PNG files', '*.png'), ('JPEG files', '*.jpg;*.jpeg')]
            file_path = filedialog.askopenfilename(filetypes=f_types)
            
            if file_path:
                img = Image.open(file_path)
                img.thumbnail((200, 200))  # Resize the image for preview
                photo = ImageTk.PhotoImage(img)
                label.configure(image=photo)
                label.image = photo  # Store a reference to the image

                image_variable.set(file_path)

        front_file = StringVar()
        left_file = StringVar()
        right_file = StringVar()

        def submit_form():
            c_id = id_entry.get().strip()
            updated_name = name_entry.get().strip()
            updated_father_name = father_entry.get().strip()
            updated_mother_name = mother_entry.get().strip()
            updated_age = age_entry.get().strip()
            updated_nationality = nationality_entry.get().strip()
            updated_gender = gender_entry.get().strip()
            updated_crime = crime_entry.get("1.0", END).strip()

            if c_id == '':
                messagebox.showerror('Invalid', 'You must fill the ID of a criminal.')
                return
            
            try:
                c_id = int(c_id)
            except ValueError:
                messagebox.showerror('Invalid', 'ID is not valid.')
                return
            
            if updated_age != '':
                try:
                    updated_age = int(updated_age) 
                except ValueError:
                    messagebox.showerror("Error", "Age must be a valid number.")
                    return
                if updated_age < 14:
                    messagebox.showerror('Invalid', 'Age must be valid.')
                    return

            conn = mysql.connector.connect(
                host='localhost',
                database='mydb',
                port='3306',
                user='root',
                password=''
            )
            c = conn.cursor()

            fetch_id = "SELECT * FROM criminal_reg WHERE id=%s"
            values = (c_id,)
            c.execute(fetch_id, values)
            crim_data = c.fetchone()

            image_paths = [front_file.get(), left_file.get(), right_file.get()]
            updated_image_data = []

            for path in image_paths:
                if path:
                    with open(path, 'rb') as file:
                        updated_image_data.append(file.read())

            if crim_data:
                if updated_name == '' and updated_father_name == '' and updated_mother_name == '' and updated_age == '' and updated_nationality == '' and updated_gender == '' and updated_crime == '':
                    messagebox.showinfo('Invalid', "No changes made.")
                    return
                
                data_update = "UPDATE criminal_reg SET "
                update_vals = {}

                if updated_name:
                    update_vals['name'] = updated_name
                else:
                    update_vals['name'] = crim_data[1]

                if updated_father_name:
                    update_vals['father_name'] = updated_father_name
                else:
                    update_vals['father_name'] = crim_data[2]

                if updated_mother_name:
                    update_vals['mother_name'] = updated_mother_name
                else:
                    update_vals['mother_name'] = crim_data[3]

                if updated_age:
                    update_vals['age'] = updated_age
                else:
                    update_vals['age'] = crim_data[4]

                if updated_gender:
                    update_vals['gender'] = updated_gender
                else:
                    update_vals['gender'] = crim_data[5]

                if updated_nationality:
                    update_vals['nationality'] = updated_nationality
                else:
                    update_vals['nationality'] = crim_data[6]

                if updated_crime:
                    update_vals['crime'] = updated_crime
                else:
                    update_vals['crime'] = crim_data[7]

                if updated_image_data and updated_image_data[0]:
                    update_vals['front_img'] = updated_image_data[0]
                else:
                    update_vals['front_img'] = crim_data[8]

                if updated_image_data and updated_image_data[1]:
                    update_vals['left_img'] = updated_image_data[1]
                else:
                    update_vals['left_img'] = crim_data[9]

                if updated_image_data and updated_image_data[2]:
                    update_vals['right_img'] = updated_image_data[2]
                else:
                    update_vals['right_img'] = crim_data[10]

                data_update += ', '.join(f"{field} = %s" for field in update_vals.keys())
                data_update += " WHERE id = %s"

                try:
                    c.execute(data_update, tuple(update_vals.values()) + (c_id,))
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Success", f"Criminal with ID: {crim_data[0]} has been updated.")

                except mysql.connector.Error as error:
                    messagebox.showerror("Database Error", str(error))
                    return

                name_entry.delete(0, END)
                father_entry.delete(0, END)
                mother_entry.delete(0, END)
                age_entry.delete(0, END)
                gender_entry.delete(0, END)
                nationality_entry.delete(0, END)
                crime_entry.delete("1.0", END)
                front_image_label.configure(image=None)
                left_image_label.configure(image=None)
                right_image_label.configure(image=None)
                front_image_label.image = None  # Clear reference to front image
                left_image_label.image = None  # Clear reference to left image
                right_image_label.image = None  # Clear reference to right image
                front_file.set("")
                left_file.set("")
                right_file.set("")
                id_entry.delete(0, END)
            else:
                name_entry.delete(0, END)
                father_entry.delete(0, END)
                mother_entry.delete(0, END)
                age_entry.delete(0, END)
                gender_entry.delete(0, END)
                nationality_entry.delete(0, END)
                crime_entry.delete("1.0", END)
                front_image_label.configure(image=None)
                left_image_label.configure(image=None)
                right_image_label.configure(image=None)
                front_image_label.image = None  # Clear reference to front image
                left_image_label.image = None  # Clear reference to left image
                right_image_label.image = None  # Clear reference to right image
                front_file.set("")
                left_file.set("")
                right_file.set("")
                id_entry.delete(0, END)
                
                messagebox.showerror('Invalid', 'Invalid ID.')            
                return


        ############  labels  #########33##########
        lbl_head = Label(frm_add, text='ID of criminal you want to update: ', fg='red', bg=add_color, font=(main_font, 18))
        lbl_head.place(x=360, y=30, anchor='n')
        id_entry = Entry(frm_add, width=7, font=('Courier New', 24), bd=5)
        id_entry.place(x=600, y=30)

        #name label
        text_label = Label(frm_add, text="Name:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
        text_label.place(x=300, y=100, anchor='ne')
        name_entry = Entry(frm_add, width=40, font=('Courier New', 16))
        name_entry.place(x=380, y=100)

        #father name
        father_label = Label(frm_add, fg='#383838', text="Father's Name:", font=('Courier New', 18, 'bold'), bg="#b2bedc")
        father_label.place(x=300, y=160, anchor='ne')
        father_entry = Entry(frm_add, width=40, font=('Courier New', 16))
        father_entry.place(x=380, y=160)

        #mother name
        mother_label = Label(frm_add, fg='#383838', text="Mother's Name:", font=('Courier New', 18, 'bold'), bg="#b2bedc")
        mother_label.place(x=300, y=220, anchor='ne')
        mother_entry = Entry(frm_add, width=40, font=('Courier New', 16))
        mother_entry.place(x=380, y=220)

        #age
        text_label = Label(frm_add, text="Age:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
        text_label.place(x=300, y=280, anchor='ne')
        age_entry = Entry(frm_add, width=40, font=('Courier New', 16))
        age_entry.place(x=380, y=280)

        #gender
        text_label = Label(frm_add, text="Gender:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
        text_label.place(x=300, y=340, anchor='ne')
        gender_entry = Entry(frm_add, width=40, font=('Courier New', 16))
        gender_entry.place(x=380, y=340)

        #nationality
        text_label = Label(frm_add, text="Nationality:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
        text_label.place(x=300, y=400, anchor='ne')
        nationality_entry = Entry(frm_add, width=40, font=('Courier New', 16))
        nationality_entry.place(x=380, y=400)

        #crime
        text_label = Label(frm_add, text="Crime Committed:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
        text_label.place(x=300, y=460, anchor='ne')
        crime_entry = Text(frm_add, width=40, height=1, font=('Courier New', 16))
        crime_entry.place(x=380, y=460)


        #image display garna labels haru
        front_image_label = Label(frm_add, bg=add_color)
        front_image_label.place(x=240, y=505)

        left_image_label = Label(frm_add, bg=add_color)
        left_image_label.place(x=600, y=505)

        right_image_label = Label(frm_add, bg=add_color)
        right_image_label.place(x=950, y=505)

        # image selection 
        browse_btn1 = Button(frm_add, cursor="hand2", text="Select Front Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(front_image_label, front_file))
        browse_btn1.place(x=140, y=610)

        browse_btn2 = Button(frm_add, cursor="hand2", text="Select Left Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(left_image_label, left_file))
        browse_btn2.place(x=495, y=610)

        browse_btn3 = Button(frm_add, cursor="hand2", text="Select Right Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(right_image_label, right_file))
        browse_btn3.place(x=830, y=610)
            
        # Apply hover effect
        def on_enter(e):
            e.widget.config(bg="#ffc168")
            
        def on_leave(e):
            e.widget.config(bg="#ffb067")

        browse_btn1.configure(bg='#ffb067', fg='#383838')
        browse_btn1.bind("<Enter>", on_enter)
        browse_btn1.bind("<Leave>", on_leave)

        browse_btn2.configure(bg='#ffb067', fg='#383838')
        browse_btn2.bind("<Enter>", on_enter)
        browse_btn2.bind("<Leave>", on_leave)

        browse_btn3.configure(bg='#ffb067', fg='#383838')
        browse_btn3.bind("<Enter>", on_enter)
        browse_btn3.bind("<Leave>", on_leave)


        # Confirm Button
        confirm_btn = Button(frm_add, text="Confirm", font=('Courier New', 16, 'bold'), fg ="#383838", bg="#ffb067", command=submit_form)
        confirm_btn.place(x=570, y=685)

        # Configure button styling options
        confirm_btn.config(relief=RAISED, bd=3, width=14)

        confirm_btn.bind("<Enter>", on_enter)
        confirm_btn.bind("<Leave>", on_leave)    


    def criminal_details(self):
        del_color = "#b2bedc"
        del_font = 'courier new'


        def delete_confirm():
            c_id = entry_id.get().strip()

            if c_id == "":
                messagebox.showerror('Invalid', 'Please enter ID of criminal to delete.')
                return
            try:
                c_id = int(c_id)
            except ValueError:
                messagebox.showerror('Invalid', "Invalid ID.")
                return
            
            conn = mysql.connector.connect(
                host = 'localhost',
                database = 'mydb',
                port = '3306',
                user = 'root',
                password  = ''
            )
            c = conn.cursor()

            fetch_id = "select * from criminal_reg where id = %s"
            values = (c_id,)
            c.execute(fetch_id, values)
            crim_data = c.fetchone()

            if crim_data:
                crim_delete = "delete from criminal_reg where id=%s"
                vals = (c_id,)

                try:
                    c.execute(crim_delete, vals)
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Success", f"Criminal with ID: {crim_data[0]} has been deleted.")

                except mysql.connector.Error as error:
                    messagebox.showerror("Database Error", str(error))
                    return
            else:
                messagebox.showerror('Invalid', 'ID not found.')
                return
            
            entry_id.delete(0, END)

        def view_details():
            c_id = entry_id.get().strip()

            if c_id == "":
                messagebox.showerror('Invalid', 'Please enter ID of criminal to view.')
                return
            try:
                c_id = int(c_id)
            except ValueError:
                messagebox.showerror('Invalid', "Invalid ID.")
                return

            conn = mysql.connector.connect(
                host='localhost',
                database='mydb',
                port='3306',
                user='root',
                password=''
            )
            c = conn.cursor()

            fetch_id = "select * from criminal_reg where id = %s"
            values = (c_id,)
            c.execute(fetch_id, values)
            crim_data = c.fetchall()

            if len(crim_data) != 0:
                self.criminal_tbl.delete(*self.criminal_tbl.get_children())  # Clear existing data in the treeview
                for row in crim_data:
                    self.criminal_tbl.insert("", 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                conn.commit()
            else:
                messagebox.showerror('Invalid', 'ID not found.')
                return

            conn.close()

            entry_id.delete(0, END)



        

        frm_detail = Frame(self.root, width=1250, height=850, bg=del_color)
        frm_detail.place(x=135, y=0)

        lbl_head = Label(frm_detail, text="Delete Criminal", font=(del_font, 28, 'bold'), bg=del_color)
        lbl_head.place(x=400, y=90)

        lbl_text = Label(frm_detail, text="Enter the criminal ID: ", fg="red", bg=del_color, font=(del_font, 20))
        lbl_text.place(x=250, y=185)

        entry_id = Entry(frm_detail, bg="white", width=7,  font=(del_font, 28), bd=5)  
        entry_id.place(x=620, y=175)

        btn_del = Button(frm_detail, width=12, text="DELETE", bg='orange', font=(del_font, 18), cursor="hand2", relief='raised', command=delete_confirm)
        btn_del.place(x=390, y=250)

        btn_view = Button(frm_detail, width=12, text="VIEW", bg='orange', font=(del_font, 18), cursor="hand2", relief='raised', command=view_details)
        btn_view.place(x=590, y=250)
    
        frm_view = LabelFrame(frm_detail, text= "Criminal details", width=800, height=380, bg="white")
        frm_view.place(x=240, y=320)
        table_frm = Frame(frm_view, bg="white")
        table_frm.place(x=0, y=0, width=780, height=360)

        scroll_x = ttk.Scrollbar(table_frm, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frm, orient=VERTICAL)
        
        self.criminal_tbl = ttk.Treeview(table_frm, column=("id", "name", "father_name", "mother_name", "age", "gender", "nationality", "crime"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.criminal_tbl.xview)
        scroll_y.config(command=self.criminal_tbl.yview)


        self.criminal_tbl.heading("id", text="ID")
        self.criminal_tbl.heading("name", text="Name")
        self.criminal_tbl.heading("father_name", text="Father's Name")
        self.criminal_tbl.heading("mother_name", text="Mother's Name")
        self.criminal_tbl.heading("age", text="Age")
        self.criminal_tbl.heading("gender", text="Gender")
        self.criminal_tbl.heading("nationality", text="Nation")
        self.criminal_tbl.heading("crime", text="Crime Committed")
        self.criminal_tbl["show"] = "headings"

        
        self.criminal_tbl.column("id", width=60)
        self.criminal_tbl.column("name", width=180)
        self.criminal_tbl.column("father_name", width=180)
        self.criminal_tbl.column("mother_name", width=180)
        self.criminal_tbl.column("age", width=60)
        self.criminal_tbl.column("gender", width=100)
        self.criminal_tbl.column("nationality", width=140)
        self.criminal_tbl.column("crime", width=300)

        self.criminal_tbl.pack(fill=BOTH, expand=1)





if __name__ == "__main__":
    root = Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()





