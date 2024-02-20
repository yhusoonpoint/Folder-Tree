import tkinter as tk
from tkinter import filedialog
import os

def pick_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("****** " + folder_path + " ******")
        list_files_and_folders(folder_path)

def list_files_and_folders(folder_path, indent=""):
    root_folder_name = os.path.basename(folder_path)
    print(indent + root_folder_name + "/")
    indent += "   "
    for root_folder, sub_folders, files in os.walk(folder_path):
        for sub_folder in sorted(sub_folders):
            list_files_and_folders(os.path.join(root_folder, sub_folder), indent)
        for file in sorted(files):
            print(indent + file)

if __name__ == "__main__":
    pick_folder()
