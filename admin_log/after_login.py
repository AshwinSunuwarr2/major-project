from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog

from PIL import Image, ImageTk
import mysql.connector


main_color = "#6f86b9"
main_font = "Courier new"


class AfterLogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x850+70+0")
        title_color = "#6f86b9"
        self.root.config(bg=title_color)
        self.root.title("Criminal Face Recognition System")
        self.root.resizable(False, False)


        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        # Create File menu
        home_menu = Menu(menu_bar, tearoff=0)
        home_menu.add_command(label="Register Criminal", command=self.criminal_reg)
        home_menu.add_separator()
        home_menu.add_command(label="Update Criminal Details", command=self.update_criminal)
        home_menu.add_separator()
        home_menu.add_command(label="Delete Criminal Details")
        home_menu.add_separator()
        home_menu.add_command(label="Exit", command=self.root.quit)
        home_menu.add_separator()
        menu_bar.add_cascade(label="Home", menu=home_menu)


        data_menu = Menu(menu_bar, tearoff=0)
        data_menu.add_command(label="View Criminal Details")
        data_menu.add_separator()
        data_menu.add_command(label="View Dataset")
        data_menu.add_separator()
        menu_bar.add_cascade(label="Datasets", menu=data_menu)

        cam_menu = Menu(menu_bar, tearoff=0)
        cam_menu.add_command(label="Recognize Criminals")
        cam_menu.add_separator()
        menu_bar.add_cascade(label="Camera", menu=cam_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Get help", command=self.help)
        help_menu.add_separator()
        help_menu.add_command(label="About us")
        help_menu.add_separator()
        menu_bar.add_cascade(label="More", menu=help_menu)


#-------------   functions  --------------------#

    def help(self):
        frm1 =Frame(self.root, width = 1250, height = 850, bg=main_color)
        frm1.place(x=0, y=0)
        lbl_text = Label(frm1, text="Canvas and frm_add are two different widgets in the Tkinter GUI toolkit in Python,\n and they have different purposes.",
                                font=(main_font, 18, 'bold'))
        lbl_text.place(x=30, y=60)
        

    def criminal_reg(self):
        add_color = "#b2bedc"
        add_font = "Courier new"
        self.front_file = StringVar()
        self.left_file = StringVar()
        self.right_file = StringVar()

        self.var_name_entry = StringVar()
        self.var_father_entry = StringVar()
        self.var_mother_entry = StringVar()
        self.var_age_entry = StringVar()
        self.var_gender_entry = StringVar()
        self.var_nationality_entry = StringVar()


         #------------------  registeration fxns ------------#

        def add_image(label, image_variable):
                f_types = [('PNG files', '*.png'), ('JPEG files', '*.jpg;*.jpeg')]
                file_path = filedialog.askopenfilename(filetypes=f_types)
                
                if file_path:
                    img = Image.open(file_path)
                    img.thumbnail((200, 200))  # Resize the image for preview
                    photo = ImageTk.PhotoImage(img)
                    label.configure(image=photo)
                    label.image = photo  # Store a reference to the image

                    image_variable.set(file_path)

        def submit():
            name = name_entry.get().strip()
            father_name = father_entry.get().strip()
            mother_name = mother_entry.get().strip()
            age = age_entry.get().strip()
            nationality = nationality_entry.get().strip()
            gender = gender_entry.get().strip()
            crime = crime_entry.get("1.0", END).strip()
            
            if name == '' or age == '' or gender == '' or nationality == '' or crime == '':
                messagebox.showerror("Error", "Please fill all required * fields.")
                return 

            try:
                age = int(age) 
            except ValueError:
                messagebox.showerror("Error", "Age must be valid.")
                return
            if age <= 16:
                messagebox.showerror("Error", "Age must be above 16.")
                return

            image_paths = [self.front_file.get(), self.left_file.get(), self.right_file.get()]
            image_data = []

            for path in image_paths:
                if path:
                    with open(path, 'rb') as file:
                        image_data.append(file.read())
                else:
                    messagebox.showerror("Error", "Please select all three images.")
                    return
                

            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                port='3306',
                database='mydb'
            )
            c = connection.cursor()

            data_insert = "INSERT INTO `criminal_reg`(`name`, `father_name`, `mother_name`, `age`, `gender`, `nationality`, `crime`, `front_img`, `left_img`, `right_img`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            vals = (name, father_name, mother_name, age, gender, nationality, crime, image_data[0], image_data[1], image_data[2])
                
            try:
                c.execute(data_insert, vals)
                connection.commit()
                fetch_id = "select id from criminal_reg where name=%s and crime=%s"
                values  = (name, crime)
                c.execute(fetch_id, values)
                crim_id = c.fetchone()
                connection.close()

                messagebox.showinfo("Success", f"Criminal with ID: {crim_id[0]} is now registered.")

            except mysql.connector.Error as error:
                messagebox.showerror("Database Error", str(error))

            name_entry.delete(0, END)
            father_entry.delete(0, END)
            mother_entry.delete(0, END)
            age_entry.delete(0, END)
            gender_entry.delete(0, END)
            nationality_entry.delete(0, END)
            crime_entry.delete("1.0", END)
            front_image_label.configure(image=None)  
            left_image_label.configure(image=None)      
            right_image_label.configure(image=None)
            front_image_label.image = None  # Clear reference to front image
            left_image_label.image = None  # Clear ref
            right_image_label.image = None  # Clear ref
            self.front_file.set("")
            self.left_file.set("")
            self.right_file.set("")






        frm_add = Frame(self.root, bg=add_color, width=1250, height=850)
        frm_add.place(x=0, y=0)

        lbl_head = Label(frm_add, text='Register Criminals', bg=add_color, font=(add_font, 28, 'bold'))
        lbl_head.place(x=380, y=30)

        #name label
        asterisk_label = Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=200, y=100, anchor='nw')

        text_label = Label(frm_add, text="Name:", font=('Courier New', 18, 'bold'), bg=add_color, fg="#383838")
        text_label.place(x=300, y=100, anchor='ne')

        name_entry = Entry(frm_add, textvariable=self.var_name_entry, width=40, font=('Courier New', 16))
        name_entry.place(x=380, y=100)

        #father name
        father_label = Label(frm_add, fg='#383838', text="Father's Name:", font=('Courier New', 18, 'bold'), bg=add_color)
        father_label.place(x=300, y=160, anchor='ne')
        father_entry = Entry(frm_add, textvariable=self.var_father_entry, width=40, font=('Courier New', 16))
        father_entry.place(x=380, y=160)

        #mother name
        mother_label = Label(frm_add, fg='#383838', text="Mother's Name:", font=('Courier New', 18, 'bold'), bg=add_color)
        mother_label.place(x=300, y=220, anchor='ne')
        mother_entry = Entry(frm_add, textvariable=self.var_mother_entry, width=40, font=('Courier New', 16))
        mother_entry.place(x=380, y=220)

        #age
        asterisk_label = Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=210, y=280, anchor='nw')

        text_label = Label(frm_add, text="Age:", font=('Courier New', 18, 'bold'), bg=add_color, fg="#383838")
        text_label.place(x=300, y=280, anchor='ne')

        age_entry = Entry(frm_add, textvariable=self.var_age_entry, width=40, font=('Courier New', 16))
        age_entry.place(x=380, y=280)

        #gender
        asterisk_label = Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=168, y=340, anchor='nw')

        text_label = Label(frm_add, text="Gender:", font=('Courier New', 18, 'bold'), bg=add_color, fg="#383838")
        text_label.place(x=300, y=340, anchor='ne')

        gender_entry = Entry(frm_add, textvariable=self.var_gender_entry, width=40, font=('Courier New', 16))
        gender_entry.place(x=380, y=340)

        #nationality
        asterisk_label = Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=94, y=400, anchor='nw')

        text_label = Label(frm_add, text="Nationality:", font=('Courier New', 18, 'bold'), bg=add_color, fg="#383838")
        text_label.place(x=300, y=400, anchor='ne')

        nationality_entry = Entry(frm_add,textvariable=self.var_nationality_entry, width=40, font=('Courier New', 16))
        nationality_entry.place(x=380, y=400)

        #crime
        asterisk_label = Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=42, y=460, anchor='nw')

        text_label = Label(frm_add, text="Crime Committed:", font=('Courier New', 18, 'bold'), bg=add_color, fg="#383838")
        text_label.place(x=300, y=460, anchor='ne')

        crime_entry = Text(frm_add, width=40, height=1, font=('Courier New', 16))
        crime_entry.place(x=380, y=460)


        #image display garna labels haru
        front_image_label = Label(frm_add, bg=add_color)
        front_image_label.place(x=240, y=505)

        left_image_label = Label(frm_add, bg=add_color)
        left_image_label.place(x=600, y=505)

        right_image_label = Label(frm_add, bg=add_color)
        right_image_label.place(x=950, y=505)

        # image selection 
        browse_btn1 = Button(frm_add, cursor="hand2", text="Select Front Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(front_image_label, self.front_file))
        browse_btn1.place(x=140, y=610)

        browse_btn2 = Button(frm_add, cursor="hand2", text="Select Left Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(left_image_label, self.left_file))
        browse_btn2.place(x=495, y=610)

        browse_btn3 = Button(frm_add, cursor="hand2", text="Select Right Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(right_image_label, self.right_file))
        browse_btn3.place(x=830, y=610)
            
        # Apply hover effect
        def on_enter(e):
            e.widget.config(bg="#ffc168")
            
        def on_leave(e):
            e.widget.config(bg="#ffb067")

        browse_btn1.configure(bg='#ffb067', fg='#383838')
        browse_btn1.bind("<Enter>", on_enter)
        browse_btn1.bind("<Leave>", on_leave)

        browse_btn2.configure(bg='#ffb067', fg='#383838')
        browse_btn2.bind("<Enter>", on_enter)
        browse_btn2.bind("<Leave>", on_leave)

        browse_btn3.configure(bg='#ffb067', fg='#383838')
        browse_btn3.bind("<Enter>", on_enter)
        browse_btn3.bind("<Leave>", on_leave)


        # Confirm Button
        confirm_btn = Button(frm_add, text="Confirm", font=('Courier New', 16, 'bold'), fg ="#383838", bg="#ffb067", command= submit)
        confirm_btn.place(x=570, y=685)

        # Configure button styling options
        confirm_btn.config(relief=RAISED, bd=3, width=14)

        confirm_btn.bind("<Enter>", on_enter)
        confirm_btn.bind("<Leave>", on_leave)

       
    def update_criminal(self):
        add_color = "#b2bedc"
        frm_add = Frame(self.root, width=1250, height=850, bg=add_color)
        frm_add.place(x=0, y=0)

        def add_image(label, image_variable):
            f_types = [('PNG files', '*.png'), ('JPEG files', '*.jpg;*.jpeg')]
            file_path = filedialog.askopenfilename(filetypes=f_types)
            
            if file_path:
                img = Image.open(file_path)
                img.thumbnail((200, 200))  # Resize the image for preview
                photo = ImageTk.PhotoImage(img)
                label.configure(image=photo)
                label.image = photo  # Store a reference to the image

                image_variable.set(file_path)

        front_file = StringVar()
        left_file = StringVar()
        right_file = StringVar()

        def submit_form():
            c_id = id_entry.get().strip()
            updated_name = name_entry.get().strip()
            updated_father_name = father_entry.get().strip()
            updated_mother_name = mother_entry.get().strip()
            updated_age = age_entry.get().strip()
            updated_nationality = nationality_entry.get().strip()
            updated_gender = gender_entry.get().strip()
            updated_crime = crime_entry.get("1.0", END).strip()

            if c_id == '':
                messagebox.showerror('Invalid', 'You must fill the ID of a criminal.')
                return
            
            try:
                c_id = int(c_id)
            except ValueError:
                messagebox.showerror('Invalid', 'ID is not valid.')
                return
            
            if updated_name == '' and updated_father_name == '' and updated_mother_name == '' and updated_age == '' and updated_nationality == '' and updated_gender == '' and updated_crime == '':
                messagebox.showinfo('Invalid', "No changes made.")
                return
            
            if updated_age != '':
                try:
                    updated_age = int(updated_age) 
                except ValueError:
                    messagebox.showerror("Error", "Age must be a valid number.")
                    return
                if updated_age < 14:
                    messagebox.showerror('Invalid', 'Age must be valid.')
                    return

            conn = mysql.connector.connect(
                host='localhost',
                database='mydb',
                port='3306',
                user='root',
                password=''
            )
            c = conn.cursor()

            fetch_id = "SELECT * FROM criminal_reg WHERE id=%s"
            values = (c_id,)
            c.execute(fetch_id, values)
            crim_data = c.fetchone()

            image_paths = [front_file.get(), left_file.get(), right_file.get()]
            updated_image_data = []

            for path in image_paths:
                if path:
                    with open(path, 'rb') as file:
                        updated_image_data.append(file.read())

            if crim_data:
                data_update = "UPDATE criminal_reg SET "
                update_vals = {}

                if updated_name:
                    update_vals['name'] = updated_name
                else:
                    update_vals['name'] = crim_data[1]

                if updated_father_name:
                    update_vals['father_name'] = updated_father_name
                else:
                    update_vals['father_name'] = crim_data[2]

                if updated_mother_name:
                    update_vals['mother_name'] = updated_mother_name
                else:
                    update_vals['mother_name'] = crim_data[3]

                if updated_age:
                    update_vals['age'] = updated_age
                else:
                    update_vals['age'] = crim_data[4]

                if updated_gender:
                    update_vals['gender'] = updated_gender
                else:
                    update_vals['gender'] = crim_data[5]

                if updated_nationality:
                    update_vals['nationality'] = updated_nationality
                else:
                    update_vals['nationality'] = crim_data[6]

                if updated_crime:
                    update_vals['crime'] = updated_crime
                else:
                    update_vals['crime'] = crim_data[7]

                if updated_image_data and updated_image_data[0]:
                    update_vals['front_img'] = updated_image_data[0]
                else:
                    update_vals['front_img'] = crim_data[8]

                if updated_image_data and updated_image_data[1]:
                    update_vals['left_img'] = updated_image_data[1]
                else:
                    update_vals['left_img'] = crim_data[9]

                if updated_image_data and updated_image_data[2]:
                    update_vals['right_img'] = updated_image_data[2]
                else:
                    update_vals['right_img'] = crim_data[10]

                data_update += ', '.join(f"{field} = %s" for field in update_vals.keys())
                data_update += " WHERE id = %s"

                try:
                    c.execute(data_update, tuple(update_vals.values()) + (c_id,))
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Success", f"Criminal with ID: {crim_data[0]} has been updated.")

                except mysql.connector.Error as error:
                    messagebox.showerror("Database Error", str(error))
                    return

                name_entry.delete(0, END)
                father_entry.delete(0, END)
                mother_entry.delete(0, END)
                age_entry.delete(0, END)
                gender_entry.delete(0, END)
                nationality_entry.delete(0, END)
                crime_entry.delete("1.0", END)
                front_image_label.configure(image=None)
                left_image_label.configure(image=None)
                right_image_label.configure(image=None)
                front_image_label.image = None  # Clear reference to front image
                left_image_label.image = None  # Clear reference to left image
                right_image_label.image = None  # Clear reference to right image
                front_file.set("")
                left_file.set("")
                right_file.set("")
                id_entry.delete(0, END)
            else:
                name_entry.delete(0, END)
                father_entry.delete(0, END)
                mother_entry.delete(0, END)
                age_entry.delete(0, END)
                gender_entry.delete(0, END)
                nationality_entry.delete(0, END)
                crime_entry.delete("1.0", END)
                front_image_label.configure(image=None)
                left_image_label.configure(image=None)
                right_image_label.configure(image=None)
                front_image_label.image = None  # Clear reference to front image
                left_image_label.image = None  # Clear reference to left image
                right_image_label.image = None  # Clear reference to right image
                front_file.set("")
                left_file.set("")
                right_file.set("")
                id_entry.delete(0, END)
                
                messagebox.showerror('Invalid', 'Invalid ID.')
                return


        ############  labels  #########33##########
        lbl_head = Label(frm_add, text='ID of criminal you want to update: ', bg=add_color, font=(main_font, 15))
        lbl_head.place(x=300, y=30, anchor='n')
        id_entry = Entry(frm_add, width=5, font=('Courier New', 15))
        id_entry.place(x=510, y=30)

        #name label
        text_label = Label(frm_add, text="Name:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
        text_label.place(x=260, y=100, anchor='ne')
        name_entry = Entry(frm_add, width=40, font=('Courier New', 16))
        name_entry.place(x=350, y=100)

        #father name
        father_label = Label(frm_add, fg='#383838', text="Father's Name:", font=('Courier New', 18, 'bold'), bg="#b2bedc")
        father_label.place(x=260, y=160, anchor='ne')
        father_entry = Entry(frm_add, width=40, font=('Courier New', 16))
        father_entry.place(x=350, y=160)

        #mother name
        mother_label = Label(frm_add, fg='#383838', text="Mother's Name:", font=('Courier New', 18, 'bold'), bg="#b2bedc")
        mother_label.place(x=260, y=220, anchor='ne')
        mother_entry = Entry(frm_add, width=40, font=('Courier New', 16))
        mother_entry.place(x=350, y=220)

        #age
        text_label = Label(frm_add, text="Age:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
        text_label.place(x=260, y=280, anchor='ne')
        age_entry = Entry(frm_add, width=40, font=('Courier New', 16))
        age_entry.place(x=350, y=280)

        #gender
        text_label = Label(frm_add, text="Gender:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
        text_label.place(x=260, y=340, anchor='ne')
        gender_entry = Entry(frm_add, width=40, font=('Courier New', 16))
        gender_entry.place(x=350, y=340)

        #nationality
        text_label = Label(frm_add, text="Nationality:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
        text_label.place(x=260, y=400, anchor='ne')
        nationality_entry = Entry(frm_add, width=40, font=('Courier New', 16))
        nationality_entry.place(x=350, y=400)

        #crime
        text_label = Label(frm_add, text="Crime Committed:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
        text_label.place(x=260, y=460, anchor='ne')
        crime_entry = Text(frm_add, width=40, height=1, font=('Courier New', 16))
        crime_entry.place(x=350, y=460)


        #image display garna labels haru
        front_image_label = Label(frm_add, bg=add_color)
        front_image_label.place(x=240, y=505)

        left_image_label = Label(frm_add, bg=add_color)
        left_image_label.place(x=600, y=505)

        right_image_label = Label(frm_add, bg=add_color)
        right_image_label.place(x=950, y=505)

        # image selection 
        browse_btn1 = Button(frm_add, cursor="hand2", text="Select Front Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(front_image_label, front_file))
        browse_btn1.place(x=140, y=610)

        browse_btn2 = Button(frm_add, cursor="hand2", text="Select Left Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(left_image_label, left_file))
        browse_btn2.place(x=495, y=610)

        browse_btn3 = Button(frm_add, cursor="hand2", text="Select Right Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(right_image_label, right_file))
        browse_btn3.place(x=830, y=610)
            
        # Apply hover effect
        def on_enter(e):
            e.widget.config(bg="#ffc168")
            
        def on_leave(e):
            e.widget.config(bg="#ffb067")

        browse_btn1.configure(bg='#ffb067', fg='#383838')
        browse_btn1.bind("<Enter>", on_enter)
        browse_btn1.bind("<Leave>", on_leave)

        browse_btn2.configure(bg='#ffb067', fg='#383838')
        browse_btn2.bind("<Enter>", on_enter)
        browse_btn2.bind("<Leave>", on_leave)

        browse_btn3.configure(bg='#ffb067', fg='#383838')
        browse_btn3.bind("<Enter>", on_enter)
        browse_btn3.bind("<Leave>", on_leave)


        # Confirm Button
        confirm_btn = Button(frm_add, text="Confirm", font=('Courier New', 16, 'bold'), fg ="#383838", bg="#ffb067", command=submit_form)
        confirm_btn.place(x=570, y=685)

        # Configure button styling options
        confirm_btn.config(relief=RAISED, bd=3, width=14)

        confirm_btn.bind("<Enter>", on_enter)
        confirm_btn.bind("<Leave>", on_leave)    



if __name__ == "__main__":
    root = Tk()
    main_window = AfterLogin(root)
    root.mainloop()





