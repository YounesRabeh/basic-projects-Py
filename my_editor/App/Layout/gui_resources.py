import customtkinter

class Info:
    #DEFAULT:
    SCREEN_WIDTH = 1020
    SCREEN_HEIGHT = 1080

    def __init__(self, _app):
        self.SCREEN_WIDTH = _app.winfo_screenwidth()
        self.SCREEN_HEIGHT = _app.winfo_screenheight()

class SetUpWindow:
    def __init__(self, _app):
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")
        _app.geometry("1300x900")
        _app.attributes("-zoomed", True)

class UI:
    def __init__(self, _app, _inf):
        button = customtkinter.CTkButton(master=_app, text="CTkButton", command=lambda: (self.button_function(_inf)))
        button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    def button_function(self, _inf):
        print(_inf.SCREEN_WIDTH)