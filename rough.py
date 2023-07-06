
# from tkinter import *
# from tkinter import ttk

# main_color = "#b2bedc"
# main_font = "Courier new"

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
#         self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

#     def configure_scrollregion(self, event):
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

# class Rough:
#     def __init__(self, root):
#         self.root = root 
#         root.state("zoomed")

#         main_frame = ScrolledFrame(root)
#         main_frame.pack(fill="both", expand=True)

#         lbl_head = Label(main_frame.inner_frame, text="Criminal Face Recognition System", font=(main_font, 18, "bold"), bg="grey")
#         lbl_head.pack(side="top", pady=20)

#         lists = [1, 2, 3, 4, 5]

#         def create_frame(item):
#             frm_item = Frame(main_frame.inner_frame, bg="black", height=350, width=750, bd=1)
#             frm_item.pack(side="top", padx=380, pady=8)
#             lbl_name = Label(frm_item, text="Name: ")
#             lbl_name.place(x=10, y=10)
#             entry_name = Entry(frm_item)
#             entry_name.place(x=29, y=10)

#         for item in lists:
#             create_frame(item)

# if __name__ == "__main__":
#     root = Tk()
#     rough_window = Rough(root)
#     root.mainloop()

from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk
import io
main_color = "#b2bedc"
main_font = "Courier new"

class ScrolledFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        # Create a canvas
        self.canvas = Canvas(self, borderwidth=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind("<Configure>", self.configure_scrollregion)

        # Create a frame inside the canvas
        self.inner_frame = Frame(self.canvas, bg="grey")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

    def configure_scrollregion(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class Rough:
    def __init__(self, root):
        self.root = root 
        root.state("zoomed")

        main_frame = ScrolledFrame(root)
        main_frame.pack(fill="both", expand=True)

        lbl_head = Label(main_frame.inner_frame, text="Criminal Details", font=(main_font, 18, "bold"), bg="grey")
        lbl_head.pack(side="top", pady=20)

        lists = [1, 2, 3, 4, 5]

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


        for row in results:
            # create_frame(item)
            frm_item = Frame(main_frame.inner_frame, bg="white", height=350, width=900, bd=1)
            frm_item.pack(side="top", padx=310, pady=8)


            # ------------ left labels ---------- #
            lbl_name = Label(frm_item, bg="white", text="Name: ", font=(main_font, 12))
            lbl_name.place(x=178, y=5, anchor="ne")
            entry_name = Entry(frm_item, font=(main_font, 12), bg='pink',width=35, relief="flat")
            entry_name.insert(0, row[1])
            entry_name.place(x=178, y=2)

            lbl_name = Label(frm_item, bg="white", text="Father's Name: ", font=(main_font, 12))
            lbl_name.place(x=178, y=35, anchor="ne")
            father_entry = Entry(frm_item, font=(main_font, 12), bg='pink',width=35, relief="flat")
            father_entry.insert(0, row[2])
            father_entry.place(x=178, y=32)
            
            lbl_name = Label(frm_item, bg="white", text="Mother's Name: ", font=(main_font, 12))
            lbl_name.place(x=178, y=67, anchor="ne")
            mother_entry = Entry(frm_item, font=(main_font, 12), bg='pink',width=35, relief="flat")
            mother_entry.insert(0, row[2])
            mother_entry.place(x=178, y=64)

            lbl_name = Label(frm_item, bg="white", text="Crime Committed: ", font=(main_font, 12))
            lbl_name.place(x=178, y=105, anchor="ne")
            crime_entry = Text(frm_item, font=(main_font, 12), bg='pink', height=3, width=35, relief="flat")
            crime_entry.insert("1.0", row[7])
            crime_entry.place(x=178, y=102)

            #   --------- right labels ---------#
            lbl_name = Label(frm_item, bg="white", text="ID: ", font=(main_font, 12))
            lbl_name.place(x=680, y=5, anchor="ne")
            id_entry = Entry(frm_item, font=(main_font, 12), bg='pink',width=21, relief="flat")
            id_entry.insert(0, row[0])
            id_entry.place(x=675, y=2)

            lbl_name = Label(frm_item, bg="white", text="Age: ", font=(main_font, 12))
            lbl_name.place(x=680, y=35, anchor="ne")
            age_entry = Entry(frm_item, font=(main_font, 12), bg='pink',width=21, relief="flat")
            age_entry.insert(0, row[4])
            age_entry.place(x=675, y=32)

            lbl_name = Label(frm_item, bg="white", text="Gender: ", font=(main_font, 12))
            lbl_name.place(x=680, y=67, anchor="ne")
            gender_entry = Entry(frm_item, font=(main_font, 12), bg='pink',width=21, relief="flat")
            gender_entry.insert(0, row[5])
            gender_entry.place(x=675, y=64)

            lbl_name = Label(frm_item, bg="white", text="Nationality: ", font=(main_font, 12))
            lbl_name.place(x=680, y=100, anchor="ne")
            nationality_entry = Entry(frm_item, font=(main_font, 12), bg='pink',width=21, relief="flat")
            nationality_entry.insert(0, row[6])
            nationality_entry.place(x=675, y=96)

            # --------- img for single criminals -----------#
            lbl_front = Label(frm_item)
            lbl_front.place(x=250, y=210)
            lbl_left = Label(frm_item)
            lbl_left.place(x=410, y=210)
            lbl_right = Label(frm_item)
            lbl_right.place(x=570, y=210)


            # ------ images ---------#
            front_data = row[8]
            left_data = row[9]
            right_data = row[10]

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



            btn_del = Button(frm_item, width=9, text="EDIT", bg='#e4d00a', fg="black", font=(main_font, 14), cursor="hand2", relief="sunken")
            btn_del.place(x=740, y=230)
            btn_del = Button(frm_item, width=9, text="DELETE", bg='#e44c5c', fg="black", font=(main_font, 14), cursor="hand2", relief="sunken")
            btn_del.place(x=740, y=280)

if __name__ == "__main__":
    root = Tk()
    rough_window = Rough(root)
    root.mainloop()