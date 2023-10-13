import customtkinter as tk
import tkinter as tkN

tk.set_appearance_mode("dark")  # Modes: system (default), light, dark
tk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

APP = None


class SetUp:
    def __init__(self, _app):
        global APP

        APP = _app


        APP.geometry("1000x700")
        APP.title("FLAG GUESSER")
        APP.config()





class UI:
    flag_image_canvas = None
    flag_image = None
    flag_ls = []
    index = 0
    bg_color = ""

    def __init__(self, flags_ls):
        self.bg_color = APP.cget("background")
        self.flags_ls = flags_ls
        self.flag_image_canvas = tkN.Canvas(APP, width=640, height=426)
        self.flag_image_canvas.config(borderwidth=0, bg=self.bg_color,
                                      highlightthickness=0, highlightbackground=self.bg_color)
        self.flag_image_canvas.place(x=150, y=100)
        self.update_canvas()


    def update_canvas(self):
        self.flag_image = tkN.PhotoImage(file=self.flags_ls[self.index])
        print(self.flags_ls[self.index])
        self.flag_image_canvas.create_image(320, 200, image=self.flag_image)


    def set_index(self, new_index):
        self.index = new_index


    def update_ui(self):
        APP.after(500, self.update_ui)
        self.set_index(self.index + 1)
        self.update_canvas()
