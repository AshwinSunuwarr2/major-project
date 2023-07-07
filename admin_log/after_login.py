from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog, Canvas

from PIL import Image, ImageTk, ImageEnhance
import mysql.connector

import io

main_color = "#b2bedc"
#6f86b9
main_font = "Courier new"

class AfterLogin:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1250x750+70+0")
        root.state('zoomed')
        title_color = "#b2bedc"
        self.root.config(bg=title_color)
        self.root.title("Criminal Face Recognition System")
        self.root.resizable(False, False)

        frm_home = Frame(self.root)
        frm_home.pack(fill="both", expand=True)

        image_path = "bg_img/background.jpg"
        try:
            image = Image.open(image_path)
            enhancer = ImageEnhance.Brightness(image)
            dark_image = enhancer.enhance(0.1)  # control the darkness

            bg_image = ImageTk.PhotoImage(dark_image)

            bg_label = Label(frm_home, image=bg_image)
            bg_label.pack(fill="none", expand=False)
            bg_label.image = bg_image  # Keep a reference to avoid garbage collection

            frm_home.bind("<Configure>", self.on_frame_configure)

        except Exception as e:
            print(f"Error loading image: {e}")


        img = Image.open("bg_img/get_help.jpg")
        resized = img.resize((240,215), Image.LANCZOS)
        enhancer = ImageEnhance.Brightness(resized)
        dark_image = enhancer.enhance(0.45)
        self.btn_img = ImageTk.PhotoImage(dark_image)

        recognize_btn = Button(frm_home, image=self.btn_img, bg="orange", relief="groove", command=self.help)
        recognize_btn.place(x=900, y=290, width=240, height=220)

        recognize_btn1 = Button(frm_home, text="Get Help", bg="orange", relief="groove", font=("courier new", 14, "bold"), command=self.help)
        recognize_btn1.place(x=900, y=490, width=240, height=40)


#  -----------   getting started  ---------------#
        start_img = Image.open("bg_img/start.jpg")
        t_resized = start_img.resize((240,215), Image.LANCZOS)
        enhancer = ImageEnhance.Brightness(t_resized)
        dark_image = enhancer.enhance(0.45)
        self.btn_start_img = ImageTk.PhotoImage(dark_image)

        get_start_btn = Button(frm_home, image=self.btn_start_img, bg="orange", relief="groove", command=self.getting_started)
        get_start_btn.place(x=300, y=290, width=240, height=220)

        get_start_btn1 = Button(frm_home, text="Get Started", bg="orange", relief="groove", font=("courier new", 14, "bold"), command=self.getting_started)
        get_start_btn1.place(x=300, y=490, width=240, height=40)


#  -----------   About US  ---------------#
        about_img = Image.open("bg_img/recognize.jpg")
        t_resized = about_img.resize((240,215), Image.LANCZOS)
        enhancer = ImageEnhance.Brightness(t_resized)
        dark_image = enhancer.enhance(0.45)
        self.btn_about_img = ImageTk.PhotoImage(dark_image)

        about_us_btn = Button(frm_home, image=self.btn_about_img, bg="orange", relief="groove", command=self.aboutus)
        about_us_btn.place(x=600, y=290, width=240, height=220)

        about_us_btn1 = Button(frm_home, text="About Us", bg="orange", relief="groove", font=("courier new", 14, "bold"), command=self.aboutus)
        about_us_btn1.place(x=600, y=490, width=240, height=40)


    def on_frame_configure(self, event):
        target_width, target_height = event.width, event.height

        image_path = "bg_img/background.jpg"
        try:
            image = Image.open(image_path)
            resized_image = image.resize((target_width, target_height), Image.LANCZOS)
            enhancer = ImageEnhance.Brightness(resized_image)
            dark_image = enhancer.enhance(0.38)
            bg_image = ImageTk.PhotoImage(dark_image)

            bg_label = event.widget.winfo_children()[0]  # Get the label inside the frame
            bg_label.configure(image=bg_image)
            bg_label.image = bg_image  # Keep a reference to avoid garbage collection

        except Exception as e:
            print(f"Error loading or resizing image: {e}")

            

# -------------------   menu bars -----------------------------#

        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        # Create File menu
        home_menu = Menu(menu_bar, tearoff=0)
        home_menu.add_command(label="Home", command=self.view_criminal)
        home_menu.add_separator()
        home_menu.add_command(label="Register", command=lambda: (self.criminal_reg(), self.register_title()))
        home_menu.add_separator()
        home_menu.add_command(label="Update", command=lambda: (self.update_criminal(), self.update_title()))
        home_menu.add_separator()
        home_menu.add_command(label="View and Delete", command=lambda: (self.criminal_details(), self.view_del_title()))
        home_menu.add_separator()
        home_menu.add_command(label="Logout", command=self.logout)
        menu_bar.add_cascade(label="Criminal Details", menu=home_menu)


        data_menu = Menu(menu_bar, tearoff=0)
        data_menu.add_command(label="Trained Images", command=self.trained_image)
        data_menu.add_separator()
        data_menu.add_command(label="View Dataset", command=self.view_dataset)

        menu_bar.add_cascade(label="Datasets", menu=data_menu)

        cam_menu = Menu(menu_bar, tearoff=0)
        cam_menu.add_command(label="Recognize Criminals", command=self.recognize)
        menu_bar.add_cascade(label="Camera", menu=cam_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Get help", command=lambda: (self.help(), self.help_title()))
        help_menu.add_separator()
        help_menu.add_command(label="About us", command=lambda: (self.aboutus(), self.aboutus_title()))

        menu_bar.add_cascade(label="More", menu=help_menu)



#-------------   functions  --------------------=============================================================================================#
           
           
            #######   title updates ###########3
    def update_title(self):
        self.root.title("Update Criminal details")

    def register_title(self):
        self.root.title("Register New Criminals")
    
    def view_del_title(self):
        self.root.title("View and Delete Criminal Details")

    def help_title(self):
        self.root.title("Get Help")

    def aboutus_title(self):
        self.root.title("About Us")

    def update_title(self):
        self.root.title("Update Criminal Details")

    # ----------------------- home page ----------#
    def main_home(self):
        frm_home = Frame(self.root, bg="red")
        frm_home.place(x=0, y=0, relheight=1, relwidth=1)

        image_path = "bg_img/background.jpg"
        try:
            image = Image.open(image_path)
            enhancer = ImageEnhance.Brightness(image)
            dark_image = enhancer.enhance(0.1)  # Adjust the value (0.5 in this example) to control the darkness

            bg_image = ImageTk.PhotoImage(dark_image)

            bg_label = Label(frm_home, image=bg_image)
            bg_label.place(x=0, y=0, relheight=1, relwidth=1)
            bg_label.image = bg_image  # Keep a reference to avoid garbage collection

            frm_home.bind("<Configure>", self.on_frame_configure)

        except Exception as e:
            print(f"Error loading image: {e}")

        # ------------ get help ------#
        img = Image.open("bg_img/get_help.jpg")
        resized = img.resize((240,215), Image.LANCZOS)
        enhancer = ImageEnhance.Brightness(resized)
        dark_image = enhancer.enhance(0.45)
        self.btn_img = ImageTk.PhotoImage(dark_image)

        help_btn = Button(frm_home, image=self.btn_img, bg="orange", relief="groove", command=self.help)
        help_btn.place(x=900, y=290, width=240, height=220)

        help_btn1 = Button(frm_home, text="Get Help", bg="orange", relief="groove", font=("courier new", 14, "bold"), command=self.help)
        help_btn1.place(x=900, y=490, width=240, height=40)

#  -----------   getting started  ---------------#
        start_img = Image.open("bg_img/start.jpg")
        t_resized = start_img.resize((240,215), Image.LANCZOS)
        enhancer = ImageEnhance.Brightness(t_resized)
        dark_image = enhancer.enhance(0.45)
        self.btn_start_img = ImageTk.PhotoImage(dark_image)

        get_start_btn = Button(frm_home, image=self.btn_start_img, bg="orange", relief="groove", command=self.getting_started)
        get_start_btn.place(x=300, y=290, width=240, height=220)

        get_start_btn1 = Button(frm_home, text="Get Started", bg="orange", relief="groove", font=("courier new", 14, "bold"), command=self.getting_started)
        get_start_btn1.place(x=300, y=490, width=240, height=40)


#  -----------   About US  ---------------#
        about_img = Image.open("bg_img/recognize.jpg")
        t_resized = about_img.resize((240,215), Image.LANCZOS)
        enhancer = ImageEnhance.Brightness(t_resized)
        dark_image = enhancer.enhance(0.45)
        self.btn_about_img = ImageTk.PhotoImage(dark_image)

        about_us_btn = Button(frm_home, image=self.btn_about_img, bg="orange", relief="groove", command=self.aboutus)
        about_us_btn.place(x=600, y=290, width=240, height=220)

        about_us_btn1 = Button(frm_home, text="About Us", bg="orange", relief="groove", font=("courier new", 14, "bold"), command=self.aboutus)
        about_us_btn1.place(x=600, y=490, width=240, height=40)
        


    def logout(self):
        ans = messagebox.askyesno("Logout", "Are you sure you want to logout? ", parent=self.root)
        if ans == True:
            self.root.destroy()
            root.deiconify()
        else:
            return

    def help(self):
        frm1 =Frame(self.root, bg=main_color)
        frm1.place(x=0, y=0, relheight=1, relwidth=1)

        # ===============  frames for devs details  ==================#
        frm_ashwin = Frame(frm1, bg="white")
        frm_ashwin.place(x=950, y=200, height=350, width=350, anchor="nw")


    def aboutus(self):
        frm1 =Frame(self.root, bg=main_color)
        frm1.place(x=0, y=0, relheight=1, relwidth=1)


    def getting_started(self):
        frm1 =Frame(self.root, bg=main_color)
        frm1.place(x=0, y=0, relheight=1, relwidth=1)


    def criminal_reg(self):
        add_color = "#010203"
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
                    img.thumbnail((105, 95))  # Resize the image for preview
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
                messagebox.showerror("Error", "Please fill all required * fields.", parent=self.root)
                return 

            try:
                age = int(age) 
            except ValueError:
                messagebox.showerror("Error", "Age must be valid.", parent=self.root)
                return
            if age <= 16:
                messagebox.showerror("Error", "Age must be 16 or above.", parent=self.root)
                return

            image_paths = [self.front_file.get(), self.left_file.get(), self.right_file.get()]
            image_data = []

            for path in image_paths:
                if path:
                    with open(path, 'rb') as file:
                        image_data.append(file.read())
                else:
                    messagebox.showerror("Error", "Please select all three images.", parent=self.root)
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

                messagebox.showinfo("Success", f"Criminal with ID: {crim_id[0]} is now registered.", parent=self.root)

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


        frm_add = Frame(self.root, bg=add_color)
        frm_add.place(x=0, y=0, relheight=1, relwidth=1)

        # lbl_head = Label(frm_add, text='Register Criminals', bg=add_color, font=(add_font, 28, 'bold'))
        # lbl_head.place(x=380, y=30)

        inner_frm_add = Frame(frm_add, bg=add_color)
        inner_frm_add.place(x=135, y=0, relheight=1, relwidth=1)
        #name label
        asterisk_label = Label(inner_frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=200, y=100, anchor='nw')

        text_label = Label(inner_frm_add, text="Name:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
        text_label.place(x=300, y=100, anchor='ne')

        name_entry = Entry(inner_frm_add, textvariable=self.var_name_entry, width=40, font=('Courier New', 16))
        name_entry.place(x=380, y=100)

        #father name
        father_label = Label(inner_frm_add, fg='white', text="Father's Name:", font=('Courier New', 18, 'bold'), bg=add_color)
        father_label.place(x=300, y=160, anchor='ne')
        father_entry = Entry(inner_frm_add, textvariable=self.var_father_entry, width=40, font=('Courier New', 16))
        father_entry.place(x=380, y=160)

        #mother name
        mother_label = Label(inner_frm_add, fg='white', text="Mother's Name:", font=('Courier New', 18, 'bold'), bg=add_color)
        mother_label.place(x=300, y=220, anchor='ne')
        mother_entry = Entry(inner_frm_add, textvariable=self.var_mother_entry, width=40, font=('Courier New', 16))
        mother_entry.place(x=380, y=220)

        #age
        asterisk_label = Label(inner_frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=210, y=280, anchor='nw')

        text_label = Label(inner_frm_add, text="Age:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
        text_label.place(x=300, y=280, anchor='ne')

        age_entry = Entry(inner_frm_add, textvariable=self.var_age_entry, width=40, font=('Courier New', 16))
        age_entry.place(x=380, y=280)

        #gender
        asterisk_label = Label(inner_frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=168, y=340, anchor='nw')

        text_label = Label(inner_frm_add, text="Gender:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
        text_label.place(x=300, y=340, anchor='ne')

        gender_entry = Entry(inner_frm_add, textvariable=self.var_gender_entry, width=40, font=('Courier New', 16))
        gender_entry.place(x=380, y=340)

        #nationality
        asterisk_label = Label(inner_frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=94, y=400, anchor='nw')

        text_label = Label(inner_frm_add, text="Nationality:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
        text_label.place(x=300, y=400, anchor='ne')

        nationality_entry = Entry(inner_frm_add,textvariable=self.var_nationality_entry, width=40, font=('Courier New', 16))
        nationality_entry.place(x=380, y=400)

        #crime
        asterisk_label = Label(inner_frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg=add_color)
        asterisk_label.place(x=42, y=460, anchor='nw')

        text_label = Label(inner_frm_add, text="Crime Committed:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
        text_label.place(x=300, y=460, anchor='ne')

        crime_entry = Text(inner_frm_add, width=40, height=1, font=('Courier New', 16))
        crime_entry.place(x=380, y=460)


        #image display garna labels haru
        front_image_label = Label(inner_frm_add, bg=add_color, height=95, width=105)
        front_image_label.place(x=240, y=505)

        left_image_label = Label(inner_frm_add, bg=add_color, height=95, width=105)
        left_image_label.place(x=600, y=505)

        right_image_label = Label(inner_frm_add, bg=add_color, height=95, width=105)
        right_image_label.place(x=950, y=505)

        # image selection 
        browse_btn1 = Button(inner_frm_add, cursor="hand2", text="Select Front Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(front_image_label, self.front_file))
        browse_btn1.place(x=140, y=610)

        browse_btn2 = Button(inner_frm_add, cursor="hand2", text="Select Left Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(left_image_label, self.left_file))
        browse_btn2.place(x=495, y=610)

        browse_btn3 = Button(inner_frm_add, cursor="hand2", text="Select Right Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(right_image_label, self.right_file))
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
        confirm_btn = Button(inner_frm_add, text="Confirm", font=('Courier New', 16, 'bold'), fg ="#383838", bg="#ffb067", command= submit)
        confirm_btn.place(x=570, y=685)

        # Configure button styling options
        confirm_btn.config(relief=RAISED, bd=3, width=14)

        confirm_btn.bind("<Enter>", on_enter)
        confirm_btn.bind("<Leave>", on_leave)

    
    def view_crim(self, criminal_id):
            # c_id = id_entry.get().strip()

            # if c_id == '':
            #     messagebox.showerror('Invalid', 'You must fill the ID of a criminal.', parent=self.root)
            #     return
            
            # try:
            #     c_id = int(c_id)
            # except ValueError:
            #     messagebox.showerror('Invalid', 'ID is not valid.', parent=self.root)
            #     return
            
            # fetch_id = "SELECT id FROM criminal_reg WHERE id=%s"
            # values = (c_id,)
            # c.execute(fetch_id, values)
            # crim_data = c.fetchone()

            # if not crim_data:
            #     messagebox.showerror("Invalid", "ID no found.")
            #     id_entry.delete(0, END)
            #     return
            add_color = "#010203"
            frm_add = Frame(self.root, bg=add_color)
            frm_add.place(x=0, y=0, relheight=1, relwidth=1)

            inner_frm_add = Frame(frm_add, bg=add_color)
            inner_frm_add.place(x=135, y=0, relheight=1, relwidth=1)

            def add_image(label, image_variable):
                f_types = [('PNG files', '*.png'), ('JPEG files', '*.jpg;*.jpeg')]
                file_path = filedialog.askopenfilename(filetypes=f_types)
                
                if file_path:
                    img = Image.open(file_path)
                    img.thumbnail((105, 100))  # Resize the image for preview
                    photo = ImageTk.PhotoImage(img)
                    label.configure(image=photo)
                    label.image = photo  # Store a reference to the image

                    image_variable.set(file_path)

            front_file = StringVar()
            left_file = StringVar()
            right_file = StringVar()


            def submit_form():
                updated_name = name_entry.get().strip()
                updated_father_name = father_entry.get().strip()
                updated_mother_name = mother_entry.get().strip()
                updated_age = age_entry.get().strip()
                updated_nationality = nationality_entry.get().strip()
                updated_gender = gender_entry.get().strip()
                updated_crime = crime_entry.get("1.0", END).strip()

                
                if updated_age != '':
                    try:
                        updated_age = int(updated_age) 
                    except ValueError:
                        messagebox.showerror("Error", "Age must be a valid number.", parent=self.root)
                        return
                    if updated_age < 14:
                        messagebox.showerror('Invalid', 'Age must be valid.', parent=self.root)
                        return

                fetch_id = "SELECT * FROM criminal_reg WHERE id=%s"
                values = (criminal_id,)
                c.execute(fetch_id, values)
                crim_data = c.fetchone()

                # image_paths = [front_file.get(), left_file.get(), right_file.get()]
                f_path = front_file.get()
                l_path = left_file.get()
                r_path = right_file.get()

                updated_front_data = []
                updated_left_data = []
                updated_right_data = []

                if f_path:
                    with open(f_path, 'rb') as file:
                        updated_front_data.append(file.read())
                if l_path:
                    with open(l_path, 'rb') as file:
                        updated_left_data.append(file.read())
                if r_path:
                    with open(r_path, 'rb') as file:
                        updated_right_data.append(file.read())

                if crim_data:
                    # if updated_name == '' or updated_father_name == '' or updated_mother_name == '' or updated_age == '' or updated_nationality == '' or updated_gender == '' or updated_crime == '' or updated_image_data == '':
                    #     messagebox.showinfo('Invalid', "No changes made.", parent=self.root)
                    #     return
                    
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


                    if len(updated_front_data) > 0 and updated_front_data[0]:
                        front_image_label.image = updated_front_data[0]  # Update the front_image_label
                        update_vals['front_img'] = updated_front_data[0]
                    elif crim_data[8]:
                        update_vals['front_img'] = crim_data[8]  # Keep the same front image if available

                    # Update the left image if provided in updated_image_data
                    if len(updated_left_data) > 0 and updated_left_data[0]:
                        left_image_label.image = updated_left_data[0]  # Update the left_image_label
                        update_vals['left_img'] = updated_left_data[0]
                    elif crim_data[9]:
                        update_vals['left_img'] = crim_data[9]  # Keep the same left image if available

                    # Update the right image if provided in updated_image_data
                    if len(updated_right_data) > 0 and updated_right_data[0]:
                        right_image_label.image = updated_right_data[0]  # Update the right_image_label
                        update_vals['right_img'] = updated_right_data[0]
                    elif crim_data[10]:
                        update_vals['right_img'] = crim_data[10] # Keep the same right image if available
                        


                    data_update += ', '.join(f"{field} = %s" for field in update_vals.keys())
                    data_update += " WHERE id = %s"

                    try:
                        ask = messagebox.askyesno("Confirm", "Are you sure you want to update this?")
                        if ask == True:
                            c.execute(data_update, tuple(update_vals.values()) + (criminal_id,))
                            conn.commit()
                            conn.close()
                            messagebox.showinfo("Success", f"Criminal with ID: {crim_data[0]} has been updated.", parent=self.root)

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
                        else:
                            return
                        
                    except mysql.connector.Error as error:
                        messagebox.showerror("Database Error", str(error), parent=self.root)
                        return
                
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
                    
                    messagebox.showerror('Invalid', 'Invalid ID.', parent=self.root)            
                    return


            conn = mysql.connector.connect(
                host='localhost',
                database='mydb',
                port='3306',
                user='root',
                password=''
            )
            c = conn.cursor()


            lbl_head = Label(inner_frm_add, text="ID:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
            lbl_head.place(x=300, y=50, anchor='ne')
            id_entry = Entry(inner_frm_add, width=7, font=('Courier New', 20), bd=3)
            id_entry.insert(0, criminal_id)
            id_entry.place(x=600, y=35, anchor='n')

            back_btn = Button(inner_frm_add, text="Back", font=('Courier New', 14), width=6, cursor="hand2", fg ="black", bg="violet", command=self.view_criminal)
            back_btn.place(x=980, y=35)

                #name label
            text_label = Label(inner_frm_add, text="Name:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
            text_label.place(x=300, y=100, anchor='ne')
            name_entry = Entry(inner_frm_add, width=40, font=('Courier New', 16))
            name_entry.place(x=380, y=100)

                #father name
            father_label = Label(inner_frm_add, fg='white', text="Father's Name:", font=('Courier New', 18, 'bold'), bg=add_color)
            father_label.place(x=300, y=160, anchor='ne')
            father_entry = Entry(inner_frm_add, width=40, font=('Courier New', 16))
            father_entry.place(x=380, y=160)

                #mother name
            mother_label = Label(inner_frm_add, fg='white', text="Mother's Name:", font=('Courier New', 18, 'bold'), bg=add_color)
            mother_label.place(x=300, y=220, anchor='ne')
            mother_entry = Entry(inner_frm_add, width=40, font=('Courier New', 16))
            mother_entry.place(x=380, y=220)

                #age
            text_label = Label(inner_frm_add, text="Age:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
            text_label.place(x=300, y=280, anchor='ne')
            age_entry = Entry(inner_frm_add, width=40, font=('Courier New', 16))
            age_entry.place(x=380, y=280)

                #gender
            text_label = Label(inner_frm_add, text="Gender:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
            text_label.place(x=300, y=340, anchor='ne')
            gender_entry = Entry(inner_frm_add, width=40, font=('Courier New', 16))
            gender_entry.place(x=380, y=340)

                #nationality
            text_label = Label(inner_frm_add, text="Nationality:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
            text_label.place(x=300, y=400, anchor='ne')
            nationality_entry = Entry(inner_frm_add, width=40, font=('Courier New', 16))
            nationality_entry.place(x=380, y=400)

                #crime
            text_label = Label(inner_frm_add, text="Crime Committed:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
            text_label.place(x=300, y=460, anchor='ne')
            crime_entry = Text(inner_frm_add, width=40, height=1, font=('Courier New', 16))
            crime_entry.place(x=380, y=460)


                #image display garna labels haru
            front_image_label = Label(inner_frm_add, bg=add_color, height=95, width=105)
            front_image_label.place(x=240, y=505)

            left_image_label = Label(inner_frm_add, bg=add_color, height=95, width=105)
            left_image_label.place(x=600, y=505)

            right_image_label = Label(inner_frm_add, bg=add_color, height=95, width=105)
            right_image_label.place(x=950, y=505)

            # name_entry.delete(0, END)
            # father_entry.delete(0, END)
            # mother_entry.delete(0, END)
            # age_entry.delete(0, END)
            # gender_entry.delete(0, END)
            # nationality_entry.delete(0, END)
            # crime_entry.delete("1.0", END)
            # front_image_label.image = None  
            # left_image_label.image = None  
            # right_image_label.image = None 

            query = "select name, father_name, mother_name, age, gender, nationality, crime, front_img, left_img, right_img from criminal_reg where id=%s"
            vals = (criminal_id,)
            c.execute(query, vals)
            result= c.fetchall()

            # if result:
            name_entry.insert(0, result[0][0])
            father_entry.insert(0, result[0][1])
            mother_entry.insert(0, result[0][2])
            age_entry.insert(0, result[0][3])
            gender_entry.insert(0, result[0][4])
            nationality_entry.insert(0, result[0][5])
            crime_entry.insert("1.0", result[0][6])

            front_data = result[0][7]
            left_data = result[0][8]
            right_data = result[0][9]

            f_img = Image.open(io.BytesIO(front_data))
            f_img.thumbnail((105,95))
            f_photo = ImageTk.PhotoImage(f_img)
            front_image_label.configure(image=f_photo)
            front_image_label.image = f_photo

            l_img = Image.open(io.BytesIO(left_data))
            l_img.thumbnail((105,95))
            l_photo = ImageTk.PhotoImage(l_img)
            left_image_label.configure(image=l_photo)
            left_image_label.image = l_photo

            r_img = Image.open(io.BytesIO(right_data))
            r_img.thumbnail((105,95))
            r_photo = ImageTk.PhotoImage(r_img)
            right_image_label.configure(image=r_photo)
            right_image_label.image = r_photo


            # image selection 
            browse_btn1 = Button(inner_frm_add, cursor="hand2", text="Select Front Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(front_image_label, front_file))
            browse_btn1.place(x=140, y=610)

            browse_btn2 = Button(inner_frm_add, cursor="hand2", text="Select Left Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(left_image_label, left_file))
            browse_btn2.place(x=495, y=610)

            browse_btn3 = Button(inner_frm_add, cursor="hand2", text="Select Right Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(right_image_label, right_file))
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
            confirm_btn = Button(inner_frm_add, text="Confirm", font=('Courier New', 16, 'bold'), fg ="#383838", bg="#ffb067", command=lambda: (submit_form(), self.view_criminal()))
            confirm_btn.place(x=570, y=685)

            # Configure button styling options
            confirm_btn.config(relief=RAISED, bd=3, width=14)

            confirm_btn.bind("<Enter>", on_enter)
            confirm_btn.bind("<Leave>", on_leave) 

            # def goto_view():
            #     self.root.destroy()
            #     self.view_criminal.deiconify()


    def update_criminal(self, criminal_id):
        add_color = "#010203"
        frm_add = Frame(self.root, bg=add_color)
        frm_add.place(x=0, y=0, relheight=1, relwidth=1)

        inner_frm_add = Frame(frm_add, bg=add_color)
        inner_frm_add.place(x=135, y=0, relheight=1, relwidth=1)

        conn = mysql.connector.connect(
                host='localhost',
                database='mydb',
                port='3306',
                user='root',
                password=''
            )
        c = conn.cursor()
                
        # self.view_crim()

        def add_image(label, image_variable):
            f_types = [('PNG files', '*.png'), ('JPEG files', '*.jpg;*.jpeg')]
            file_path = filedialog.askopenfilename(filetypes=f_types)
            
            if file_path:
                img = Image.open(file_path)
                img.thumbnail((105, 100))  # Resize the image for preview
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
                messagebox.showerror('Invalid', 'You must fill the ID of a criminal.', parent=self.root)
                return
            
            try:
                c_id = int(c_id)
            except ValueError:
                messagebox.showerror('Invalid', 'ID is not valid.', parent=self.root)
                return
            
            if updated_age != '':
                try:
                    updated_age = int(updated_age) 
                except ValueError:
                    messagebox.showerror("Error", "Age must be a valid number.", parent=self.root)
                    return
                if updated_age < 14:
                    messagebox.showerror('Invalid', 'Age must be valid.', parent=self.root)
                    return

            fetch_id = "SELECT * FROM criminal_reg WHERE id=%s"
            values = (c_id,)
            c.execute(fetch_id, values)
            crim_data = c.fetchone()

            # image_paths = [front_file.get(), left_file.get(), right_file.get()]
            f_path = front_file.get()
            l_path = left_file.get()
            r_path = right_file.get()

            updated_front_data = []
            updated_left_data = []
            updated_right_data = []

            if f_path:
                with open(f_path, 'rb') as file:
                    updated_front_data.append(file.read())
            if l_path:
                with open(l_path, 'rb') as file:
                    updated_left_data.append(file.read())
            if r_path:
                with open(r_path, 'rb') as file:
                    updated_right_data.append(file.read())

            if crim_data:
                # if updated_name == '' or updated_father_name == '' or updated_mother_name == '' or updated_age == '' or updated_nationality == '' or updated_gender == '' or updated_crime == '' or updated_image_data == '':
                #     messagebox.showinfo('Invalid', "No changes made.", parent=self.root)
                #     return
                
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


                if len(updated_front_data) > 0 and updated_front_data[0]:
                    front_image_label.image = updated_front_data[0]  # Update the front_image_label
                    update_vals['front_img'] = updated_front_data[0]
                elif crim_data[8]:
                    update_vals['front_img'] = crim_data[8]  # Keep the same front image if available

                # Update the left image if provided in updated_image_data
                if len(updated_left_data) > 0 and updated_left_data[0]:
                    left_image_label.image = updated_left_data[0]  # Update the left_image_label
                    update_vals['left_img'] = updated_left_data[0]
                elif crim_data[9]:
                    update_vals['left_img'] = crim_data[9]  # Keep the same left image if available

                # Update the right image if provided in updated_image_data
                if len(updated_right_data) > 0 and updated_right_data[0]:
                    right_image_label.image = updated_right_data[0]  # Update the right_image_label
                    update_vals['right_img'] = updated_right_data[0]
                elif crim_data[10]:
                    update_vals['right_img'] = crim_data[10] # Keep the same right image if available
                    


                data_update += ', '.join(f"{field} = %s" for field in update_vals.keys())
                data_update += " WHERE id = %s"

                try:
                    c.execute(data_update, tuple(update_vals.values()) + (c_id,))
                    conn.commit()

                    messagebox.showinfo("Success", f"Criminal with ID: {crim_data[0]} has been updated.", parent=self.root)

                except mysql.connector.Error as error:
                    messagebox.showerror("Database Error", str(error), parent=self.root)
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
                
                messagebox.showerror('Invalid', 'Invalid ID.', parent=self.root)            
                return


        ############  labels  #########33##########
        # lbl_heading = Label(inner_frm_add, text="Update Criminal Details", font=('Courier new', 20, 'bold'), bg="#b2bedc")
        # lbl_heading.place(x=500, y=10)

        lbl_head = Label(inner_frm_add, text="ID:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
        lbl_head.place(x=300, y=50, anchor='ne')
        id_entry = Entry(inner_frm_add, width=7, font=('Courier New', 20), bd=3)
        id_entry.insert(0, criminal_id)
        id_entry.place(x=600, y=35, anchor='n')

        view_id_btn = Button(inner_frm_add, text="View ID", font=('Courier New', 16, 'bold'), fg ="#383838", bg="#ffb067")
        view_id_btn.place(x=700, y=35)

        #name label
        text_label = Label(inner_frm_add, text="Name:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
        text_label.place(x=300, y=100, anchor='ne')
        name_entry = Entry(inner_frm_add, width=40, font=('Courier New', 16))
        name_entry.place(x=380, y=100)

        #father name
        father_label = Label(inner_frm_add, fg='white', text="Father's Name:", font=('Courier New', 18, 'bold'), bg=add_color)
        father_label.place(x=300, y=160, anchor='ne')
        father_entry = Entry(inner_frm_add, width=40, font=('Courier New', 16))
        father_entry.place(x=380, y=160)

        #mother name
        mother_label = Label(inner_frm_add, fg='white', text="Mother's Name:", font=('Courier New', 18, 'bold'), bg=add_color)
        mother_label.place(x=300, y=220, anchor='ne')
        mother_entry = Entry(inner_frm_add, width=40, font=('Courier New', 16))
        mother_entry.place(x=380, y=220)

        #age
        text_label = Label(inner_frm_add, text="Age:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
        text_label.place(x=300, y=280, anchor='ne')
        age_entry = Entry(inner_frm_add, width=40, font=('Courier New', 16))
        age_entry.place(x=380, y=280)

        #gender
        text_label = Label(inner_frm_add, text="Gender:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
        text_label.place(x=300, y=340, anchor='ne')
        gender_entry = Entry(inner_frm_add, width=40, font=('Courier New', 16))
        gender_entry.place(x=380, y=340)

        #nationality
        text_label = Label(inner_frm_add, text="Nationality:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
        text_label.place(x=300, y=400, anchor='ne')
        nationality_entry = Entry(inner_frm_add, width=40, font=('Courier New', 16))
        nationality_entry.place(x=380, y=400)

        #crime
        text_label = Label(inner_frm_add, text="Crime Committed:", font=('Courier New', 18, 'bold'), bg=add_color, fg="white")
        text_label.place(x=300, y=460, anchor='ne')
        crime_entry = Text(inner_frm_add, width=40, height=1, font=('Courier New', 16))
        crime_entry.place(x=380, y=460)


        #image display garna labels haru
        front_image_label = Label(inner_frm_add, bg=add_color, height=95, width=105)
        front_image_label.place(x=240, y=505)

        left_image_label = Label(inner_frm_add, bg=add_color, height=95, width=105)
        left_image_label.place(x=600, y=505)

        right_image_label = Label(inner_frm_add, bg=add_color, height=95, width=105)
        right_image_label.place(x=950, y=505)

        # image selection 
        browse_btn1 = Button(inner_frm_add, cursor="hand2", text="Select Front Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(front_image_label, front_file))
        browse_btn1.place(x=140, y=610)

        browse_btn2 = Button(inner_frm_add, cursor="hand2", text="Select Left Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(left_image_label, left_file))
        browse_btn2.place(x=495, y=610)

        browse_btn3 = Button(inner_frm_add, cursor="hand2", text="Select Right Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(right_image_label, right_file))
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
        confirm_btn = Button(inner_frm_add, text="Confirm", font=('Courier New', 16, 'bold'), fg ="#383838", bg="#ffb067", command=submit_form)
        confirm_btn.place(x=570, y=685)

        # Configure button styling options
        confirm_btn.config(relief=RAISED, bd=3, width=14)

        confirm_btn.bind("<Enter>", on_enter)
        confirm_btn.bind("<Leave>", on_leave)    


    def criminal_details(self):
        del_color = "#b2bedc"
        del_font = 'courier new'

        # ------------------- delete criminal ----------------#
        def delete_confirm():
            c_id = entry_id.get().strip()

            if c_id == "":
                messagebox.showerror('Invalid', 'Please enter ID of criminal to delete.', parent=self.root)
                return
            try:
                c_id = int(c_id)
            except ValueError:
                messagebox.showerror('Invalid', "Invalid ID.", parent=self.root)
                return
            
            conn = mysql.connector.connect(
                host = 'localhost',
                database = 'mydb',
                port = '3306',
                user = 'root',
                password  = ''
            )
            c = conn.cursor()

            fetch_id = "select * from criminal_reg where id = %s"
            values = (c_id,)
            c.execute(fetch_id, values)
            crim_data = c.fetchone()

            if crim_data:
                crim_delete = "delete from criminal_reg where id=%s"
                vals = (c_id,)

                try:
                    result = messagebox.askyesno("Warning", f"Are you sure you want to delete {crim_data[0]} id criminal?", parent=self.root)
                    if result == True:
                        c.execute(crim_delete, vals)
                        conn.commit()
                        conn.close()

                        messagebox.showinfo("Success", f"Criminal with ID: {crim_data[0]} has been deleted.", parent=self.root)
                        lbl_right.image = None
                        lbl_left.image = None
                        lbl_front.image = None
                    else:
                        return

                except mysql.connector.Error as error:
                    messagebox.showerror("Database Error", str(error), parent=self.root)
                    return
            else:
                messagebox.showerror('Invalid', 'ID not found.', parent=self.root)
                return
            
            entry_id.delete(0, END)

        
        # ------------------- view one criminal -----------------#
        def view_details():
            c_id = entry_id.get().strip()

            if c_id == "":
                messagebox.showerror('Invalid', 'Please enter ID of criminal to view.', parent=self.root)
                return
            try:
                c_id = int(c_id)
            except ValueError:
                messagebox.showerror('Invalid', "Invalid ID.", parent=self.root)
                return

            conn = mysql.connector.connect(
                host='localhost',
                database='mydb',
                port='3306',
                user='root',
                password=''
            )
            c = conn.cursor()

            fetch_id = "select * from criminal_reg where id = %s"
            values = (c_id,)
            c.execute(fetch_id, values)
            crim_data = c.fetchall()

            if len(crim_data) != 0:
                self.criminal_tbl.delete(*self.criminal_tbl.get_children())  # Clear existing data in the treeview
                for row in crim_data:
                    self.criminal_tbl.insert("", 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], ))
                conn.commit()
            else:
                messagebox.showerror('Invalid', 'ID not found.', parent=self.root)
                return

            conn.close()

            # entry_id.delete(0, END)


        # --------------- view all criminals  --------------------#
        def viewall_details():
            lbl_right.image = None
            lbl_left.image = None
            lbl_front.image = None
            entry_id.delete(0, END)

            conn = mysql.connector.connect(
                host='localhost',
                database='mydb',
                port='3306',
                user='root',
                password=''
            )
            c = conn.cursor()

            fetch_id = "select * from criminal_reg"
            c.execute(fetch_id)
            crim_data = c.fetchall()

            if len(crim_data) != 0:
                self.criminal_tbl.delete(*self.criminal_tbl.get_children())  # Clear existing data in the treeview
                for row in crim_data:
                    self.criminal_tbl.insert("", 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                conn.commit()
            else:
                messagebox.showerror('Invalid', 'Empty database', parent=self.root)
                return

            conn.close()

        # ------------------- view criminal image -------------- #
        def crim_img():
            c_id = entry_id.get().strip()

            lbl_right.image = None
            lbl_left.image = None
            lbl_front.image = None

            conn = mysql.connector.connect(
                host='localhost',
                database='mydb',
                port='3306',
                user='root',
                password=''
            )
            c = conn.cursor()

            query = "select front_img, left_img, right_img from criminal_reg where id=%s"
            vals = (c_id,)
            c.execute(query, vals)
            img= c.fetchall()
            print("image fetching")

            if img:
                front_data = img[0][0]
                left_data = img[0][1]
                right_data = img[0][2]

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


        frm_detail = Frame(self.root, bg=del_color)
        frm_detail.place(x=0, y=0, relheight=1, relwidth=1)

        frm_inner_detail = Frame(frm_detail, bg=del_color)
        frm_inner_detail.place(x=127, y=0, relheight=1, relwidth=1)


        lbl_text = Label(frm_inner_detail, text="Enter criminal ID: ", bg=del_color, font=(del_font, 16))
        lbl_text.place(x=70, y=60)

        entry_id = Entry(frm_inner_detail, bg="white", width=7,  font=(del_font, 20), bd=5)  
        entry_id.place(x=320, y=52)

        btn_viewall = Button(frm_inner_detail, width=9, text="VIEW ALL", bg='orange', fg="black", font=(del_font, 16), cursor="hand2", relief="ridge", command=viewall_details)
        btn_viewall.place(x=600, y=52)

        btn_view = Button(frm_inner_detail, width=9, text="VIEW", bg='orange', fg="black", font=(del_font, 16), cursor="hand2", relief="ridge", command=lambda: (view_details(), crim_img()))
        btn_view.place(x=730, y=52)

        btn_del = Button(frm_inner_detail, width=9, text="DELETE", bg='red', fg="white", font=(del_font, 16, 'bold'), cursor="hand2", relief="sunken", command=delete_confirm)
        btn_del.place(x=1120, y=52)
    
        frm_view = LabelFrame(frm_inner_detail, text= "Criminal details", font=('courier new', 12), width=1185, height=490, bg=del_color)
        frm_view.place(x=65, y=95)
        table_frm = Frame(frm_view, bg="black", bd=1)
        table_frm.place(x=5, y=5, width=1170, height=460)


# --------- img for single criminals -----------#
        lbl_front = Label(frm_inner_detail, bg=main_color)
        lbl_front.place(x=200, y=650)
        lbl_left = Label(frm_inner_detail, bg=main_color)
        lbl_left.place(x=600, y=650)
        lbl_right = Label(frm_inner_detail, bg=main_color)
        lbl_right.place(x=1000, y=650)

        scroll_x = ttk.Scrollbar(table_frm, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frm, orient=VERTICAL)
        
        self.criminal_tbl = ttk.Treeview(table_frm, column=("id", "name", "father_name", "mother_name", "age", "gender", "nationality", "crime"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.criminal_tbl.xview)
        scroll_y.config(command=self.criminal_tbl.yview)


        self.criminal_tbl.heading("id", text="ID")
        self.criminal_tbl.heading("name", text="Name")
        self.criminal_tbl.heading("father_name", text="Father's Name")
        self.criminal_tbl.heading("mother_name", text="Mother's Name")
        self.criminal_tbl.heading("age", text="Age")
        self.criminal_tbl.heading("gender", text="Gender")
        self.criminal_tbl.heading("nationality", text="Nation")
        self.criminal_tbl.heading("crime", text="Crime Committed")
        self.criminal_tbl["show"] = "headings"

        
        self.criminal_tbl.column("id", width=60)
        self.criminal_tbl.column("name", width=180)
        self.criminal_tbl.column("father_name", width=180)
        self.criminal_tbl.column("mother_name", width=180)
        self.criminal_tbl.column("age", width=60)
        self.criminal_tbl.column("gender", width=100)
        self.criminal_tbl.column("nationality", width=140)
        self.criminal_tbl.column("crime", width=300)

        self.criminal_tbl.pack(fill=BOTH, expand=1)

    def view_criminal(self):
        frm_top = Frame(self.root, bg="#141414")
        frm_top.place(x=0, y=2, relwidth=1, height=50)

        lbl_head = Label(frm_top, text="Criminal Details", font=("Arial", 20, "bold"), fg="white", bg="#141414")
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
        main_frame.config(bg="#292929")
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

            btn_del = Button(frm_item, width=9, text="EDIT", bg='#e4d00a', fg="black", font=(main_font, 14), cursor="hand2", relief="sunken", command=lambda criminal_id=row[0]: (self.update_criminal(criminal_id), self.view_crim(criminal_id)))
            btn_del.place(x=740, y=230)
            btn_del = Button(frm_item, width=9, text="DELETE", bg='#e44c5c', fg="black", font=(main_font, 14), cursor="hand2", relief="sunken")
            btn_del.place(x=740, y=280)

        # put the frame to be scrolled in the canvas  ---------- group of widgets need use of canvas 
        canvas.create_window(0, 0, anchor='nw', window=main_frame)
        # everything displayed confirmation
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), 
                        yscrollcommand=scroll_y.set)
                        
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')

    def trained_image(self):
        frm1 =Frame(self.root, bg=main_color)
        frm1.place(x=0, y=0, relheight=1, relwidth=1)

        frm_inner = Frame(frm1, bg=main_color)
        frm_inner.place(x=135, y=0, relheight=1, relwidth=1)
        lbl_text = Label(frm_inner, bg=main_color, text="Trained Images frame here.",
                                font=(main_font, 18))
        lbl_text.place(x=30, y=60)


    def view_dataset(self):
        frm1 =Frame(self.root, bg=main_color)
        frm1.place(x=0, y=0, relheight=1, relwidth=1)

        frm_inner = Frame(frm1, bg=main_color)
        frm_inner.place(x=135, y=0, relheight=1, relwidth=1)
        lbl_text = Label(frm_inner, bg=main_color, text="Dataset labels frame here.",
                                font=(main_font, 18))
        lbl_text.place(x=30, y=60)

    def recognize(self):
        frm1 =Frame(self.root, bg=main_color)
        frm1.place(x=0, y=0, relheight=1, relwidth=1)

        frm_inner = Frame(frm1, bg=main_color)
        frm_inner.place(x=135, y=0, relheight=1, relwidth=1)
        lbl_text = Label(frm_inner, bg=main_color, text="openCV camera face detection here.",
                                font=(main_font, 18))
        lbl_text.place(x=30, y=60)


        


if __name__ == "__main__":
    root = Tk()
    main_window = AfterLogin(root)
    root.mainloop()