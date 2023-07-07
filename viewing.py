from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk
import io
main_color = "#b2bedc"
main_font = "Courier new"

# class ScrolledFrame(Frame):
#     def __init__(self, parent, *args, **kwargs):
#         Frame.__init__(self, parent, *args, **kwargs)

#         # Create a canvas
#         self.canvas = Canvas(self, borderwidth=0)
#         self.canvas.pack(side="left", fill="both", expand=True)

#         # Create a scrollbar
#         scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
#         scrollbar.pack(side="right", fill="y")

#         self.canvas.configure(yscrollcommand=scrollbar.set)
#         self.canvas.bind("<Configure>", self.configure_scrollregion)

#         # Create a frame inside the canvas
#         self.inner_frame = Frame(self.canvas, bg="grey")
#         self.canvas.create_window((0, 0), window=self.inner_frame)

#         title_frame = Frame(self.canvas, bg="grey")
#         title_frame.place(x=0, y=0, height=40, relwidth=1)
#         lbl_head = Label(title_frame, text="Criminal Details",font=("Arial", 20, "bold"), fg="white", bg="grey")
#         lbl_head.pack(fill="x", pady=10)

        # view_id_btn = Button(title_frame, text="Search", width=8, font=('Courier New', 12), fg ="black", bg="#ffb067")
        # view_id_btn.place(x=1370, y=2)

        # lbl_head = Label(title_frame, text="ID:", font=('Courier New', 16, 'bold'), fg="white", bg="grey")
        # lbl_head.place(x=1200, y=4, anchor='ne')
        # id_entry = Entry(title_frame, width=14, font=('Courier New', 12), bd=1)
        # id_entry.place(x=1205, y=6)

#     def configure_scrollregion(self, event):
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class Rough:
    def __init__(self, root):
        self.root = root 
        root.state("zoomed")

        frm_top = Frame(root, bg="black")
        frm_top.place(x=0, y=2, relwidth=1, height=50)

        lbl_head = Label(frm_top, text="Criminal Details", font=("Arial", 20, "bold"), fg="white", bg="black")
        lbl_head.place(relx=0.4, y=6)

        view_id_btn = Button(frm_top, text="Search", width=8, font=('Courier New', 12), fg ="black", bg="#ffb067")
        view_id_btn.place(x=1370, y=8)

        lbl_head = Label(frm_top, text="ID:", font=('Courier New', 16, 'bold'), fg="white", bg="grey")
        lbl_head.place(x=1200, y=8, anchor='ne')
        id_entry = Entry(frm_top, width=14, font=('Courier New', 12), bd=1)
        id_entry.place(x=1205, y=10)

        frm = Frame(root)
        frm.place(x=0, y=50, relheight=1, relwidth=1)

        canvas = Canvas(frm)
        scroll_y = Scrollbar(frm, orient="vertical", command=canvas.yview)

        main_frame = Frame(canvas)


        conn = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                port = '3306',
                database = 'mydb'
            )
        c = conn.cursor()

        insert_query = "select * from criminal_reg"
        c.execute(insert_query)
        results = c.fetchall()

        entry_color = "white"
        font_color = "red"
        for row in results:
            # create_frame(item)
            frm_item = Frame(main_frame, bg="white", height=350, width=900, bd=1)
            frm_item.pack(side="top", padx=310, pady=20)
            # ------------ left labels ---------- #
            lbl_name = Label(frm_item, bg="white", text="Name: ", font=(main_font, 12))
            lbl_name.place(x=178, y=5, anchor="ne")
            entry_name = Entry(frm_item, font=(main_font, 12), fg=font_color, bg=entry_color,width=35, relief="flat")
            entry_name.insert(0, row[1])
            entry_name.place(x=178, y=5)

            lbl_name = Label(frm_item, bg="white", text="Father's Name: ", font=(main_font, 12))
            lbl_name.place(x=178, y=35, anchor="ne")
            father_entry = Entry(frm_item, font=(main_font, 12), fg=font_color, bg=entry_color,width=35, relief="flat")
            father_entry.insert(0, row[2])
            father_entry.place(x=178, y=35)
            
            lbl_name = Label(frm_item, bg="white", text="Mother's Name: ", font=(main_font, 12))
            lbl_name.place(x=178, y=67, anchor="ne")
            mother_entry = Entry(frm_item, font=(main_font, 12), fg=font_color, bg=entry_color,width=35, relief="flat")
            mother_entry.insert(0, row[2])
            mother_entry.place(x=178, y=67)

            lbl_name = Label(frm_item, bg="white", text="Crime Committed: ", font=(main_font, 12))
            lbl_name.place(x=178, y=105, anchor="ne")
            crime_entry = Text(frm_item, font=(main_font, 12), fg=font_color, bg=entry_color, height=3, width=35, relief="flat")
            crime_entry.insert("1.0", row[7])
            crime_entry.place(x=178, y=105)

            #   --------- right labels ---------#
            lbl_name = Label(frm_item, bg="white", text="ID: ", font=(main_font, 12))
            lbl_name.place(x=680, y=5, anchor="ne")
            id_entry = Entry(frm_item, font=(main_font, 12), fg=font_color, bg=entry_color,width=21, relief="flat")
            id_entry.insert(0, row[0])
            id_entry.place(x=675, y=5)

            # cid = id_entry.get().strip()

            lbl_name = Label(frm_item, bg="white", text="Age: ", font=(main_font, 12))
            lbl_name.place(x=680, y=35, anchor="ne")
            age_entry = Entry(frm_item, font=(main_font, 12), fg=font_color, bg=entry_color,width=21, relief="flat")
            age_entry.insert(0, row[4])
            age_entry.place(x=675, y=35)

            lbl_name = Label(frm_item, bg="white", text="Gender: ", font=(main_font, 12))
            lbl_name.place(x=680, y=67, anchor="ne")
            gender_entry = Entry(frm_item, font=(main_font, 12), fg=font_color, bg=entry_color,width=21, relief="flat")
            gender_entry.insert(0, row[5])
            gender_entry.place(x=675, y=67)

            lbl_name = Label(frm_item, bg="white", text="Nationality: ", font=(main_font, 12))
            lbl_name.place(x=680, y=100, anchor="ne")
            nationality_entry = Entry(frm_item, font=(main_font, 12), fg=font_color, bg=entry_color, width=21, relief="flat")
            nationality_entry.insert(0, row[6])
            nationality_entry.place(x=675, y=100)

            # --------- img for single criminals -----------#
            lbl_left = Label(frm_item, height=95, width=105)
            lbl_left.place(x=250, y=210)
            lbl_front = Label(frm_item, height=115, width=110)
            lbl_front.place(x=410, y=200)
            lbl_right = Label(frm_item, height=95, width=105)
            lbl_right.place(x=570, y=210)


            # ------ images ---------#
            front_data = row[8]
            left_data = row[9]
            right_data = row[10]

            f_img = Image.open(io.BytesIO(front_data))
            f_img.thumbnail((110, 115))  # Resize the image to fit label size
            f_photo = ImageTk.PhotoImage(f_img)
            lbl_front.configure(image=f_photo)
            lbl_front.image = f_photo

            l_img = Image.open(io.BytesIO(left_data))
            l_img.thumbnail((105, 95))  # Resize the image to fit label size
            l_photo = ImageTk.PhotoImage(l_img)
            lbl_left.configure(image=l_photo)
            lbl_left.image = l_photo

            r_img = Image.open(io.BytesIO(right_data))
            r_img.thumbnail((105, 95))  # Resize the image to fit label size
            r_photo = ImageTk.PhotoImage(r_img)
            lbl_right.configure(image=r_photo)
            lbl_right.image = r_photo


            btn_del = Button(frm_item, width=9, text="EDIT", bg='#e4d00a', fg="black", font=(main_font, 14), cursor="hand2", relief="sunken", command=cupdate)
            btn_del.place(x=740, y=230)
            btn_del = Button(frm_item, width=9, text="DELETE", bg='#e44c5c', fg="black", font=(main_font, 14), cursor="hand2", relief="sunken")
            btn_del.place(x=740, y=280)

        def cupdate(self):
            cid = id_entry.get().strip()
            print(cid)


        # put the frame to be scrolled in the canvas  ---------- group of widgets need use of canvas 
        canvas.create_window(0, 0, anchor='nw', window=main_frame)
        # everything displayed confirmation
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), 
                        yscrollcommand=scroll_y.set)
                        
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')
if __name__ == "__main__":
    root = Tk()
    rough_window = Rough(root)
    root.mainloop()