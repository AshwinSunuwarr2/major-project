import tkinter as tk
from tkinter import messagebox, ttk

import mysql.connector


my_color = "#e13746"
my_font = "Courier new"

log_w = tk.Tk()
log_w.title("Login")
log_w.geometry("720x560")
log_w.resizable(False, False)


conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    port = '3306',
    database = 'mydb'
)
c = conn.cursor()


def signin():
    username = user.get()
    passw = psw.get()

    db_info = "select 'user', 'password' from admins where user=%s and password=%s"
    vals = (username, passw)
    c.execute(db_info, vals)
    result = c.fetchone()

    if result:
        log_w.destroy()
        import new as new

    else:
        messagebox.showerror("Invalid", "Username or password not correct.")
        return


def nav_signup():
    log_w.withdraw()
    import signup as signup


my_font = "Courier new"
frm = tk.Frame(log_w, width=850, height=660, bg="white")
frm.place(x=0, y=0)

lbl_head = tk.Label(frm, text="Sign in", bg="white", fg=my_color, font=(my_font, 28, "bold"))
lbl_head.place(x=170, y=80)


def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, "Username")

# username label
user = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(my_font, 18))
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

# password label
psw = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(my_font, 18))
psw.place(x=170, y=270)
psw.insert(0, "Password")
psw.bind('<FocusIn>', on_enter)
psw.bind('<FocusOut>', on_leave)

tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=303)

btn_log = tk.Button(frm, text="SIGN IN", width=18, bg=my_color, cursor='hand2', fg="white", font=(my_font, 16, "bold"),relief="flat", border=0, command=signin)
btn_log.place(x=200, y=350)

# log in btn
lbl_signup = tk.Label(frm, text="Don't have an account?", bg="white", fg="black", font=(my_font, 12))
lbl_signup.place(x=165, y=440)
btn_signup = tk.Button(frm, text="Sign up", border=0, cursor="hand2", font=(my_font, 12, "italic bold"), relief="flat", fg="#432771", bg="white", command=nav_signup)
btn_signup.place(x=390, y=439)



log_w.mainloop()