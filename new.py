import tkinter as tk
from tkinter import ttk, Toplevel
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1190x700")

title_color = "#6f86b9"
root.config(bg=title_color, padx=20, pady=20)
root.title("Criminal Face Recognition System")

my_color = "#6f86b9"

style = ttk.Style()
style.configure('TRoundedFrame.TFrame', background=my_color, borderwidth=5, relief='flat')

def nav_login():
    root.destroy()
    import login

def animate_gif():
    global frame_index

    frame = gif_frames[frame_index]
    disp_frame = ImageTk.PhotoImage(frame)
    lbl_icon.configure(image=disp_frame)
    lbl_icon.image = disp_frame

    frame_index = (frame_index + 1) % len(gif_frames)
    root.after(100, animate_gif)

# Load the animated GIF frames
gif = Image.open("icon_img/eye.gif")
gif_frames = []
try:
    while True:
        frame = gif.copy()
        frame.thumbnail((250, 250))
        gif_frames.append(frame)
        # Seek next frame
        gif.seek(len(gif_frames))
except EOFError:
    pass

frame_index = 0

lbl_title = tk.Label(root, text="CRIMINAL FACE RECOGNITION SYSTEM", font=("Courier new", 24, 'bold'), bg=title_color)
lbl_title.pack(pady=20, ipadx=5, ipady=5)

# #canvas 
# canvas = tk.Canvas(root, bg="white")
# canvas.pack(fill='both', expand=True, ipadx=40, ipady=0)

#frame 1
frm1 = ttk.Frame(root, style='TRoundedFrame.TFrame')
frm1.pack(ipady=20)

lbl_icon = tk.Label(frm1, bg=my_color)
lbl_icon.pack()

lbl_details = tk.Label(frm1, text="System that detects human faces from live footage and recognize them.\nBetter than other biometric scanners as it doesnot requires physical presence.\nLet's dive into the system.",
                       font=("Verdana", 16), bg=my_color)
lbl_details.pack(pady=7, padx=5, ipadx=30, ipady=30)

#frame 2
frm2 = tk.Frame(frm1)
frm2.pack(padx=10, pady=50)
frm2.configure(background=my_color)

btn_login = tk.Button(frm2, text="LOGIN", width=14, fg="white", font=("Verdana", 16), relief="flat", bg="#e13746", command=nav_login)
btn_login.pack(side='left', padx=(0, 20), pady=10)

btn_signup = tk.Button(frm2, text="SIGN UP", width=14, fg="white", font=("Verdana", 16), relief="flat", bg="#432771")
btn_signup.pack(side='right', padx=(20, 0), pady=10)

btn_learn_more = tk.Button(frm1, text="Learn more about us.", font=("Verdana", 11, "italic"), relief="flat", bg=my_color)
btn_learn_more.pack(pady=5)

animate_gif()

root.mainloop()
