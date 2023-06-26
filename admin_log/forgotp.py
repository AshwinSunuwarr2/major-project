from tkinter import *
from tkinter import ttk, messagebox
from tkinter import messagebox, ttk, filedialog

from PIL import Image, ImageTk
import mysql.connector
    


class ForgetPass:    
    def __init__(self, root):
        self.root = root
        self.root.title("Reset password")
        self.root.geometry("720x560")
        self.root.resizable(False, False)
        self.root.config(bg="white")


        self.var_entry_name = StringVar()
        self.var_entry_newpass = StringVar()
        self.var_entry_confirmpass = StringVar()


        forgot_color = "red"
        forgot_font = "Courier new"

        lbl_head = Label(self.root, text="Password reset", bg="white", fg=forgot_color, font=(forgot_font, 28, "bold"))
        lbl_head.place(x=140, y=86)


        def on_enter(e):
            entry_name.delete(0, "end")

        def on_leave(e):
            user = entry_name.get()
            if user == '':
                entry_name.insert(0, 'Enter your Username')

        entry_name = Entry(self.root, textvariable=self.var_entry_name, width=32, fg="black", border=0, bg="white", font=(forgot_font, 16))
        entry_name.place(x=140, y=195)
        entry_name.insert(0, "Enter your Username")
        entry_name.bind('<FocusIn>', on_enter)
        entry_name.bind('<FocusOut>', on_leave)

        Frame(self.root, width=350, height=2, bg="black").place(x=140, y=222)

        def on_enter(e):
            entry_newpass.delete(0, "end")

        def on_leave(e):
            newpsw = entry_newpass.get()
            if newpsw == '':
                entry_newpass.insert(0, 'Enter new password')

        entry_newpass = Entry(self.root, textvariable=self.var_entry_newpass, width=32, fg="black", border=0, bg="white", font=(forgot_font, 16))
        entry_newpass.place(x=140, y=255)
        entry_newpass.insert(0, "Enter new password")
        entry_newpass.bind('<FocusIn>', on_enter)
        entry_newpass.bind('<FocusOut>', on_leave)

        Frame(self.root, width=350, height=2, bg="black").place(x=140, y=282)

        def on_enter(e):
            entry_confirmpass.delete(0, "end")

        def on_leave(e):
            c_newpsw = entry_confirmpass.get()
            if c_newpsw == '':
                entry_confirmpass.insert(0, 'Confirm new password')

        entry_confirmpass = Entry(self.root, textvariable=self.var_entry_confirmpass, width=32, fg="black", border=0, bg="white", font=(forgot_font, 16))
        entry_confirmpass.place(x=140, y=315)
        entry_confirmpass.insert(0, "Confirm new password")
        entry_confirmpass.bind('<FocusIn>', on_enter)
        entry_confirmpass.bind('<FocusOut>', on_leave)

        Frame(self.root, width=350, height=2, bg="black").place(x=140, y=342)

        btn_confirm = Button(
            self.root, text="CONFIRM", width=16, bg=forgot_color, cursor='hand2', fg="white", font=(forgot_font, 16, "bold"),
            relief="flat", border=0, command=self.confirmuser
        )
        btn_confirm.place(x=180, y=385)



    def confirmuser(self):
        user = self.var_entry_name.get()
        newp = self.var_entry_newpass.get()
        c_newp = self.var_entry_confirmpass.get()

        if newp == '' or c_newp == '':
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
                    return

                except mysql.connector.Error as error:
                    messagebox.showerror("Error", str(error), parent=self.root)

        else:
            messagebox.showerror('Invalid', 'User does not exist.', parent=self.root)


        self.var_entry_name.delete(0, END)
        self.var_entry_newpass.delete(0, END)
        self.var_entry_confirmpass.delete(0, END)




if __name__ == "__main__":
    root = Tk()
    fgpsw = ForgetPass(root)
    root.mainloop()
