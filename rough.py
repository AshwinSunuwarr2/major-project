import tkinter as tk
from tkinter import messagebox, Menu, ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector


MAX_RESOLUTION = 1080

root = tk.Tk()
root.title("Register Criminal")
root.geometry("1100x750")
root.configure(bg="#237de1")
root.tk_setPalette(background='#F8E0DB')

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port='3306',
    database='mydb'
)
c = connection.cursor()

def add_image(label):
    f_types = [('PNG files', '*.png'), ('JPEG files', '*.jpg;*.jpeg')]
    file_path = filedialog.askopenfilename(filetypes=f_types)
    
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((200, 200))  # Resize the image for preview
        photo = ImageTk.PhotoImage(img)
        label.configure(image=photo)
        label.image = photo  # Store a reference to the image


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
    if not crime:
        messagebox.showerror("Error", "Please fill in the Crime Committed field.")
        return
    
    image_paths = [front_file.get(), left_file.get(), right_file.get()]
    image_data = []
    for path in image_paths:
        with open(path, 'rb') as file:
            image_data.append(file.read())
    
    data_insert = "INSERT INTO `criminal_reg`(`name`, `father_name`, `mother_name`, `age`, `gender`, `nationality`, `crime`, `front_img`, `left_img`, `right_img`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    vals = (name, father_name, mother_name, age, gender, nationality, crime, image_data[0], image_data[1], image_data[2])
    c.execute(data_insert, vals)
    connection.commit()
    
    name_entry.delete(0, tk.END)
    father_entry.delete(0, tk.END)
    mother_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    nationality_entry.delete(0, tk.END)
    crime_entry.delete("1.0", tk.END)
    
    messagebox.showinfo("Success", f"Criminal with name: {name} has been registered.")


frame = tk.Frame(root, bg="#237de1")
frame.pack(pady=20)

#name label
name_label = tk.Label(frame, bg="#237de1")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

asterisk_label = tk.Label(name_label, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#237de1")
asterisk_label.grid(row=0, column=0)

text_label = tk.Label(name_label, text="Name:", font=('Courier New', 18, 'bold'), bg="#237de1", fg="#383838")
text_label.grid(row=0, column=1)

name_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
name_entry.grid(row=0, column=1, padx=10, pady=10)

#father name
father_label = tk.Label(frame, fg='#383838', text="Father's Name:", font=('Courier New', 18, 'bold'), bg="#237de1")
father_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
father_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
father_entry.grid(row=1, column=1, padx=10, pady=10)

#mother name
mother_label = tk.Label(frame, fg='#383838', text="Mother's Name:", font=('Courier New', 18, 'bold'), bg="#237de1")
mother_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
mother_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
mother_entry.grid(row=2, column=1, padx=10, pady=10)

#age
age_label = tk.Label(frame, fg='#383838', text="Age:", font=('Courier New', 18, 'bold'), bg="#237de1")
age_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
age_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
age_entry.grid(row=3, column=1, padx=10, pady=10)

#gender
gender_label = tk.Label(frame, bg="#237de1")
gender_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")

asterisk_label = tk.Label(gender_label, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#237de1")
asterisk_label.grid(row=0, column=0)

text_label = tk.Label(gender_label, text="Gender:", font=('Courier New', 18, 'bold'), bg="#237de1", fg="#383838")
text_label.grid(row=0, column=1)

gender_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
gender_entry.grid(row=4, column=1, padx=10, pady=10)

#nationality
nationality_label = tk.Label(frame, bg="#237de1")
nationality_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")

asterisk_label = tk.Label(nationality_label, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#237de1")
asterisk_label.grid(row=0, column=0)

text_label = tk.Label(nationality_label, text="Nationality:", font=('Courier New', 18, 'bold'), bg="#237de1", fg="#383838")
text_label.grid(row=0, column=1)

nationality_entry = tk.Entry(frame, width=32, font=('Courier New', 16))
nationality_entry.grid(row=5, column=1, padx=10, pady=10)

#crime
crime_label = tk.Label(frame, bg="#237de1")
crime_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")

asterisk_label = tk.Label(crime_label, text="*", font=('Courier New', 18, 'bold'), fg='red', bg="#237de1")
asterisk_label.grid(row=0, column=0)

text_label = tk.Label(crime_label, text="Crime Committed:", font=('Courier New', 18, 'bold'), bg="#237de1", fg="#383838")
text_label.grid(row=0, column=1)

crime_entry = tk.Text(frame, width=32, height=1, font=('Courier New', 16))
crime_entry.grid(row=6, column=1, padx=10, pady=10)

# Image Buttons and Labels
front_file = tk.StringVar()
left_file = tk.StringVar()
right_file = tk.StringVar()

front_image_label = tk.Label(frame, bg="#237de1")
front_image_label.grid(row=7, column=0, padx=10, pady=10)

left_image_label = tk.Label(frame, bg="#237de1")
left_image_label.grid(row=7, column=1, padx=10, pady=10)

right_image_label = tk.Label(frame, bg="#237de1")
right_image_label.grid(row=7, column=2, padx=10, pady=10)

browse_btn1 = tk.Button(frame, text="Select Front Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(front_image_label))
browse_btn1.grid(row=8, column=0, padx=4, pady=4)


browse_btn2 = tk.Button(frame, text="Select Left Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(left_image_label))
browse_btn2.grid(row=8, column=1, padx=4, pady=4)

browse_btn3 = tk.Button(frame, text="Select Right Face Image", font=('Courier New', 16, 'bold'), command=lambda: add_image(right_image_label))
browse_btn3.grid(row=8, column=2, padx=4, pady=4)

# Apply hover effect
def on_enter(e):
    e.widget.config(bg="#ffc168")
    
def on_leave(e):
    e.widget.config(bg="#feac57")

browse_btn1.configure(bg='#feac57', fg='#383838')
browse_btn1.bind("<Enter>", on_enter)
browse_btn1.bind("<Leave>", on_leave)

browse_btn2.configure(bg='#feac57', fg='#383838')
browse_btn2.bind("<Enter>", on_enter)
browse_btn2.bind("<Leave>", on_leave)

browse_btn3.configure(bg='#feac57', fg='#383838')
browse_btn3.bind("<Enter>", on_enter)
browse_btn3.bind("<Leave>", on_leave)


# Confirm Button
confirm_btn = tk.Button(root, text="Confirm", font=('Courier New', 16, 'bold'), fg ="#383838", command=submit_form, bg="#feac57")
confirm_btn.pack(pady=35)

# Configure button styling options
confirm_btn.config(relief=tk.RAISED, bd=3, width=14, height=2)

confirm_btn.bind("<Enter>", on_enter)
confirm_btn.bind("<Leave>", on_leave)


root.update_idletasks()  # Update the window to calculate its size
root_width = root.winfo_width()
root_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (root_width // 2)
y = (screen_height // 2) - (root_height // 2)
root.geometry(f"{root_width}x{root_height}+{x}+{y}")  # Center the window on the screen

root.mainloop()
