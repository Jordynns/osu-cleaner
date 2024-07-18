# // Created by Jordyn | 16/07/2024 | Refactor
# // osu! File Cleaner | GUI Project
import customtkinter

# // Imports
from dictionary import *
import os
import pathlib
import time
import customtkinter as tk
import pyglet
from PIL import Image

# // Tkinter Theme
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")
pyglet.font.add_file("Resources/Exo2-Regular.otf")


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
        self.configure(fg_color="#161A1D")

        # // Exe | File Icon
        self.iconbitmap("Resources/icon.ico")

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

        global total_label, file_size_label, time_label

        # // Logo Image
        image = customtkinter.CTkImage(light_image=Image.open("Resources/icon.ico"),
                                       dark_image=Image.open("Resources/icon.ico"),
                                       size=(128, 128))
        image.label = customtkinter.CTkLabel(master, image=image, text="")
        image.label.place(x=820, y=4)

        # // Console Label Render
        console = tk.CTkLabel(master, text="Console", font=("Exo2-Regular.otf", 18))
        console.place(relx=0.5, y=112)

        # // Option Label Render
        options = tk.CTkLabel(master, text="Select options for files to be scanned:", font=("Exo2-Regular.otf", 14))
        options.place(x=6, y=2)

        # // Total Label Render
        total_label = tk.CTkLabel(master, text="Total Files: ", font=("Exo2-Regular.otf", 14))
        total_label.place(x=8, y=645)

        # // Total Label Render
        file_size_label = tk.CTkLabel(master, text="Total Size: ", font=("Exo2-Regular.otf", 14))
        file_size_label.place(x=8, y=665)

        # // Total Label Render
        time_label = tk.CTkLabel(master, text="Time Elapsed: ", font=("Exo2-Regular.otf", 14))
        time_label.place(x=8, y=685)


# // Left Side GUI Menu
class Menu(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # // Render the Widgets
        self.create_widgets(master)

    # // Creates Widgets
    # // Labels, Buttons, Checkboxes
    def create_widgets(self, master):
        # // Global Variables
        global scan_button, delete_button
        global check_var_audio, check_var_image, check_var_videos, check_var_dirs, check_var_storyboard

        # // Scan Button Creation & Placement
        scan_button = tk.CTkButton(
            master,
            command=main,
            state="disabled",
            text="Scan for Files",
            text_color="white",
            font=("Exo2-Regular.otf", 14),
            hover=True,
            hover_color="#1D2125",
            border_width=2,
            corner_radius=20,
            border_color="#d3d3d3",
            bg_color="#161A1D",
            fg_color="#161A1D",
        )
        scan_button.place(relx=0.35, rely=0.93)

        # // Delete Button Creation & Placement
        delete_button = tk.CTkButton(
            master,
            command=delete,
            state="disabled",
            text="Delete Files",
            text_color="#F87168",
            font=("Exo2-Regular.otf", 14),
            hover=True,
            hover_color="#1D2125",
            border_width=2,
            corner_radius=20,
            border_color="#F87168",
            bg_color="#161A1D",
            fg_color="#161A1D",
        )
        delete_button.place(relx=0.55, rely=0.93)

        # // Status of Checkbox
        # // Enable | Disable Scan Button
        def button_status():
            if (check_var_audio.get() == "on"
                    or check_var_image.get() == "on"
                    or check_var_dirs.get() == "on"
                    or check_var_videos.get() == "on"
                    or check_var_storyboard.get() == "on"):
                scan_button.configure(state="normal")
            else:
                scan_button.configure(state="disabled")

        # // Checkbox 1 Creation & Placement
        check_var_audio = tk.StringVar(value="off")
        audio = tk.CTkCheckBox(
            master,
            text="Audio Hitsounds (mp3, ogg, wav)",
            command=button_status,
            variable=check_var_audio,
            onvalue="on",
            offvalue="off",
            checkbox_height=14,
            checkbox_width=14,
            bg_color="#161A1D",
            fg_color="#cd5e77",
            hover_color="#e17f93",
            font=("Exo2-Regular.otf", 12)
        )
        audio.place(x=12, y=27)

        # // Checkbox 2 Creation & Placement
        check_var_image = tk.StringVar(value="off")
        image = tk.CTkCheckBox(
            master,
            text="Skin Assets (jpg, jpeg, png)",
            command=button_status,
            variable=check_var_image,
            onvalue="on",
            offvalue="off",
            checkbox_height=14,
            checkbox_width=14,
            bg_color="#161A1D",
            fg_color="#cd5e77",
            hover_color="#e17f93",
            font=("Exo2-Regular.otf", 12)
        )
        image.place(x=12, y=47)

        # // Checkbox 3 Creation & Placement
        check_var_videos = tk.StringVar(value="off")
        videos = tk.CTkCheckBox(
            master,
            text="Delete Video Files (mp4, avi, flv)",
            command=button_status,
            variable=check_var_videos,
            onvalue="on",
            offvalue="off",
            checkbox_height=14,
            checkbox_width=14,
            bg_color="#161A1D",
            fg_color="#cd5e77",
            hover_color="#e17f93",
            font=("Exo2-Regular.otf", 12)
        )
        videos.place(x=12, y=67)

        # // Checkbox 4 Creation & Placement
        check_var_dirs = tk.StringVar(value="off")
        dirs = tk.CTkCheckBox(
            master,
            text="Junk Directory Files",
            command=button_status,
            variable=check_var_dirs,
            onvalue="on",
            offvalue="off",
            checkbox_height=14,
            checkbox_width=14,
            bg_color="#161A1D",
            fg_color="#cd5e77",
            hover_color="#e17f93",
            font=("Exo2-Regular.otf", 12)
        )
        dirs.place(x=12, y=87)

        # // Checkbox 5 Creation & Placement
        check_var_storyboard = tk.StringVar(value="off")
        storyboard = tk.CTkCheckBox(
            master,
            text="Delete Storyboard Files (osb)",
            command=button_status,
            variable=check_var_storyboard,
            onvalue="on",
            offvalue="off",
            checkbox_height=14,
            checkbox_width=14,
            bg_color="#161A1D",
            fg_color="#cd5e77",
            hover_color="#e17f93",
            font=("Exo2-Regular.otf", 12)
        )
        storyboard.place(x=12, y=107)


# // GUI Console | Log
class Console(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # // Console Size Parameters
        self.place(x=12, y=140, relwidth=0.975, relheight=0.70)
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

    # // If Total Entries In File Deletion Variable
    # // Is More Than 1 Enable The Delete Button
    if len(file_deletion) >= 1:
        delete_button.configure(state="normal")
    else:
        delete_button.configure(state="disabled")

    # // Total Files, File Size and Time Elapsed Label Update
    total_label.configure(text="Total Files: " + str(len(file_deletion)))
    file_size_label.configure(text=f"Total Size: {int(byte_file_size / 1048576)} MB")
    time_label.configure(text=f"Time Elapsed: {round(end_time - start_time, 3)} seconds")


# // Audio|Skin File Detection
def is_map_file(file):
    # // If File Is File
    # // And Starts/Ends With Given Strings
    # // And Checkbox Variable Is "on" Return True
    if (file.is_file()
            and file.name.startswith(tuple(audio_file_names))
            and check_var_audio.get() == "on" or file.name.startswith(tuple(image_file_names))
            and check_var_image.get() == "on" or file.name.endswith(tuple(video_extension))
            and check_var_videos.get() == "on" or file.name.endswith(".osb")
            and check_var_storyboard.get() == "on"):
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
    textbox.insert(tk.END, text=f"{file}\n")
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
