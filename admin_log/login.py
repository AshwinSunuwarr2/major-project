from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

import mysql.connector
from forgotp import ForgetPass
from after_login import AfterLogin


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

        forget_psw_created = False


        self.var_user = StringVar()
        self.var_psw = StringVar()


        # outmenu_bar = Menu(self.root)
        # self.root.config(menu=outmenu_bar)

        # home_menu = Menu(outmenu_bar, tearoff=0)
        # home_menu.add_command(label='Home page')
        # home_menu.add_separator()
        # home_menu.add_command(label="Exit", command=self.root.quit)
        # outmenu_bar.add_cascade(label="HOME", menu=home_menu)

        # user_menu = Menu(outmenu_bar, tearoff=0)
        # user_menu.add_command(label="Sign in")
        # user_menu.add_separator()
        # user_menu.add_command(label="Sign up")
        # outmenu_bar.add_cascade(label="USER", menu=user_menu)


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
            fg="#432771", bg="white"
        )
        btn_signup.place(x=390, y=439)

        btn_fgpass = Button(
            frm, text="Forgot password?", border=0, cursor="hand2", font=(login_font, 12, "italic bold"), relief="flat",
            fg="#432771", bg="white", command=self.forget_pass
        )
        btn_fgpass.place(x=220, y=480)

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


    def forget_pass(self):
        self.forgot_window = Toplevel(self.root)
        self.forgot_win = ForgetPass(self.forgot_window)


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
    login = Logging(root)
    root.mainloop()



# import tkinter as tk
# from tkinter import messagebox, ttk
# import mysql.connector

# login_color = "#e13746"
# login_font = "Courier new"

# log_w = tk.Tk()
# log_w.title("Login")
# log_w.geometry("720x560")
# log_w.resizable(False, False)

# # Database connection setup
# conn = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     port='3306',
#     database='mydb'
# )
# c = conn.cursor()


# def signin():
#     username = user.get()
#     passw = psw.get()

#     if username == '' or passw == '':
#         messagebox.showerror('Invalid', 'You must fill all fields')
#         return

#     db_info = "select user, password from admins where user=%s and password=%s"
#     vals = (username, passw)
#     c.execute(db_info, vals)
#     result = c.fetchone()

#     if result:
#         log_w.destroy()
#         import new as new
#     else:
#         messagebox.showerror("Invalid", "Username or password not correct.")
#         return


# def fgpass():
#     log_w.withdraw()

    # def confirmuser():
    #     user = entry_name.get()
    #     newp = entry_newpass.get()
    #     c_newp = entry_confirmpass.get()

    #     db_info = "select user from admins where user=%s"
    #     vals = (user,)
    #     c.execute(db_info, vals)
    #     yesuser = c.fetchone()

    #     if yesuser:
    #         if user == '' or newp == '' or c_newp == '':
    #             messagebox.showerror('Invalid', 'You must fill all fields')
    #             return
    #         elif newp != c_newp:
    #             messagebox.showerror('Invalid', 'Both passwords must match.')
    #             return
    #         elif len(newp) < 8:
    #             messagebox.showerror('Invalid', 'Password must be at least 8 characters long.')
    #             return
    #         else:
    #             insert_newpsw = "update admins set password=%s where user=%s"
    #             vals = (newp, user)

    #             try:
    #                 c.execute(insert_newpsw, vals)
    #                 conn.commit()
    #                 messagebox.showinfo("Success", "Password reset successful.")

    #             except mysql.connector.Error as error:
    #                 messagebox.showerror("Database Error", str(error))
    #                 return
    #     else:
    #         messagebox.showerror('Invalid', 'User does not exist.')
    #         return

    #     entry_name.delete(0, tk.END)
    #     entry_newpass.delete(0, tk.END)
    #     entry_confirmpass.delete(0, tk.END)
        

#     fgpass_w = tk.Toplevel(log_w)
#     fgpass_w.title("Reset password")
#     fgpass_w.geometry("720x560")
#     fgpass_w.resizable(False, False)
#     fgpass_w.config(bg="white")

#     lbl_head = tk.Label(fgpass_w, text="Password reset", bg="white", fg=login_color, font=(login_font, 28, "bold"))
#     lbl_head.place(x=140, y=86)

    # def on_enter(e):
    #     entry_name.delete(0, "end")

    # def on_leave(e):
    #     user = entry_name.get()
    #     if user == '':
    #         entry_name.insert(0, 'Enter your Username')

    # entry_name = tk.Entry(fgpass_w, width=32, fg="black", border=0, bg="white", font=(login_font, 16))
    # entry_name.place(x=140, y=195)
    # entry_name.insert(0, "Enter your Username")
    # entry_name.bind('<FocusIn>', on_enter)
    # entry_name.bind('<FocusOut>', on_leave)

    # tk.Frame(fgpass_w, width=350, height=2, bg="black").place(x=140, y=222)

    # def on_enter(e):
    #     entry_newpass.delete(0, "end")

    # def on_leave(e):
    #     newpsw = entry_newpass.get()
    #     if newpsw == '':
    #         entry_newpass.insert(0, 'Enter new password')

    # entry_newpass = tk.Entry(fgpass_w, width=32, fg="black", border=0, bg="white", font=(login_font, 16))
    # entry_newpass.place(x=140, y=255)
    # entry_newpass.insert(0, "Enter new password")
    # entry_newpass.bind('<FocusIn>', on_enter)
    # entry_newpass.bind('<FocusOut>', on_leave)

    # tk.Frame(fgpass_w, width=350, height=2, bg="black").place(x=140, y=282)

    # def on_enter(e):
    #     entry_confirmpass.delete(0, "end")

    # def on_leave(e):
    #     c_newpsw = entry_confirmpass.get()
    #     if c_newpsw == '':
    #         entry_confirmpass.insert(0, 'Confirm new password')

    # entry_confirmpass = tk.Entry(fgpass_w, width=32, fg="black", border=0, bg="white", font=(login_font, 16))
    # entry_confirmpass.place(x=140, y=315)
    # entry_confirmpass.insert(0, "Confirm new password")
    # entry_confirmpass.bind('<FocusIn>', on_enter)
    # entry_confirmpass.bind('<FocusOut>', on_leave)

    # tk.Frame(fgpass_w, width=350, height=2, bg="black").place(x=140, y=342)

    # btn_confirm = tk.Button(
    #     fgpass_w, text="CONFIRM", width=16, bg=login_color, cursor='hand2', fg="white", font=(login_font, 16, "bold"),
    #     relief="flat", border=0, command=confirmuser
    # )
    # btn_confirm.place(x=180, y=385)

#     fgpass_w.deiconify()


# def nav_signup():
#     log_w.withdraw()
#     import signup as signup


# frm = tk.Frame(log_w, width=850, height=660, bg="white")
# frm.place(x=0, y=0)

# lbl_head = tk.Label(frm, text="Sign in", bg="white", fg=login_color, font=(login_font, 28, "bold"))
# lbl_head.place(x=170, y=80)


# def on_enter(e):
#     user.delete(0, "end")


# def on_leave(e):
#     name = user.get()
#     if name == '':
#         user.insert(0, "Username")


# user = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(login_font, 18))
# user.place(x=170, y=170)
# user.insert(0, "Username")
# user.bind('<FocusIn>', on_enter)
# user.bind('<FocusOut>', on_leave)

# tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=203)


# def on_enter(e):
#     psw.delete(0, "end")


# def on_leave(e):
#     passw = psw.get()
#     if passw == '':
#         psw.insert(0, "Password")


# psw = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(login_font, 18))
# psw.place(x=170, y=270)
# psw.insert(0, "Password")
# psw.bind('<FocusIn>', on_enter)
# psw.bind('<FocusOut>', on_leave)

# tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=303)

# btn_log = tk.Button(
#     frm, text="SIGN IN", width=18, bg=login_color, cursor='hand2', fg="white", font=(login_font, 16, "bold"),
#     relief="flat", border=0, command=signin
# )
# btn_log.place(x=200, y=350)

# lbl_signup = tk.Label(frm, text="Don't have an account?", bg="white", fg="black", font=(login_font, 12))
# lbl_signup.place(x=165, y=440)
# btn_signup = tk.Button(
#     frm, text="Sign up", border=0, cursor="hand2", font=(login_font, 12, "italic bold"), relief="flat",
#     fg="#432771", bg="white", command=nav_signup
# )
# btn_signup.place(x=390, y=439)

# btn_fgpass = tk.Button(
#     frm, text="Forgot password?", border=0, cursor="hand2", font=(login_font, 12, "italic bold"), relief="flat",
#     fg="#432771", bg="white", command=fgpass
# )
# btn_fgpass.place(x=220, y=480)

# log_w.mainloop()


