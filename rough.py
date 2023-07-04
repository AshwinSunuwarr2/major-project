import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector
import io

def crim_img():
    c_id = entry_id.get().strip()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port="3306",
        database="mydb"
    )
    c = conn.cursor()

    query = "select front_img, left_img, right_img from criminal_reg where id=%s"
    vals = (c_id,)
    c.execute(query, vals)
    result = c.fetchall()
    print("image fetching")

    if result:
        front_data = result[0][0]
        left_data = result[0][1]
        right_data = result[0][2]

        f_img = Image.open(io.BytesIO(front_data))
        f_photo = ImageTk.PhotoImage(f_img)
        lbl_front.configure(image=f_photo)
        lbl_front.image = f_photo

        l_img = Image.open(io.BytesIO(left_data))
        l_photo = ImageTk.PhotoImage(l_img)
        lbl_left.configure(image=l_photo)
        lbl_left.image = l_photo

        r_img = Image.open(io.BytesIO(right_data))
        r_photo = ImageTk.PhotoImage(r_img)
        lbl_right.configure(image=r_photo)
        lbl_right.image = r_photo

        print("..............image is displayed.............")
    else:
        print("------------------ error -------------")

# Create the Tkinter window and labels
window = tk.Tk()

lbl_front = tk.Label(window)
lbl_front.pack()

lbl_left = tk.Label(window)
lbl_left.pack()

lbl_right = tk.Label(window)
lbl_right.pack()

entry_id = tk.Entry(window)
entry_id.pack()

button_fetch = tk.Button(window, text="Fetch Images", command=crim_img)
button_fetch.pack()

# Run the Tkinter event loop
window.mainloop()
