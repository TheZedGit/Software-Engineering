import os
import random
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("800x600")
root.configure(bg="#1C1F25")

    image = ImageTk.PhotoImage(Image.open(image_path).resize((50, 50)))
    label = tk.Label(self, image=self.image, bg='white')
    label.pack(side='left')

self.button = tk.Button(self, text='▼', bg='white', bd=0, command=self.show_dropdown)
self.button.pack(side='left', padx=(5, 0))

self.dropdown_var = tk.StringVar(self)
self.dropdown = None


def search_images(self, query):
    # function to search for images in a file
    # returns a list of image file paths

    # implementation omitted for brevity
    pass


def set_image(self, image_path):
    self.image = ImageTk.PhotoImage(Image.open(image_path).resize((50, 50)))
    self.label.configure(image=self.image)


def show_dropdown(self):
    if self.dropdown is not None:
        # dropdown already exists, destroy it
        self.dropdown.destroy()

    # create new dropdown
    search_entry = tk.Entry(self, textvariable=self.dropdown_var)
    search_entry.pack(side='left', padx=(5, 0))

    search_button = tk.Button(self, text='Search', command=self.update_dropdown)
    search_button.pack(side='left', padx=(5, 0))


def update_dropdown(self):
    query = self.dropdown_var.get()
    image_paths = self.search_images(query)

    if self.dropdown is not None:
        self.dropdown.destroy()

    self.dropdown_var.set('')
    self.dropdown = tk.OptionMenu(self, self.dropdown_var, *image_paths, command=self.set_image)
    self.dropdown.pack(side='left', padx=(5, 0))


root = tk.Tk()
loc_label = (root, 'path/to/image.png')
loc_label.pack()
root.mainloop()
