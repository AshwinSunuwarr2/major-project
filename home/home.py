import tkinter as tk
from tkinter import messagebox, ttk, filedialog

from PIL import Image, ImageTk
import mysql.connector


home_font = "Courier new"
home_color = "green"
home = tk.Tk()
home.geometry('1250x850')
home.config(bg=home_color)
home.resizable(False, False)

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port='3306',
    database='mydb'
)
c = connection.cursor()


lbl_home = tk.Label(home, text="Some details about Our system goes here", font=(home_font, 24, 'italic'), bg=home_color)
lbl_home.place(x=100, y=100)


###################33 add criminals  ########3#############
def add():
    
    add_color = "#b2bedc"
    frm_add = tk.Frame(home, width=1250, height=1300, bg=add_color)
    frm_add.place(x=0, y=0)
    # frm_add.tk_setPalette(background='#F8E0DB')

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

    front_file = tk.StringVar()
    left_file = tk.StringVar()
    right_file = tk.StringVar()   

###########   submit form  ################################
    def submit_form():
        name = name_entry.get().strip()
        father_name = father_entry.get().strip()
        mother_name = mother_entry.get().strip()
        age = age_entry.get().strip()
        nationality = nationality_entry.get().strip()
        gender = gender_entry.get().strip()
        crime = crime_entry.get("1.0", tk.END).strip()

        if not name:
            messagebox.showerror("Error", "Please fill in the Name field.")
            return
        if not gender:
            messagebox.showerror("Error", "Please fill in the Gender field.")
            return
        if not age:
            messagebox.showerror("Error", "Please fill in the Age field.")
            return
        if not crime:
            messagebox.showerror("Error", "Please fill in the Crime Committed field.")
            return
        
        try:
            age = int(age) 
        except ValueError:
            messagebox.showerror("Error", "Age must be valid.")
            return
        if age <= 16:
            messagebox.showerror("Error", "Age must be above 16.")
            return

        image_paths = [front_file.get(), left_file.get(), right_file.get()]
        image_data = []

        # for path in image_paths:
        #     with open(path, 'rb') as file:
        #         image_data.append(file.read())
        
        for path in image_paths:
            if path:
                with open(path, 'rb') as file:
                    image_data.append(file.read())
            else:
                messagebox.showerror("Error", "Please select all three images.")
                return

        data_insert = "INSERT INTO `criminal_reg`(`name`, `father_name`, `mother_name`, `age`, `gender`, `nationality`, `crime`, `front_img`, `left_img`, `right_img`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        vals = (name, father_name, mother_name, age, gender, nationality, crime, image_data[0], image_data[1], image_data[2])
            
        try:
            c.execute(data_insert, vals)
            connection.commit()
            fetch_id = "select id from criminal_reg where name=%s and crime=%s"
            values  = (name, crime)
            c.execute(fetch_id, values)
            crim_id = c.fetchone()

            messagebox.showinfo("Success", f"Criminal with ID: {crim_id[0]} is now registered.")

        except mysql.connector.Error as error:
            messagebox.showerror("Database Error", str(error))

        name_entry.delete(0, tk.END)
        father_entry.delete(0, tk.END)
        mother_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_entry.delete(0, tk.END)
        nationality_entry.delete(0, tk.END)
        crime_entry.delete("1.0", tk.END)
        front_image_label.configure(image=None)  
        left_image_label.configure(image=None)      
        right_image_label.configure(image=None)
        front_image_label.image = None  # Clear reference to front image
        left_image_label.image = None  # Clear ref
        right_image_label.image = None  # Clear ref
        front_file.set("")
        left_file.set("")
        right_file.set("")




    ############  labels  #########33##########
    lbl_head = tk.Label(frm_add, text='Register Criminals', bg=add_color, font=(home_font, 28, 'bold'))
    lbl_head.place(x=380, y=30)

    #name label
    asterisk_label = tk.Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#b2bedc")
    asterisk_label.place(x=170, y=100, anchor='nw')

    text_label = tk.Label(frm_add, text="Name:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
    text_label.place(x=260, y=100, anchor='ne')

    name_entry = tk.Entry(frm_add, width=40, font=('Courier New', 16))
    name_entry.place(x=350, y=100)

    #father name
    father_label = tk.Label(frm_add, fg='#383838', text="Father's Name:", font=('Courier New', 18, 'bold'), bg="#b2bedc")
    father_label.place(x=260, y=160, anchor='ne')
    father_entry = tk.Entry(frm_add, width=40, font=('Courier New', 16))
    father_entry.place(x=350, y=160)

    #mother name
    mother_label = tk.Label(frm_add, fg='#383838', text="Mother's Name:", font=('Courier New', 18, 'bold'), bg="#b2bedc")
    mother_label.place(x=260, y=220, anchor='ne')
    mother_entry = tk.Entry(frm_add, width=40, font=('Courier New', 16))
    mother_entry.place(x=350, y=220)

    #age
    asterisk_label = tk.Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#b2bedc")
    asterisk_label.place(x=180, y=280, anchor='nw')

    text_label = tk.Label(frm_add, text="Age:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
    text_label.place(x=260, y=280, anchor='ne')

    age_entry = tk.Entry(frm_add, width=40, font=('Courier New', 16))
    age_entry.place(x=350, y=280)

    #gender
    asterisk_label = tk.Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#b2bedc")
    asterisk_label.place(x=138, y=340, anchor='nw')

    text_label = tk.Label(frm_add, text="Gender:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
    text_label.place(x=260, y=340, anchor='ne')

    gender_entry = tk.Entry(frm_add, width=40, font=('Courier New', 16))
    gender_entry.place(x=350, y=340)

    #nationality
    asterisk_label = tk.Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#b2bedc")
    asterisk_label.place(x=64, y=400, anchor='nw')

    text_label = tk.Label(frm_add, text="Nationality:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
    text_label.place(x=260, y=400, anchor='ne')

    nationality_entry = tk.Entry(frm_add, width=40, font=('Courier New', 16))
    nationality_entry.place(x=350, y=400)

    #crime
    asterisk_label = tk.Label(frm_add, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#b2bedc")
    asterisk_label.place(x=12, y=460, anchor='nw')

    text_label = tk.Label(frm_add, text="Crime Committed:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
    text_label.place(x=260, y=460, anchor='ne')

    crime_entry = tk.Text(frm_add, width=40, height=1, font=('Courier New', 16))
    crime_entry.place(x=350, y=460)


    #image display garna labels haru
    front_image_label = tk.Label(frm_add, bg=add_color)
    front_image_label.place(x=240, y=505)

    left_image_label = tk.Label(frm_add, bg=add_color)
    left_image_label.place(x=600, y=505)

    right_image_label = tk.Label(frm_add, bg=add_color)
    right_image_label.place(x=950, y=505)

    # image selection 
    browse_btn1 = tk.Button(frm_add, cursor="hand2", text="Select Front Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(front_image_label, front_file))
    browse_btn1.place(x=140, y=610)

    browse_btn2 = tk.Button(frm_add, cursor="hand2", text="Select Left Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(left_image_label, left_file))
    browse_btn2.place(x=495, y=610)

    browse_btn3 = tk.Button(frm_add, cursor="hand2", text="Select Right Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(right_image_label, right_file))
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
    confirm_btn = tk.Button(frm_add, text="Confirm", font=('Courier New', 16, 'bold'), fg ="#383838", bg="#ffb067", command=submit_form)
    confirm_btn.place(x=570, y=685)

    # Configure button styling options
    confirm_btn.config(relief=tk.RAISED, bd=3, width=14)

    confirm_btn.bind("<Enter>", on_enter)
    confirm_btn.bind("<Leave>", on_leave)



def update():
    add_color = "#b2bedc"
    frm_add = tk.Frame(home, width=1250, height=1300, bg=add_color)
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

    front_file = tk.StringVar()
    left_file = tk.StringVar()
    right_file = tk.StringVar()

    def submit_form():
        c_id = id_entry.get().strip()
        updated_name = name_entry.get().strip()
        updated_father_name = father_entry.get().strip()
        updated_mother_name = mother_entry.get().strip()
        updated_age = age_entry.get().strip()
        updated_nationality = nationality_entry.get().strip()
        updated_gender = gender_entry.get().strip()
        updated_crime = crime_entry.get("1.0", tk.END).strip()

        if c_id == '':
            messagebox.showerror('Invalid', 'You must fill the ID of a criminal.')
            return
        
        try:
            c_id = int(c_id)
        except ValueError:
            messagebox.showerror('Invalid', 'ID is not valid.')
            return
        
        if updated_age != '':
            try:
                updated_age = int(updated_age) 
            except ValueError:
                messagebox.showerror("Error", "Age must be a valid number.")
                return
            if updated_age < 14:
                messagebox.showerror('Invalid', 'Age must be valid.')

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
                connection.commit()

                messagebox.showinfo("Success", f"Criminal with ID: {crim_data[0]} has been updated.")

            except mysql.connector.Error as error:
                messagebox.showerror("Database Error", str(error))
                return

            name_entry.delete(0, tk.END)
            father_entry.delete(0, tk.END)
            mother_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
            gender_entry.delete(0, tk.END)
            nationality_entry.delete(0, tk.END)
            crime_entry.delete("1.0", tk.END)
            front_image_label.configure(image=None)
            left_image_label.configure(image=None)
            right_image_label.configure(image=None)
            front_image_label.image = None  # Clear reference to front image
            left_image_label.image = None  # Clear reference to left image
            right_image_label.image = None  # Clear reference to right image
            front_file.set("")
            left_file.set("")
            right_file.set("")
            id_entry.delete(0, tk.END)
        else:
            name_entry.delete(0, tk.END)
            father_entry.delete(0, tk.END)
            mother_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
            gender_entry.delete(0, tk.END)
            nationality_entry.delete(0, tk.END)
            crime_entry.delete("1.0", tk.END)
            front_image_label.configure(image=None)
            left_image_label.configure(image=None)
            right_image_label.configure(image=None)
            front_image_label.image = None  # Clear reference to front image
            left_image_label.image = None  # Clear reference to left image
            right_image_label.image = None  # Clear reference to right image
            front_file.set("")
            left_file.set("")
            right_file.set("")
            id_entry.delete(0, tk.END)
            
            messagebox.showerror('Invalid', 'Invalid ID.')
            return


    ############  labels  #########33##########
    lbl_head = tk.Label(frm_add, text='ID of criminal you want to update: ', bg=add_color, font=(home_font, 15))
    lbl_head.place(x=300, y=30, anchor='n')
    id_entry = tk.Entry(frm_add, width=5, font=('Courier New', 15))
    id_entry.place(x=510, y=30)

    #name label
    text_label = tk.Label(frm_add, text="Name:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
    text_label.place(x=260, y=100, anchor='ne')
    name_entry = tk.Entry(frm_add, width=40, font=('Courier New', 16))
    name_entry.place(x=350, y=100)

    #father name
    father_label = tk.Label(frm_add, fg='#383838', text="Father's Name:", font=('Courier New', 18, 'bold'), bg="#b2bedc")
    father_label.place(x=260, y=160, anchor='ne')
    father_entry = tk.Entry(frm_add, width=40, font=('Courier New', 16))
    father_entry.place(x=350, y=160)

    #mother name
    mother_label = tk.Label(frm_add, fg='#383838', text="Mother's Name:", font=('Courier New', 18, 'bold'), bg="#b2bedc")
    mother_label.place(x=260, y=220, anchor='ne')
    mother_entry = tk.Entry(frm_add, width=40, font=('Courier New', 16))
    mother_entry.place(x=350, y=220)

    #age
    text_label = tk.Label(frm_add, text="Age:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
    text_label.place(x=260, y=280, anchor='ne')
    age_entry = tk.Entry(frm_add, width=40, font=('Courier New', 16))
    age_entry.place(x=350, y=280)

    #gender
    text_label = tk.Label(frm_add, text="Gender:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
    text_label.place(x=260, y=340, anchor='ne')
    gender_entry = tk.Entry(frm_add, width=40, font=('Courier New', 16))
    gender_entry.place(x=350, y=340)

    #nationality
    text_label = tk.Label(frm_add, text="Nationality:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
    text_label.place(x=260, y=400, anchor='ne')
    nationality_entry = tk.Entry(frm_add, width=40, font=('Courier New', 16))
    nationality_entry.place(x=350, y=400)

    #crime
    text_label = tk.Label(frm_add, text="Crime Committed:", font=('Courier New', 18, 'bold'), bg="#b2bedc", fg="#383838")
    text_label.place(x=260, y=460, anchor='ne')
    crime_entry = tk.Text(frm_add, width=40, height=1, font=('Courier New', 16))
    crime_entry.place(x=350, y=460)


    #image display garna labels haru
    front_image_label = tk.Label(frm_add, bg=add_color)
    front_image_label.place(x=240, y=505)

    left_image_label = tk.Label(frm_add, bg=add_color)
    left_image_label.place(x=600, y=505)

    right_image_label = tk.Label(frm_add, bg=add_color)
    right_image_label.place(x=950, y=505)

    # image selection 
    browse_btn1 = tk.Button(frm_add, cursor="hand2", text="Select Front Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(front_image_label, front_file))
    browse_btn1.place(x=140, y=610)

    browse_btn2 = tk.Button(frm_add, cursor="hand2", text="Select Left Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(left_image_label, left_file))
    browse_btn2.place(x=495, y=610)

    browse_btn3 = tk.Button(frm_add, cursor="hand2", text="Select Right Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(right_image_label, right_file))
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
    confirm_btn = tk.Button(frm_add, text="Confirm", font=('Courier New', 16, 'bold'), fg ="#383838", bg="#ffb067", command=submit_form)
    confirm_btn.place(x=570, y=685)

    # Configure button styling options
    confirm_btn.config(relief=tk.RAISED, bd=3, width=14)

    confirm_btn.bind("<Enter>", on_enter)
    confirm_btn.bind("<Leave>", on_leave)    


##################3  help   #############################
def info():
    frm1 = tk.Frame(home, width = 1250, height = 850, bg="yellow")
    frm1.place(x=0, y=0)
    lbl_text = tk.Label(frm1, text="Canvas and frm_add are two different widgets in the Tkinter GUI toolkit in Python,\n and they have different purposes.",
                        font=(home_font, 18, 'bold'))
    lbl_text.place(x=30, y=60)


menu_bar = tk.Menu(home)
home.config(menu=menu_bar)

# Create File menu
home_menu = tk.Menu(menu_bar, tearoff=0)
home_menu.add_command(label="Add criminal details", command=add)
home_menu.add_command(label="Update criminal details", command=update)
home_menu.add_command(label="Delete criminal details")
home_menu.add_separator()
home_menu.add_command(label="Exit", command=home.quit)
menu_bar.add_cascade(label="Home", menu=home_menu)

# Create Edit menu
# edit_menu = tk.Menu(menu_bar, tearoff=0)
# edit_menu.add_command(label="Cut")
# edit_menu.add_command(label="Copy")
# edit_menu.add_command(label="Paste")

# Create Help menu
data_menu = tk.Menu(menu_bar, tearoff=0)
data_menu.add_command(label="View criminal details")
data_menu.add_command(label="View dataset")
data_menu.add_separator()
# data_menu.add_command(label="Exit", command=data_menu.quit)
menu_bar.add_cascade(label="Datasets", menu=data_menu)

cam_menu = tk.Menu(menu_bar, tearoff=0)
cam_menu.add_command(label="Recognize criminals")
menu_bar.add_cascade(label="Camera", menu=cam_menu)
menu_bar.add_cascade(label="Help", command=info)


home.mainloop()