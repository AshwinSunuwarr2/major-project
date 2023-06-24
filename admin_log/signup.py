import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

signup_font = "Courier new"
signup_color = "#432771"

signup_w = tk.Tk()
signup_w.title("Sign up")
signup_w.geometry("720x560")
signup_w.resizable(False, False)


conn = mysql.connector.connect(
    host  = 'localhost',
    user = 'root',
    password = '',
    database = 'mydb',
    port = '3306'
)

c = conn.cursor()

# sign up confiramtion
def signup():
    name = user.get()
    passw = psw.get()
    c_passw = c_psw.get()

    if name ==  '' or passw == '' or c_passw == '':
            messagebox.showerror('Invalid', 'You must fill all fields')
            return

    if passw != c_passw:
        messagebox.showerror('Invalid', 'Both password should match.')
        return

    if len(passw) < 8:
        messagebox.showerror('Invalid', 'Password must be atleast of 8 characters.')
        return

    insert_admin = "insert into admins(user, password) values (%s, %s)"
    vals = (name, passw)
    
    try:
        c.execute(insert_admin, vals)
        conn.commit()
        messagebox.showinfo('Success', "You're now registered.")
        return
    
    except mysql.connector.Error as error:
        messagebox.showerror('Database error', str(error))

    user.delete(0, tk.END)
    psw.delete(0, tk.END)
    c_psw.delete(0, tk.END)



# log btn
def nav_log():
    signup_w.withdraw()
    import login as login


# signup_w contd
signup_font = signup_font
frm = tk.Frame(signup_w, width=850, height=660, bg="white")
frm.place(x=0, y=0)

lbl_head = tk.Label(frm, text="Sign up", bg="white", fg=signup_color, font=(signup_font, 28, "bold"))
lbl_head.place(x=170, y=80)


def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, "Username")

# username label
user = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(signup_font, 16))
user.place(x=170, y=158)
user.insert(0, "Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=183)

def on_enter(e):
    psw.delete(0, "end")

def on_leave(e):
    name = psw.get()
    if name == '':
        psw.insert(0, "Password")

# password label
psw = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(signup_font, 16))
psw.place(x=170, y=225)
psw.insert(0, "Password")
psw.bind('<FocusIn>', on_enter)
psw.bind('<FocusOut>', on_leave)

tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=250)

def on_enter(e):
    c_psw.delete(0, "end")

def on_leave(e):
    name = c_psw.get()
    if name == '':
        c_psw.insert(0, "Confirm Password")

# confirm password label
c_psw = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(signup_font, 16))
c_psw.insert(0, "Confirm Password")
c_psw.place(x=170, y=295)
c_psw.bind('<FocusIn>', on_enter)
c_psw.bind('<FocusOut>', on_leave)

tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=320)

btn_signup = tk.Button(frm, text="SIGN UP", width=18, bg=signup_color, cursor='hand2', fg="white", font=(signup_font, 16, "bold"),relief="flat", border=0, command=signup)
btn_signup.place(x=200, y=360)

# sign up btn
lbl_signup = tk.Label(frm, text="Already have an account?", bg="white", fg="black", font=(signup_font, 12))
lbl_signup.place(x=160, y=440)
btn_log = tk.Button(frm, text="Sign in", border=0, cursor="hand2", font=(signup_font, 12, "italic bold"), relief="flat", fg="#e13746", bg="white", command=nav_log)
btn_log.place(x=407, y=439)



signup_w.mainloop()