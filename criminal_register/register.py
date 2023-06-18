
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
import os
import mysql.connector

MAX_RESOLUTION = 1080


root = tk.Tk()
root['bg']='#237de1'
root.geometry("1080x650")
root.title("Register Criminal")

connection = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='mydb')
c= connection.cursor()

# def browse_image():
#     file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
#     if file_path:
#         image = Image.open(file_path)
#         width, height = image.size
#         if width <= MAX_RESOLUTION and height <= MAX_RESOLUTION:
#             confirm_btn.file_path = file_path
#             messagebox.showinfo("Success", "Image uploaded successfully.")
#         else:
#             messagebox.showerror("Error", f"Please select an image with a resolution of {MAX_RESOLUTION}x{MAX_RESOLUTION} pixels or smaller.")

# def save_image():
#     if hasattr(confirm_btn, 'file_path') and confirm_btn.file_path:
#         file_path = confirm_btn.file_path
#         image = Image.open(file_path)
#         os.makedirs("images", exist_ok=True)
#         file_name = os.path.basename(file_path)
#         destination_path = os.path.join("images", file_name)
#         image.save(destination_path)
#         messagebox.showinfo(f"Registration success.")
#     else:
#         messagebox.showerror("Error", "Please upload an image before saving.")

def submit_form():
    name = name_entry.get().strip()
    father_name = father_entry.get()
    mother_name = mother_entry.get()
    age = age_entry.get()
    nationality = nationality_entry.get()
    gender = gender_entry.get().strip()
    crime = crime_entry.get("1.0", tk.END).strip()

    if name == "":
        messagebox.showerror("Error", "Please fill in the Name field.")
    elif gender == "":
        messagebox.showerror("Error", "Please fill in the Gender field.")
    elif crime == "":
        messagebox.showerror("Error", "Please fill in the Crime Committed field.")
    else:
        # Perform further actions here, e.g., save the name to a database
        data_insert = "INSERT INTO `criminal_reg`(`name`, `father_name`, `mother_name`, `age`, `gender`, `nationality`, `crime`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        vals = (name, father_name, mother_name, age, gender, nationality, crime)
        c.execute(data_insert, vals)
        connection.commit()

        # save_image()

        messagebox.showinfo("Success", f"Criminal with name: {name} has been registered.")

frame = tk.Frame(root, bg="#237de1")
frame.pack(pady=20)

# name_label = tk.Label(frame, fg='orange', text="*Name:", font=('Courier New', 18, 'bold'), bg="#237de1")
# name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
# name_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
# name_entry.grid(row=0, column=1, padx=10, pady=10)

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

crime_entry = tk.Text(frame, width=32, height=4, font=('Courier New', 16))
crime_entry.grid(row=6, column=1, padx=10, pady=10)

# browse_btn = tk.Button(root, text="Upload Image", font=('Courier New', 16), command=browse_image)
# browse_btn.pack(pady=20)

#confirm button 
confirm_btn = tk.Button(root, text="Confirm", font=('Courier New', 16, 'bold'), command=submit_form, bg="#feac57")
confirm_btn.pack(pady=10)


root.mainloop()

