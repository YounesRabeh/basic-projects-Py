from Flag_guesser.App.Layout.gui import *
from App.manager.file_location import *
import time

DATA_DIRECTORY = get_folder_path("data")
FLAGS_DIRECTORY = get_folder_path_in_dir("_flagsIMG_", DATA_DIRECTORY)

flags_ls = get_all_files_in_dir(FLAGS_DIRECTORY)

app = tk.CTk()
set_up = SetUp(app)
ui = UI(flags_ls)
i = 0
ui.update_ui()

app.mainloop()




