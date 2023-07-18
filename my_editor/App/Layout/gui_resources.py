import customtkinter as tk

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
        _app.attributes('-zoomed', True)  # Set the window to full screen
        #_app.resizable(False, False)


class UI:
    def __init__(self, _app, _inf):
        # DRAW UI #
        self.files_frame = tk.CTkFrame(master=_app, fg_color="white",border_color="black",
                                       corner_radius=0, width=_inf.SCREEN_WIDTH//2, height=_inf.SCREEN_HEIGHT//1.86)
        self.files_frame.place(relx=0, rely=0)
        self.window_frame = tk.CTkFrame(master=_app, fg_color="yellow", border_color="black",
                                        corner_radius=0, width=_inf.SCREEN_WIDTH//2, height=_inf.SCREEN_HEIGHT//1.86)
        #self.window_frame.place(relx=0.5, rely=0)
        self.timeline_frame = tk.CTkFrame(master=_app, fg_color="blue", border_color="black",
                                          corner_radius=0, width=_inf.SCREEN_WIDTH, height=_inf.SCREEN_HEIGHT//2.24)
        self.timeline_frame.place(relx=0, rely=0.55)

        self.button = tk.CTkButton(master=_app, text="CTkButton", command=lambda: (self.button_function(_inf)))
        self.button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.my_text = tk.CTkLabel(master=self.files_frame, text=" ajSS ", fg_color='black', anchor=tk.CENTER)
        self.my_text.place(relx=0.5, rely=0.95)


    def button_function(self, _inf):
        self.my_text.configure(text="gggggggg")