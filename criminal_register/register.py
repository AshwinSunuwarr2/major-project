
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import mysql.connector
import base64


MAX_RESOLUTION = 1080


root = tk.Tk()
root['bg']='#237de1'
root.geometry("1080x750")
root.title("Register Criminal")

connection = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='mydb')
c= connection.cursor()


def add_front():
    global front_file, img
    
    f_types = [('png files', '*.png'), ('jpg files', '*.jpg'), ('jpeg files', '*.jpeg')]
    front_file = tk.StringVar()
    front_file.set(filedialog.askopenfilename(filetypes=f_types))
    
    if front_file.get():
        img = Image.open(front_file.get())
        img.thumbnail((200, 200))  # Resize the image for preview
        
        # Create a PhotoImage object for the image
        img = ImageTk.PhotoImage(img)
        
        # Configure the image_label with the selected image
        front_image_label.configure(image=img)
        front_image_label.image = img  # Store a reference to the image

def add_left():
    global left_file, img
    
    f_types = [('png files', '*.png'), ('jpg files', '*.jpg'), ('jpeg files', '*.jpeg')]
    left_file = tk.StringVar()
    left_file.set(filedialog.askopenfilename(filetypes=f_types))
    
    if left_file.get():
        img = Image.open(left_file.get())
        img.thumbnail((200, 200))  # Resize the image for preview
        
        # Create a PhotoImage object for the image
        img = ImageTk.PhotoImage(img)
        
        # Configure the image_label with the selected image
        left_image_label.configure(image=img)
        left_image_label.image = img  # Store a reference to the image

def add_right():
    global right_file, img
    
    f_types = [('png files', '*.png'), ('jpg files', '*.jpg'), ('jpeg files', '*.jpeg')]
    right_file = tk.StringVar()
    right_file.set(filedialog.askopenfilename(filetypes=f_types))
    
    if right_file.get():
        img = Image.open(right_file.get())
        img.thumbnail((200, 200))  # Resize the image for preview
        
        # Create a PhotoImage object for the image
        img = ImageTk.PhotoImage(img)
        
        # Configure the image_label with the selected image
        right_image_label.configure(image=img)
        right_image_label.image = img  # Store a reference to the image


# will be submitted to db
def submit_form():
    global front_file, img

    #file from add_front
    name = name_entry.get().strip()
    father_name = father_entry.get()
    mother_name = mother_entry.get()
    age = age_entry.get()
    nationality = nationality_entry.get()
    gender = gender_entry.get().strip()
    crime = crime_entry.get("1.0", tk.END).strip()
    image_data = open(front_file.get(), 'rb')
    image_data = image_data.read()

    left_data = open(left_file.get(), 'rb')
    left_data = left_data.read()

    right_data = open(right_file.get(), 'rb')
    right_data = right_data.read()


    
    if name == "":
        messagebox.showerror("Error", "Please fill in the Name field.")
    elif gender == "":
        messagebox.showerror("Error", "Please fill in the Gender field.")
    elif crime == "":
        messagebox.showerror("Error", "Please fill in the Crime Committed field.")
    else:        
        # save the details to a database
        data_insert = "INSERT INTO `criminal_reg`(`name`, `father_name`, `mother_name`, `age`, `gender`, `nationality`, `crime`, `front_img`, `left_img`, `right_img`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        vals = (name, father_name, mother_name, age, gender, nationality, crime, image_data, left_data, right_data)
        c.execute(data_insert, vals)
        connection.commit()
        
        # clears fields
        name_entry.delete(0, tk.END)
        father_entry.delete(0, tk.END)
        mother_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_entry.delete(0, tk.END)
        nationality_entry.delete(0, tk.END)
        crime_entry.delete("1.0", tk.END)
        image_data = None
        right_data = None
        left_data = None
        
        messagebox.showinfo("Success", f"Criminal with name: {name} has been registered.")


frame = tk.Frame(root, bg="#237de1")
frame.pack(pady=20, expand=True, anchor='center')


#name label
name_label = tk.Label(frame, bg="#237de1")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

asterisk_label = tk.Label(name_label, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#237de1")
asterisk_label.grid(row=0, column=0)

text_label = tk.Label(name_label, text="Name:", font=('Courier New', 18, 'bold'), bg="#237de1", fg="orange")
text_label.grid(row=0, column=1)

name_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
name_entry.grid(row=0, column=1, padx=10, pady=10)

#father name
father_label = tk.Label(frame, fg='orange', text="Father's Name:", font=('Courier New', 18, 'bold'), bg="#237de1")
father_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
father_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
father_entry.grid(row=1, column=1, padx=10, pady=10)

#mother name
mother_label = tk.Label(frame, fg='orange', text="Mother's Name:", font=('Courier New', 18, 'bold'), bg="#237de1")
mother_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
mother_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
mother_entry.grid(row=2, column=1, padx=10, pady=10)

#age
age_label = tk.Label(frame, fg='orange', text="Age:", font=('Courier New', 18, 'bold'), bg="#237de1")
age_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
age_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
age_entry.grid(row=3, column=1, padx=10, pady=10)

#gender
gender_label = tk.Label(frame, bg="#237de1")
gender_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")

asterisk_label = tk.Label(gender_label, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#237de1")
asterisk_label.grid(row=0, column=0)

text_label = tk.Label(gender_label, text="Gender:", font=('Courier New', 18, 'bold'), bg="#237de1", fg="orange")
text_label.grid(row=0, column=1)

gender_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
gender_entry.grid(row=4, column=1, padx=10, pady=10)

#nationality
nationality_label = tk.Label(frame, bg="#237de1")
nationality_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")

asterisk_label = tk.Label(nationality_label, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#237de1")
asterisk_label.grid(row=0, column=0)

text_label = tk.Label(nationality_label, text="Nationality:", font=('Courier New', 18, 'bold'), bg="#237de1", fg="orange")
text_label.grid(row=0, column=1)

nationality_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
nationality_entry.grid(row=5, column=1, padx=10, pady=10)

#crime
crime_label = tk.Label(frame, bg="#237de1")
crime_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")

asterisk_label = tk.Label(crime_label, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#237de1")
asterisk_label.grid(row=0, column=0)

text_label = tk.Label(crime_label, text="Crime Committed:", font=('Courier New', 18, 'bold'), bg="#237de1", fg="orange")
text_label.grid(row=0, column=1)

crime_entry = tk.Text(frame, width=32, height=1, font=('Courier New', 16))
crime_entry.grid(row=6, column=1, padx=10, pady=10)




#front_image btn
browse_btn = tk.Button(frame, text="Select Front Face Image", font=('Courier New', 13), command=lambda:add_front())
browse_btn.grid(row=7, column=0, padx=4, pady=4)

front_image_label = tk.Label(frame)
front_image_label.grid(row=9, column=0)

# left image btn
browse_btn = tk.Button(frame, text="Select Left Face Image", font=('Courier New', 13), command=lambda:add_left())
browse_btn.grid(row=7, column=1, padx=4, pady=4)

left_image_label = tk.Label(frame)
left_image_label.grid(row=9, column=1)


#right image btn
browse_btn = tk.Button(frame, text="Select Right Face Image", font=('Courier New', 13), command=lambda:add_right())
browse_btn.grid(row=7, column=2, padx=4, pady=4)

right_image_label = tk.Label(frame)
right_image_label.grid(row=9, column=2)

#confirm button 
confirm_btn = tk.Button(root, text="Confirm", font=('Courier New', 16, 'bold'), command=submit_form, bg="#feac57")
confirm_btn.pack(pady=10)


root.mainloop()
