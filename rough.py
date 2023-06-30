import tkinter as tk

def exit_application():
    root.destroy()

# Create the main window
root = tk.Tk()

# Create a custom menubar frame
menubar_frame = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
menubar_frame.pack(side=tk.TOP, fill=tk.X)

# Create a custom menubar
menubar = tk.Menu(menubar_frame)

# Add File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_application)
menubar.add_cascade(label="File", menu=file_menu)

# Position the "File" menu at the right corner
menubar_frame.update_idletasks()
file_menu_width = file_menu.winfo_reqwidth()
menubar_frame.config(width=file_menu_width)
menubar_frame.pack_propagate(0)

# Set the menubar for the main window
root.config(menu=menubar)

# Run the Tkinter event loop
root.mainloop()
