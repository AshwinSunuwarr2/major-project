import tkinter as tk
from tkinter import messagebox, ttk

root = tk.Tk()
root.geometry("720x560")
root.resizable(False, False)

my_font = "Courier new"
frm = tk.Frame(root, width=850, height=660, bg="white")
frm.place(x=0, y=0)

lbl_name = tk.Label(frm, text="Sign in", bg="white", fg="orange", font=(my_font, 28, "bold"))
lbl_name.place(x=170, y=80)

# username label
user = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(my_font, 18))
user.place(x=170, y=170)
user.insert(0, "Username")

tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=203)

# password label
psw = tk.Entry(frm, width=32, fg="black", border=0, bg="white", font=(my_font, 18))
psw.place(x=170, y=270)
psw.insert(0, "Password")

tk.Frame(frm, width=350, height=2, bg="black").place(x=169, y=303)

btn_log = tk.Button(frm, text="SIGN IN", width=8, bg="grey", font=(my_font, 16, "bold"),relief="flat", border=0)
btn_log.place(x=250, y=350)

# sign up or forgot pass
btn_psw_forgot = tk.Button(frm, text="Forgot password?", font=(my_font, 12, "italic"), relief="flat", fg="red", bg="white")
btn_psw_forgot.place(x=165, y=410)
lbl_signup = tk.Label(frm, text="Already have an account.", bg="white", fg="black", font=(my_font, 12))
lbl_signup.place(x=332, y=415)



root.mainloop()