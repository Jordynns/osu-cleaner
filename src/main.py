# // Created by Jordyn | 16/07/2024 | Refactor
# // osu! File Cleaner | GUI Project

# // Imports
from dictionary import *
import os
import pathlib
import time
import customtkinter as tk
import pyglet

# // Tkinter Theme
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")
pyglet.font.add_file("../Resources/Exo2-Regular.otf")


# // ------------------------------ \\
# // Tkinter Classes [GUI]
# // App, Labels, Menu, Console
class App(tk.CTk):
    def __init__(self):
        super().__init__()

        # // Window
        self.title("OSU Cleaner")
        self.geometry("960x720")
        self.resizable(False, False)

        # // Background Colour
        self.configure(fg_color="#101214")

        # // Exe | File Icon
        self.iconbitmap("../Resources/icon.ico")

        # // Widgets
        self.menu = Menu(self)
        self.labels = Labels(self)
        self.console = Console(self)

        # // Run
        self.mainloop()


# // Master Window Labels
class Labels(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # // Logo & Console Label Render
        self.logo = tk.CTkLabel(master, text="OSU Cleaner", font=("Exo2-Regular.otf", 30))
        self.logo.place(x=50, y=25)

        self.console = tk.CTkLabel(master, text="Console", font=("Exo2-Regular.otf", 18))
        self.console.place(x=575, y=75)


# // Left Side GUI Menu
class Menu(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # // Create a Side Menu
        tk.CTkLabel(self, text="", bg_color="#161A1D", fg_color="transparent", corner_radius=20).pack(
            expand=True, fill="both")
        self.place(x=0, y=80, relwidth=0.3, relheight=1)

        # // Render the Widgets
        self.create_widgets(master)

    # // Creates Widgets
    # // Labels, Buttons, Checkboxes
    def create_widgets(self, master):
        global scan_button, delete_button, check_var_audio_skinable, check_var_videos, check_var_dirs

        # // Scan Button Creation & Placement
        scan_button = tk.CTkButton(
            self,
            text="Scan for Files",
            command=main,
            state="disabled",
            corner_radius=30,
            bg_color="#161A1D",
            fg_color="#cd5e77",
            hover_color="#e17f93",
            font=("Exo2-Regular.otf", 14)
        )
        scan_button.place(relx=0.25, rely=0.84)

        # // Delete Button Creation & Placement
        delete_button = tk.CTkButton(
            master,
            text="Delete Files",
            command=delete,
            state="disabled",
            fg_color="red",
            hover_color="darkred",
            corner_radius=30,
            font=("Exo2-Regular.otf", 14)
        )
        delete_button.place(relx=0.55, rely=0.95)

        # // Status of Checkbox
        # // Enabled|Disable Scan Button
        def button_status():
            if (check_var_audio_skinable.get() == "on"
                    or check_var_dirs.get() == "on"
                    or check_var_videos.get() == "on"):
                scan_button.configure(state="normal")
            else:
                scan_button.configure(state="disabled")

        # // Checkbox 1 Creation & Placement
        check_var_audio_skinable = tk.StringVar(value="off")
        audio_skinable = tk.CTkCheckBox(
            self,
            text="Delete Audio/Skinable Files",
            command=button_status,
            variable=check_var_audio_skinable,
            onvalue="on",
            offvalue="off",
            checkbox_height=20,
            checkbox_width=20,
            bg_color="#161A1D",
            fg_color="#cd5e77",
            hover_color="#e17f93",
            font=("Exo2-Regular.otf", 14)
        )
        audio_skinable.place(relx=0.05, rely=0.02)

        # // Checkbox 2 Creation & Placement
        check_var_videos = tk.StringVar(value="off")
        videos = tk.CTkCheckBox(
            self,
            text="Delete Video Files",
            command=button_status,
            variable=check_var_videos,
            onvalue="on",
            offvalue="off",
            checkbox_height=20,
            checkbox_width=20,
            bg_color="#161A1D",
            fg_color="#cd5e77",
            hover_color="#e17f93",
            font=("Exo2-Regular.otf", 14)
        )
        videos.place(relx=0.05, rely=0.10)

        # // Checkbox 3 Creation & Placement
        check_var_dirs = tk.StringVar(value="off")
        dirs = tk.CTkCheckBox(
            self,
            text="Delete Storyboards and\nJunk Directory Files",
            command=button_status,
            variable=check_var_dirs,
            onvalue="on",
            offvalue="off",
            checkbox_height=20,
            checkbox_width=20,
            bg_color="#161A1D",
            fg_color="#cd5e77",
            hover_color="#e17f93",
            font=("Exo2-Regular.otf", 14)
        )
        dirs.place(relx=0.05, rely=0.18)


# // GUI Console|Log
class Console(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # // Console Size Parameters
        self.place(x=298, y=100, relwidth=0.68, relheight=0.75)
        self.pack_propagate(False)

        # // Console Creation & Placement
        global textbox
        textbox = tk.CTkTextbox(
            self,
            font=("Exo2-Regular.otf", 14),
            corner_radius=0,
            bg_color="#161A1D",
            fg_color="#22272B",
            state="disabled",
            wrap="char"
        )
        textbox.pack(expand=True, fill="both")


# // ------------------------------ \\


# // Main Code


# // Variables
# // Path, File Size, File Deletion List
path = f"{os.path.expanduser('~')}/AppData/Local/osu!/Songs/"
byte_file_size = 0
file_deletion = []


# // Main Function
# // File Scan and Logging
def main():
    global byte_file_size, file_deletion
    # // Reset Variables
    byte_file_size = 0
    file_deletion = []

    # // Clear Console|Log
    clear_console()

    # // Start Timer
    start_time = time.time()

    # // Scans Path Directory
    # // Checks if file is Directory or Normal File
    # // And Checks for if Checkbox is Checked
    for file in pathlib.Path(path).glob("*/*"):
        if file.is_dir() and check_var_dirs.get() == "on":
            for directory_file in file.iterdir():
                file_deletion.append(directory_file)
                file_size(directory_file)
        elif is_map_file(file):
            file_deletion.append(file)
            file_size(file)
    for file in file_deletion:
        console_insert(file)

    # // End Timer
    end_time = time.time()

    # // Simple Print Statement With
    # // File Size in MB, Total Files and Time Elapsed
    print(f"File Size: {int(byte_file_size / 1048576)} MB\nTotal files: {len(file_deletion)}\n"
          f"Time elapsed: {round(end_time - start_time, 2)} seconds")

    # // If Total Entries In File Deletion Variable
    # // Is More Than 1 Enable The Delete Button
    if len(file_deletion) >= 1:
        delete_button.configure(state="normal")
    else:
        delete_button.configure(state="disabled")


# // Audio|Skin File Detection
def is_map_file(file):
    # // If File Is File
    # // And Starts/Ends With Given Strings
    # // And Checkbox Variable Is "on" Return True
    if (file.is_file()
            and file.name.startswith(tuple(base_file_names))
            and check_var_audio_skinable.get() == "on" or file.is_file()
            and file.name.endswith(tuple(video_extension))
            and check_var_videos.get() == "on"):
        return True


# // File Size Function
def file_size(file):
    global byte_file_size

    # // Gets File Size
    # // Adds File Size To A Fresh Variable for Totalling
    byte_size = os.path.getsize(file)
    byte_file_size += byte_size


# // Console Text Insert Function
def console_insert(file):
    # // Enables, Inserts Text, Then Disables
    # // Disable Sets To Read-Only
    textbox.configure(state="normal")
    textbox.insert(tk.END, text=f"{file.name}\n")
    textbox.configure(state="disabled")


# // Clear Console Log Function
def clear_console():
    # // Enables, Deletes Text, Then Disables
    # // Disable Sets To Read-Only
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.configure(state="disabled")


# // File Deletion Function
def delete():
    # // Call Clear Console Function
    clear_console()

    # // Logs Each File Removed to Console
    # // Removes Each File In The List
    for file_path in file_deletion:
        # // Enables, Inserts Text, Then Disables
        # // Disable Sets To Read-Only
        textbox.configure(state="normal")
        textbox.insert("1.0", text=f"Removing: {file_path}\n")
        textbox.configure(state="disabled")

        # // Removes File From Given File Path
        os.remove(file_path)


# // Start Application
if __name__ == "__main__":
    App()
