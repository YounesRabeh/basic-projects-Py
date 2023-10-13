import pathlib
import os.path

# OS:
def get_file_path(file_name):
    current_dir = pathlib.Path(__file__).parent.resolve()
    DATA_file_abs_path = os.path.join(current_dir, file_name)
    return DATA_file_abs_path

def get_folder_path(folder_name):
    current_directory = os.path.abspath(os.getcwd())
    folder_path = os.path.join(current_directory, folder_name)
    # Check if the folder actually exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return folder_path
    else:
        raise FileNotFoundError(f"The folder '{folder_name}' does not exist in the project.")

