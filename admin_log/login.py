import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

login_color = "#e13746"
login_font = "Courier new"

log_w = tk.Tk()
log_w.title("Login")
log_w.geometry("720x560")
log_w.resizable(False, False)

# Database connection setup
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port='3306',
    database='mydb'
)
c = conn.cursor()


def signin():
    username = user.get()
    passw = psw.get()

    if username == '' or passw == '':
        messagebox.showerror('Invalid', 'You must fill all fields')
        return

    db_info = "select user, password from admins where user=%s and password=%s"
    vals = (username, passw)
    c.execute(db_info, vals)
    result = c.fetchone()

    if result:
        log_w.destroy()
        import new as new
    else:
        messagebox.showerror("Invalid", "Username or password not correct.")
        return


def fgpass():
    log_w.withdraw()

    def confirmuser():
        user = entry_name.get()
        newp = entry_newpass.get()
        c_newp = entry_confirmpass.get()

        db_info = "select user from admins where user=%s"
        vals = (user,)
        c.execute(db_info, vals)
        yesuser = c.fetchone()

        if yesuser:
            if user == '' or newp == '' or c_newp == '':
                messagebox.showerror('Invalid', 'You must fill all fields')
                return
            elif newp != c_newp:
                messagebox.showerror('Invalid', 'Both passwords must match.')
                return
            elif len(newp) < 8:
                messagebox.showerror('Invalid', 'Password must be at least 8 characters long.')
                return
            else:
                insert_newpsw = "update admins set password=%s where user=%s"
                vals = (newp, user)

                try:
                    c.execute(insert_newpsw, vals)
                    conn.commit()
                    messagebox.showinfo("Success", "Password reset successful.")

                except mysql.connector.Error as error:
                    messagebox.showerror("Database Error", str(error))
                    return
        else:
            messagebox.showerror('Invalid', 'User does not exist.')
            return

        entry_name.delete(0, tk.END)
        entry_newpass.delete(0, tk.END)
        entry_confirmpass.delete(0, tk.END)
        

    fgpass_w = tk.Toplevel(log_w)
    fgpass_w.title("Reset password")
    fgpass_w.geometry("720x560")
    fgpass_w.resizable(False, False)
    fgpass_w.config(bg="white")

    lbl_head = tk.Label(fgpass_w, text="Password reset", bg="white", fg=login_color, font=(login_font, 28, "bold"))
    lbl_head.place(x=140, y=86)

    def on_enter(e):
        entry_name.delete(0, "end")

    def on_leave(e):
        user = entry_name.get()
        if user == '':
            entry_name.insert(0, 'Enter your Username')

    entry_name = tk.Entry(fgpass_w, width=32, fg="black", border=0, bg="white", font=(login_font, 16))
    entry_name.place(x=140, y=195)
    entry_name.insert(0, "Enter your Username")
    entry_name.bind('<FocusIn>', on_enter)
    entry_name.bind('<FocusOut>', on_leave)

    tk.Frame(fgpass_w, width=350, height=2, bg="black").place(x=140, y=222)

    def on_enter(e):
        entry_newpass.delete(0, "end")

    def on_leave(e):
        newpsw = entry_newpass.get()
        if newpsw == '':
            entry_newpass.insert(0, 'Enter new password')

    entry_newpass = tk.Entry(fgpass_w, width=32, fg="black", border=0, bg="white", font=(login_font, 16))
    entry_newpass.place(x=140, y=255)
    entry_newpass.insert(0, "Enter new password")
    entry_newpass.bind('<FocusIn>', on_enter)
    entry_newpass.bind('<FocusOut>', on_leave)

    tk.Frame(fgpass_w, width=350, height=2, bg="black").place(x=140, y=282)

    def on_enter(e):
        entry_confirmpass.delete(0, "end")

    def on_leave(e):
        c_newpsw = entry_confirmpass.get()
        if c_newpsw == '':
            entry_confirmpass.insert(0, 'Confirm new password')

    entry_confirmpass = tk.Entry(fgpass_w, width=32, fg="black", border=0, bg="white", font=(login_font, 16))
    entry_confirmpass.place(x=140, y=315)
    entry_confirmpass.insert(0, "Confirm new password")
    entry_confirmpass.bind('<FocusIn>', on_enter)
    entry_confirmpass.bind('<FocusOut>', on_leave)

    tk.Frame(fgpass_w, width=350, height=2, bg="black").place(x=140, y=342)

    btn_confirm = tk.Button(
        fgpass_w, text="CONFIRM", width=16, bg=login_color, cursor='hand2', fg="white", font=(login_font, 16, "bold"),
        relief="flat", border=0, command=confirmuser
    )
    btn_confirm.place(x=180, y=385)

    fgpass_w.deiconify()


def nav_signup():
    log_w.withdraw()
    import signup as signup


frm = tk.Frame(log_w, width=850, height=660, bg="white")
frm.place(x=0, y=0)

lbl_head = tk.Label(frm, text="Sign in", bg="white", fg=login_color, font=(login_font, 28, "bold"))
lbl_head.place(x=170, y=80)


def on_enter(e):
    user.delete(0, "end")


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, "Username")


user = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(login_font, 18))
user.place(x=170, y=170)
user.insert(0, "Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=203)


def on_enter(e):
    psw.delete(0, "end")


def on_leave(e):
    passw = psw.get()
    if passw == '':
        psw.insert(0, "Password")


psw = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(login_font, 18))
psw.place(x=170, y=270)
psw.insert(0, "Password")
psw.bind('<FocusIn>', on_enter)
psw.bind('<FocusOut>', on_leave)

tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=303)

btn_log = tk.Button(
    frm, text="SIGN IN", width=18, bg=login_color, cursor='hand2', fg="white", font=(login_font, 16, "bold"),
    relief="flat", border=0, command=signin
)
btn_log.place(x=200, y=350)

lbl_signup = tk.Label(frm, text="Don't have an account?", bg="white", fg="black", font=(login_font, 12))
lbl_signup.place(x=165, y=440)
btn_signup = tk.Button(
    frm, text="Sign up", border=0, cursor="hand2", font=(login_font, 12, "italic bold"), relief="flat",
    fg="#432771", bg="white", command=nav_signup
)
btn_signup.place(x=390, y=439)

btn_fgpass = tk.Button(
    frm, text="Forgot password?", border=0, cursor="hand2", font=(login_font, 12, "italic bold"), relief="flat",
    fg="#432771", bg="white", command=fgpass
)
btn_fgpass.place(x=220, y=480)

log_w.mainloop()




# import tkinter as tk
# from tkinter import messagebox, ttk

# import mysql.connector


# login_color = "#e13746"
# login_font = "Courier new"

# log_w = tk.Tk()
# log_w.title("Login")
# log_w.geometry("720x560")
# log_w.resizable(False, False)


# conn = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '',
#     port = '3306',
#     database = 'mydb'
# )
# c = conn.cursor()


# def signin():
#     username = user.get()
#     passw = psw.get()
    
#     if username ==  '' or passw == '':
#             messagebox.showerror('Invalid', 'You must fill all fields')
#             return

#     db_info = "select 'user', 'password' from admins where user=%s and password=%s"
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

#     fgpass_w = tk.Toplevel()

#     fgpass_w.title("Reset password")
#     fgpass_w.geometry("720x560")
#     fgpass_w.resizable(False, False)
#     fgpass_w.config(bg="white")

#     def confirmuser():
#         user = entry_name.get()
#         newp = entry_newpass.get()
#         c_newp = entry_confirmpass.get()

#         if user ==  '' or newp == '' or c_newp == '':
#             messagebox.showerror('Invalid', 'You must fill all fields')
#             return

#         db_info = "select 'user' from admins where user=%s"
#         vals = (user,)
#         c.execute(db_info, vals)
#         conn.commit()
#         yesuser = c.fetchone()

#         if yesuser:
#             if newp != c_newp:
#                 messagebox.showerror('Invalid', 'Both password must match.')
#             elif len(newp) < 8:
#                 messagebox.showerror('Invalid', 'Password must be atleast of 8 characters')
#             else:
#                 insert_newpsw = "update admins set password=%s where user=%s"
#                 vals = (newp, user)

#                 try:
#                     c.execute(insert_newpsw, vals)
#                     conn.commit()
#                     messagebox.showinfo("Success", f"Password reset success.")

#                 except mysql.connector.Error as error:
#                     messagebox.showerror("Database Error", str(error))

#         else:
#             messagebox.showerror('Invalid', 'User doesnot exists.')
#             return


#     lbl_head = tk.Label(fgpass_w, text="Password reset", bg="white", fg=login_color, font=(login_font, 28, "bold"))
#     lbl_head.place(x=140, y=86)

#     def on_enter(e):
#         entry_name.delete(0, "end")
#     def on_leave(e):
#         user = entry_name.get()
#         if user == '':
#             entry_name.insert(0, 'Enter your Username')
#     entry_name = tk.Entry(fgpass_w, width=32, fg="black", border=0, bg="white", font=(login_font, 16))
#     entry_name.place(x=140, y=195)
#     entry_name.insert(0, "Enter your Username")
#     entry_name.bind('<FocusIn>', on_enter)
#     entry_name.bind('<FocusOut>', on_leave)

#     tk.Frame(fgpass_w, width=350, height=2, bg="black").place(x=140, y=222)

#     def on_enter(e):
#         entry_newpass.delete(0, "end")
#     def on_leave(e):
#         newpsw = entry_newpass.get()
#         if newpsw == '':
#             entry_newpass.insert(0, 'Enter new password')
#     entry_newpass = tk.Entry(fgpass_w, width=32, fg="black", border=0, bg="white", font=(login_font, 16))
#     entry_newpass.place(x=140, y=255)
#     entry_newpass.insert(0, "Enter new password")
#     entry_newpass.bind('<FocusIn>', on_enter)
#     entry_newpass.bind('<FocusOut>', on_leave)

#     tk.Frame(fgpass_w, width=350, height=2, bg="black").place(x=140, y=282)

#     def on_enter(e):
#         entry_confirmpass.delete(0, "end")
#     def on_leave(e):
#         c_newpsw = entry_confirmpass.get()
#         if c_newpsw == '':
#             entry_confirmpass.insert(0, 'Confirm new password')
#     entry_confirmpass = tk.Entry(fgpass_w, width=32, fg="black", border=0, bg="white", font=(login_font, 16))
#     entry_confirmpass.place(x=140, y=315)
#     entry_confirmpass.insert(0, "Confirm new password")
#     entry_confirmpass.bind('<FocusIn>', on_enter)
#     entry_confirmpass.bind('<FocusOut>', on_leave)

#     tk.Frame(fgpass_w, width=350, height=2, bg="black").place(x=140, y=342)

#     btn_confirm = tk.Button(fgpass_w, text="CONFIRM", width=16, bg=login_color, cursor='hand2', fg="white", font=(login_font, 16, "bold"),relief="flat", border=0, command=confirmuser)
#     btn_confirm.place(x=180, y=385)

#     fgpass_w.deiconify()


# def nav_signup():
#     log_w.withdraw()
#     import signup as signup


# login_font = "Courier new"
# frm = tk.Frame(log_w, width=850, height=660, bg="white")
# frm.place(x=0, y=0)

# # def back():
# #     log_w.destroy()

# # btn_back = tk.Button(frm, text='Back', font=(login_font, 14), bg='white', relief='flat', fg='black', command=back)
# # btn_back.place(x=20, y=20)

# lbl_head = tk.Label(frm, text="Sign in", bg="white", fg=login_color, font=(login_font, 28, "bold"))
# lbl_head.place(x=170, y=80)


# def on_enter(e):
#     user.delete(0, "end")

# def on_leave(e):
#     name = user.get()
#     if name == '':
#         user.insert(0, "Username")

# # username label
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

# # password label
# psw = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(login_font, 18))
# psw.place(x=170, y=270)
# psw.insert(0, "Password")
# psw.bind('<FocusIn>', on_enter)
# psw.bind('<FocusOut>', on_leave)

# tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=303)

# btn_log = tk.Button(frm, text="SIGN IN", width=18, bg=login_color, cursor='hand2', fg="white", font=(login_font, 16, "bold"),relief="flat", border=0, command=signin)
# btn_log.place(x=200, y=350)

# # log in btn
# lbl_signup = tk.Label(frm, text="Don't have an account?", bg="white", fg="black", font=(login_font, 12))
# lbl_signup.place(x=165, y=440)
# btn_signup = tk.Button(frm, text="Sign up", border=0, cursor="hand2", font=(login_font, 12, "italic bold"), relief="flat", fg="#432771", bg="white", command=nav_signup)
# btn_signup.place(x=390, y=439)

# btn_fgpass = tk.Button(frm, text="Forgot password?", border=0, cursor="hand2", font=(login_font, 12, "italic bold"), relief="flat", fg="#432771", bg="white", command=fgpass)
# btn_fgpass.place(x=220, y=480)


# log_w.mainloop()