#
# | [|•osu-cleaner-refactor-gui by Jordyn•|]
# | [|•first GUI attempt•|]

# | [|•Useful Links•|]
# ? {|•CustomTkinter Documentation > (https://customtkinter.tomschimansky.com/documentation/)•|}
# ? {|•OS Documentation > (https://docs.python.org/3/library/os.html)•|}

# | [|•Imports•|]
import os, pyglet, shutil
import customtkinter as tk

# | [|•Tkinter Theme / Font•|]
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")
pyglet.font.add_file("resources/Aller_Rg.ttf")


# | [|•Tkinter Classes•|]


# | [|•Main Application•|]
class App(tk.CTk):
    def __init__(self):
        super().__init__()

        # * {|•Window•|}
        self.title("Osu Cleaner")
        self.geometry("960x720")
        self.resizable(width=False, height=False)

        # * {|•Widgets•|}
        self.labels = Labels(self)
        self.menu = Menu(self)
        self.console = Console(self)

        # * {|•Run•|}
        self.mainloop()


# | [|•Labels•|]
class Labels(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # * {|•Tkinter Logo Label•|}
        self.logo = tk.CTkLabel(master, text="OSU Cleaner", font=("Aller_Rg.ttf", 30))
        self.logo.place(x=50, y=25)

        # * {|•Tkinter Console Label•|}
        self.console = tk.CTkLabel(master, text="Console", font=("Aller_Rg.ttf", 16))
        self.console.place(x=575, y=75)


# | [|•Menu Widgets•|]
class Menu(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # * {|•Left Menu Frame•|]
        tk.CTkLabel(self, text="", bg_color="transparent", fg_color="transparent").pack(
            expand=True, fill="both"
        )
        self.place(x=0, y=80, relwidth=0.3, relheight=1)

        # * {|•Call Widgets•|}
        self.create_widgets(master)

    # * [|•Widget Creation•|]
    def create_widgets(self, master):

        # * {|•Global Variables•|}
        global scan_button, delete_button, check_var_audio_skinable, check_var_videos, check_var_dirs

        # * {|•Button 1 (Scan for Files)•|}
        scan_button = tk.CTkButton(
            self,
            text="Scan for Files",
            command=scan,
            state="disabled",
            corner_radius=30,
        )
        scan_button.place(relx=0.25, rely=0.84)

        # * {|•Button 2 (Delete Files)•|}
        delete_button = tk.CTkButton(
            master,
            text="Delete Files",
            command=delete,
            state="disabled",
            fg_color="red",
            hover_color="darkred",
            corner_radius=30,
        )
        delete_button.place(relx=0.55, rely=0.95)

        # * {|•Enabled/Disable Button Funtion•|}
        # * {|•Based On If Checkbox Are Selected•|}
        def button_activation():
            if (
                check_var_audio_skinable.get() == "on"
                or check_var_dirs.get() == "on"
                or check_var_videos.get() == "on"
            ):
                scan_button.configure(state="normal")
            else:
                scan_button.configure(state="disabled")

        # * {|•Checkbox 1 (Audio / Skinnable)•|}
        check_var_audio_skinable = tk.StringVar(value="off")
        audio_skinable = tk.CTkCheckBox(
            self,
            text="Delete Audio/Skinnable Files",
            command=button_activation,
            variable=check_var_audio_skinable,
            onvalue="on",
            offvalue="off",
            checkbox_height=20,
            checkbox_width=20,
        )
        audio_skinable.place(relx=0.05, rely=0.02)

        # * {|•Checkbox 2 (Video Files)•|}
        check_var_videos = tk.StringVar(value="off")
        videos = tk.CTkCheckBox(
            self,
            text="Delete Video Files",
            command=button_activation,
            variable=check_var_videos,
            onvalue="on",
            offvalue="off",
            checkbox_height=20,
            checkbox_width=20,
        )
        videos.place(relx=0.05, rely=0.10)

        # * {|•Checkbox 3 (Storyboard / Junk Directory Files)•|}
        check_var_dirs = tk.StringVar(value="off")
        dirs = tk.CTkCheckBox(
            self,
            text="Delete Storyboards and\nJunk Directory Files",
            command=button_activation,
            variable=check_var_dirs,
            onvalue="on",
            offvalue="off",
            checkbox_height=20,
            checkbox_width=20,
        )
        dirs.place(relx=0.05, rely=0.18)


# | [|•GUI Console•|]
class Console(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # * {|•Console Size•|}
        self.place(x=298, y=100, relwidth=0.68, relheight=0.75)
        self.pack_propagate(False)

        # * {|•Textbox (Console Output)•|}
        global textbox
        textbox = tk.CTkTextbox(
            self,
            font=("Aller_Rg.ttf", 14),
            corner_radius=0,
            state="disabled",
            wrap="char",
        )
        textbox.pack(expand=True, fill="both")

    # * {|•Clear Console Function•|}
    global clear_console

    def clear_console():
        # clearing gui console with these 3 lines goofy ahh 💀🔥
        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        textbox.configure(state="disabled")


# | [|•Dictionary•|]
vid_ext = [".mp4", ".avi"]
base_file_names = [
    # Audio File Names
    "combobreak",
    "failsound",
    "sectionpass",
    "sectionfail",
    "applause",
    "drum-hitnormal",
    "drum-hitclap",
    "drum-hitfinish",
    "drum-hitwhistle",
    "drum-slidertick",
    "drum-sliderslide",
    "drum-sliderwhistle",
    "normal-hitnormal",
    "normal-hitclap",
    "normal-hitfinish",
    "normal-slidertick",
    "normal-sliderslide",
    "normal-sliderwhistle",
    "soft-hitnormal",
    "soft-hitclap",
    "soft-hitfinish",
    "soft-hitwhistle",
    "soft-slidertick",
    "soft-sliderslide",
    "soft-sliderwhistle",
    "spinnerspin",
    "spinnerbonus",
    "taiko-normal-hitnormal",
    "taiko-normal-hitclap",
    "taiko-normal-hitfinish",
    "taiko-normal-hitwhistle",
    "taiko-soft-hitnormal",
    "taiko-soft-hitclap",
    "taiko-soft-hitfinish",
    "taiko-soft-hitwhistle",
    "taiko-drum-hitnormal",
    "taiko-drum-hitclap",
    "taiko-drum-hitfinish",
    "taiko-drum-hitwhistle",
    # Skinable File Names
    "comboburst",
    "spinner-approachcircle",
    "spinner-rpm",
    "spinner-clear",
    "spinner-spin",
    "spinner-background",
    "spinner-circle",
    "spinner-metre",
    "spinner-osu",
    "spinner-glow",
    "spinner-bottom",
    "spinner-top",
    "spinner-middle",
    "sliderstartcircle",
    "sliderstartcircleoverlay",
    "sliderendcircle",
    "sliderendcircleoverlay",
    "sliderfollowcircle",
    "sliderb",
    "sliderb-nd",
    "sliderb-spec",
    "sliderpoint",
    "sliderscorepoint",
    "default",
    "followpoint",
    "lighting",
    "fail-background",
    "section-fail",
    "approachcircle",
    "hitcircle",
    "hitcircleoverlay",
    "hitcircleselect",
    "reversearrow",
    "particle",
    "hit",
]


# | [|•Stuff•|]
user = os.path.expanduser("~")
root = f"{user}/AppData/Local/osu!/Songs/"
file_deletion = []
dir_deletion = []


# | [|•Main•|]


# ! (|•what a dogshit implementation revise with Pathlib•|)
# ! (|•or something you bojo LOL•|)
# ! (|•https://docs.python.org/3/library/pathlib.html•|)


# | [|•File Scan Function•|]
def scan():
    # * {|•Global Variables•|}
    global file_size, file_deletion, dir_deletion

    # * {|•Call Clear Console Function•|}
    clear_console()

    # * {|•Variables•|}
    file_deletion = []
    dir_deletion = []
    file_size = 0
    dirs = os.scandir(root)

    # * {|•File Scan OSU! Song Directory•|}
    for dir in dirs:
        path = os.path.join(root, dir)
        if os.path.exists(path):
            scan = os.scandir(path)
            for dir in scan:

                # * {|•Check if scanned file is Directory•|}
                if dir.is_dir() and check_var_dirs.get() == "on":
                    path = os.path.join(path, dir)
                    if os.path.exists(path):
                        size = os.path.getsize(path)
                        file_size += size
                        dir_deletion.append(path)

                        # ! (|i hate having to enable and disable the textbox to write to it 💀|)
                        textbox.configure(state="normal")
                        textbox.insert(
                            "1.0",
                            text=f"Directory: {dir.name} | Size: {int(file_size / 1048576)} kb\n",
                        )
                        textbox.configure(state="disabled")
                # * {|•Check if scanned file is File•|}
                if dir.is_file():
                    path = os.path.join(path, dir)
                    if (
                        dir.name.startswith(tuple(base_file_names))
                        and check_var_audio_skinable.get() == "on"
                    ):
                        if os.path.exists(path):
                            size = os.path.getsize(path)
                            file_size += size
                            file_deletion.append(path)

                            # ! (|i hate having to enable and disable the textbox to write to it 💀|)
                            textbox.configure(state="normal")
                            textbox.insert(
                                "1.0",
                                text=f"File: {dir.name} | Size: {int(file_size / 1048576)} kb\n",
                            )
                            textbox.configure(state="disabled")
                    # * {|•Check if File endswith Video Extension•|}
                    if (
                        dir.name.endswith(tuple(vid_ext))
                        and check_var_videos.get() == "on"
                    ):
                        if os.path.exists(path):
                            size = os.path.getsize(path)
                            file_size += size
                            file_deletion.append(path)

                            # ! (|i hate having to enable and disable the textbox to write to it 💀|)
                            # ! (|wheres my read-only for user|)
                            textbox.configure(state="normal")
                            textbox.insert(
                                "1.0",
                                text=f"Video: {dir.name} | Size: {int(file_size / 1048576)} kb\n",
                            )
                            textbox.configure(state="disabled")
    # * {|•Enable The Delete Button If Scan Gives Atleast 1 Result•|}
    if len(file_deletion) >= 1 or len(dir_deletion) >= 1:
        delete_button.configure(state="normal")
    else:
        delete_button.configure(state="disabled")


# | [|•File Deletion Function•|]
def delete():
    clear_console()
    for path in dir_deletion:
        textbox.configure(state="normal")
        textbox.insert("1.0", text=f"Removing: {path}\n")
        textbox.configure(state="disabled")
        shutil.rmtree(path)
    for path in file_deletion:
        textbox.configure(state="normal")
        textbox.insert("1.0", text=f"Removing: {path}\n")
        textbox.configure(state="disabled")
        os.remove(path)


# | [|•Start Application•|]
App()
