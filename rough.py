
# from tkinter import *
# from tkinter import ttk

# import tkinter as tk

# root = tk.Tk()
# root.state("zoomed")
# frm = tk.Frame(root)
# frm.pack(side="left",fill="both", expand=True)

# canvas = tk.Canvas(frm)
# scroll_y = tk.Scrollbar(frm, orient="vertical", command=canvas.yview)

# frame = tk.Frame(canvas)
# # group of widgets
# for i in range(200):
#     tk.Label(frame, text='label %i' % i).pack()

# # put the frame in the canvas
# canvas.create_window(0, 0, anchor='nw', window=frame)
# # make sure everything is displayed before configuring the scrollregion
# canvas.update_idletasks()

# canvas.configure(scrollregion=canvas.bbox('all'), 
#                  yscrollcommand=scroll_y.set)
                 
# canvas.pack(fill='both', expand=True, side='left')
# scroll_y.pack(fill='y', side='right')

# root.mainloop()


from tkinter import *
from tkinter import ttk

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

        # Create a frame inside the canvas for the contents
        self.inner_frame = Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Create a background frame inside the inner frame
        self.background_frame = Frame(self.inner_frame, bg="blue")
        self.background_frame.pack(fill="both", expand=True)

        # Add your background elements here
        background_label = Label(self.background_frame, text="Background", bg="blue", fg="white")
        background_label.pack(pady=20)

        # Create example contents in the inner frame
        for i in range(20):
            label = Label(self.inner_frame, text=f"Item {i+1}", bg="white")
            label.pack(pady=10)

    def configure_scrollregion(self, event):
        # Configure the scrollable region to exclude the background frame
        content_bbox = self.inner_frame.bbox("all")
        self.canvas.configure(scrollregion=content_bbox)

# Create the main window
root = Tk()
root.title("Scrollable Frame with Fixed Background")
root.geometry("400x300")

# Create the scrolled frame
scrolled_frame = ScrolledFrame(root)
scrolled_frame.pack(fill="both", expand=True)

# Start the Tkinter event loop
root.mainloop()
