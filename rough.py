import tkinter as tk
from tkinter import messagebox, ttk, filedialog

from PIL import Image, ImageTk
import mysql.connector

out_font = "Courier new"
out_color = "green"
outpage = tk.Tk()
outpage.geometry('1250x850')
outpage.config(bg=out_color)
outpage.resizable(False, False)

frame_index = 0
home_page_created = False
login_page_created = False
signup_page_created = False

########################  login page  #####################################

def signin():
    outpage.deiconify()
    login_color = "#e13746"
    login_font = "Courier new"

    log_w = tk.Frame(outpage, width=1250, height=850, bg='black')
    log_w.place(x=0, y=0)

    lbl_head = tk.Label(log_w, text="Sign in", bg="white", fg=login_color, font=(login_font, 28, "bold"))
    lbl_head.place(x=170, y=80)
    


########################  signup page  #####################################

def signup():
    pass


########################   outpage base #################################
# def outhome():
#     global home_page_created

#     if home_page_created:
#         return
    

#     title_color = "#6f86b9"
#     outpage.config(bg=title_color)
#     outpage.title("Criminal Face Recognition System")
#     home_page_created = True

#     my_color = "#6f86b9"

#     style = ttk.Style()
#     style.configure('TRoundedFrame.TFrame', background=my_color, borderwidth=5, relief='flat')



#     #########  outpage Contd  ###############
#     def animate_gif():
#         global frame_index

#         frame = gif_frames[frame_index]
#         disp_frame = ImageTk.PhotoImage(frame)
#         lbl_icon.configure(image=disp_frame)
#         lbl_icon.image = disp_frame

#         frame_index = (frame_index + 1) % len(gif_frames)
#         outpage.after(100, animate_gif)

#     # Load the animated GIF frames
#     gif = Image.open("icon_img/eye.gif")
#     gif_frames = []
#     try:
#         while True:
#             frame = gif.copy()
#             frame.thumbnail((250, 250))
#             gif_frames.append(frame)
#             # Seek next frame
#             gif.seek(len(gif_frames))
#     except EOFError:
#         pass


#     lbl_title = tk.Label(outpage, text="CRIMINAL FACE RECOGNITION SYSTEM", font=("Courier new", 24, 'bold'), bg=title_color)
#     lbl_title.pack(pady=20, ipadx=5, ipady=5)

#     #frame 1
#     frm1 = ttk.Frame(outpage, style='TRoundedFrame.TFrame')
#     frm1.pack()

#     lbl_icon = tk.Label(frm1, bg=my_color)
#     lbl_icon.pack()

#     lbl_details = tk.Label(frm1, text="Detects human faces through live footage and recognize them.\nBetter than other biometric scanners which require very close physical presence.\nLearn more about us below.",
#                         font=("Verdana", 16), bg=my_color)
#     lbl_details.pack(padx=5, ipadx=30, ipady=30)

#     #frame 2
#     frm2 = tk.Frame(frm1)
#     frm2.pack(padx=10, pady=50)
#     frm2.configure(background=my_color)

#     btn_login = tk.Button(frm2, text="LOGIN", width=14, cursor='hand2', fg="white", font=("Verdana", 16), relief="flat", bg="#e13746", command=signin)
#     btn_login.pack(side='left', padx=(0, 20))

#     btn_signup = tk.Button(frm2, text="SIGN UP", width=14, cursor='hand2', fg="white", font=("Verdana", 16), relief="flat", bg="#432771")
#     btn_signup.pack(side='right', padx=(20, 0))

#     btn_learn_more = tk.Button(frm1, text="Learn more about us.", cursor='hand2',fg="black", border=0, font=("Verdana", 11, "italic", "underline"), relief="flat", bg=my_color)
#     btn_learn_more.pack(pady=5)

#     animate_gif()

#     outpage.iconify()

outmenu_bar = tk.Menu(outpage)
outpage.config(menu=outmenu_bar)

home_menu = tk.Menu(outmenu_bar, tearoff=0)
home_menu.add_command(label='Home page')
home_menu.add_separator()
home_menu.add_command(label="Exit", command=outpage.quit)
outmenu_bar.add_cascade(label="HOME", menu=home_menu)

user_menu = tk.Menu(outmenu_bar, tearoff=0)
user_menu.add_command(label="Sign in", command=signin)
user_menu.add_separator()
user_menu.add_command(label="Sign up")
outmenu_bar.add_cascade(label="USER", menu=user_menu)

outpage.mainloop()
