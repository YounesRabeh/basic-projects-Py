import customtkinter as tk
from PIL import Image, ImageTk

tk.set_appearance_mode("dark")  # Modes: system (default), light, dark
tk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = tk.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x600")
app.title("18 Di Grid :)")

button_image = tk.CTkImage(Image.open("../Resources/GridPhoto.png"), size=(550, 550))

test_text = tk.CTkLabel(app, image=button_image, text="")

def button_function():
    test_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = tk.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

app.mainloop()




