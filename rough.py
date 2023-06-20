# import tkinter as tk
# from tkinter import filedialog
# import mysql.connector
# from mysql.connector import Error

# # Create the Tkinter UI
# root = tk.Tk()

# frame = tk.Frame(root)
# root.title("Image Uploader")
# root.geometry("1080x790")

# # btn_browse['command'] = selectPic
# img_label = tk.Label(frame, text="Front view", font=('Courier new', 16))
# img_show_label = tk.Label(frame)
# btn_browse = tk.Button(frame, font=('Courier new', 16))

# frame.pack()

# img_label.grid(row=0, column=0)
# img_show_label(row=1, column=0)
# btn_browse.grid(row=2, columnspan=0)

# root.mainloop()


import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import Error

# Create the Tkinter UI
root = tk.Tk()
frame = tk.Frame(root)
root.title("Image Uploader")
root.geometry("1080x790")

# Browse button command
def selectPic():
    filepath = filedialog.askopenfilename()
    img = ImageTk.PhotoImage(Image.open(filepath))
    img_show_label.config(image=img)
    img_show_label.image = img

img_label = tk.Label(frame, text="Front view", font=('Courier new', 16))
img_show_label = tk.Label(frame)
btn_browse = tk.Button(frame, text="Browse", font=('Courier new', 16))
btn_browse['command'] = selectPic

frame.pack()
img_label.grid(row=0, column=0)
img_show_label.grid(row=1, column=0)
btn_browse.grid(row=2, columnspan=2)

root.mainloop()
