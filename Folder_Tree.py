import tkinter as tk
from tkinter import filedialog
import os

def pick_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_file = "tree.txt"
        with open(output_file, "w") as f:
            f.write("****** " + folder_path + " ******\n")
            list_files_and_folders(folder_path, f)

def list_files_and_folders(folder_path, output_file, indent=""):
    root_folder_name = os.path.basename(folder_path)
    output_file.write(indent + root_folder_name + "/\n")
    indent += "   "
    for root_folder, sub_folders, files in os.walk(folder_path):
        for sub_folder in sorted(sub_folders):
            list_files_and_folders(os.path.join(root_folder, sub_folder), output_file, indent)
        for file in sorted(files):
            output_file.write(indent + file + "\n")

if __name__ == "__main__":
    pick_folder()
