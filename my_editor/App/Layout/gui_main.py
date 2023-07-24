import customtkinter as tk
from gui_resources import Info, SetUpWindow, UI

app = tk.CTk()  # create CTk window
window_info = Info(app)  # window start info are fields in info
window_set_up = SetUpWindow(app, window_info)  # init the window
window_UI = UI(app, window_info)  # make the UI


app.mainloop()
