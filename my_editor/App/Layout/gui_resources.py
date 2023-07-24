import customtkinter as tk
from tkinter import Menu
from my_editor.App.Data.Font.fonts import *

class Info:
    #DEFAULT:
    SCREEN_WIDTH = 1020
    SCREEN_HEIGHT = 1080

    def __init__(self, _app):
        self.SCREEN_WIDTH = _app.winfo_screenwidth()
        self.SCREEN_HEIGHT = _app.winfo_screenheight()

class SetUpWindow:
    def __init__(self, _app, _inf):
        tk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        tk.set_default_color_theme("blue")
        size = f"{_inf.SCREEN_WIDTH//2}x{_inf.SCREEN_HEIGHT//2}"
        _app.geometry(size)
        _app.title("MY EDITOR")
        _app.minsize(_inf.SCREEN_WIDTH - 200, _inf.SCREEN_HEIGHT - 200)
        _app.attributes('-zoomed', True)  # Set the window to full screen
        # _app.resizable(False, False)
        # create a window_menubar
        window_menubar = Menu(_app, background="grey", border=0, relief="flat", tearoff=0)
        _app.config(menu=window_menubar)
        file_menu = Menu(window_menubar, border=0, relief="flat", tearoff=0)
        window_menubar.add_cascade(label="File          ", menu=file_menu)  # add the File menu to the window_menubar
        file_menu.add_command(label='Import',)
        file_menu.add_command(label='Exit', command=_app.destroy)  # add a menu item to the menu


class UI:
    def __init__(self, _app, _inf):
        # DRAW UI #
        #### TABS:
        self.tabview = tk.CTkTabview(_app, corner_radius=2,
                                     width=_inf.SCREEN_WIDTH//2.1, height=_inf.SCREEN_HEIGHT//1.86)
        self.tabview.place(relx=0.005, rely=0)
        video_tab_name = "\n             VIDEO             \n"
        image_tab_name = "\n             IMAGE             \n"
        audio_tab_name = "\n             AUDIO             \n"
        self.tabview.add(video_tab_name)
        self.tabview.add(image_tab_name)
        self.tabview.add(audio_tab_name)
        self.tabview.set(video_tab_name)
        self.file_canvas = tk.CTkCanvas(self.tabview.tab(video_tab_name), background="grey",
                                        width=_inf.SCREEN_WIDTH//2.011, height=_inf.SCREEN_HEIGHT//2.17)
        self.file_canvas.pack()
        self.file_canvas = tk.CTkCanvas(self.tabview.tab(image_tab_name), background="green",
                                        width=_inf.SCREEN_WIDTH // 2.011, height=_inf.SCREEN_HEIGHT // 2.17)
        self.file_canvas.pack()
        self.file_canvas = tk.CTkCanvas(self.tabview.tab(audio_tab_name), background="blue",
                                        width=_inf.SCREEN_WIDTH // 2.011, height=_inf.SCREEN_HEIGHT // 2.17)
        self.file_canvas.pack()





        self.window_frame = tk.CTkFrame(master=_app, fg_color="yellow", border_color="black",
                                        corner_radius=0, width=_inf.SCREEN_WIDTH//2, height=_inf.SCREEN_HEIGHT//1.86)
        #self.window_frame.place(relx=0.5, rely=0)
        self.timeline_frame = tk.CTkFrame(master=_app, fg_color="blue", border_color="black",
                                          corner_radius=0, width=_inf.SCREEN_WIDTH, height=_inf.SCREEN_HEIGHT//2.20)
        #self.timeline_frame.place(relx=0, rely=0.57)

        #self.button = tk.CTkButton(master=_app, text="CTkButton", command=lambda: (self.button_function(_inf)))
        #self.button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def button_function(self, _inf):
        pass
