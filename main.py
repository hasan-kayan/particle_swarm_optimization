from csv_operations import * 
from data_visualization import * 

import tkinter as tk
from tkinter import filedialog
import os
import shutil

def create_project_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    project_folder_path = filedialog.askdirectory(
        title="Select Project Folder Location"
    )

    if project_folder_path:
        project_folder_name = input("Enter project folder name: ")
        project_folder_path = os.path.join(project_folder_path, project_folder_name)

        try:
            os.makedirs(project_folder_path)
            print("Project folder created successfully:", project_folder_path)
        except OSError as e:
            print("Failed to create project folder:", e)

        return project_folder_path
    else:
        print("No project folder selected.")
        return None

def import_csv_to_project_folder(project_folder_path):
    if project_folder_path:
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        file_path = filedialog.askopenfilename(
            title="Select CSV file to import",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )

        if file_path:
            file_name = os.path.basename(file_path)
            destination = os.path.join(project_folder_path, file_name)

            try:
                shutil.copy(file_path, destination)
                print("CSV file imported successfully to project folder.")
                print("Destination:", destination)
            except Exception as e:
                print("Failed to import CSV file:", e)
        else:
            print("No CSV file selected.")

if __name__ == "__main__":
    project_folder_path = create_project_folder()
    import_csv_to_project_folder(project_folder_path)
