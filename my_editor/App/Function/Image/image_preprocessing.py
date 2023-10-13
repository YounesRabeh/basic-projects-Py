from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        img = resize_image(file_path, 1400, 400)
        canvas.image = img
        canvas.create_image(0, 0, anchor=tk.NW, image=img)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Resizer")

    canvas = tk.Canvas(root, width=1500, height=900)
    canvas.pack()

    open_button = tk.Button(root, text="Open Image", command=open_image)
    open_button.pack()

    root.mainloop()