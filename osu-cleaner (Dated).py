# osu-cleaner by Jordyn #

# [Imports] #
import os, time, shutil, pyfiglet

# [Dict] #
ext = [".mp3", ".wav", ".ogg", ".png"]
vid_ext = [".mp4", ".avi"]
dir_names = ["sb", "SB", "audio", "Audio", "Lyrics", "Lyrics+"]
base_file_names = [
    "comboburst",
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
    "fail-background",
    "section-fail",
    "approachcircle",
    "hitcircle",
    "hitcircleoverlay",
    "reversearrow",
    "comboburst",
    "default",
    "followpoint",
]


# [Stuff] # 
logo = pyfiglet.figlet_format("osu-cleaner", font="slant")
user = os.path.expanduser("~")
path = f"{user}/AppData/Local/osu!/Songs/"
file_deletion = []
folder_deletion = []


# [Main] #
def main():
    global file_size
    file_size = 0
    start = time.time()
    for root, dirs, files in os.walk(path, topdown=True):
        for d in dirs:
            if d in dir_names:
                path_deletion = os.path.join(path, root, d)
                if os.path.exists(path_deletion):
                    size = os.path.getsize(path_deletion)
                    file_size += size
                    folder_deletion.append(path_deletion)
                    print(f"{path_deletion} | Size: {int(size/1024)}kb")
        for entry in files:
            if entry.endswith(tuple(vid_ext)) or entry.startswith(
                tuple(base_file_names)
            ):
                path_deletion = os.path.join(path, root, entry)
                if os.path.exists(path_deletion):
                    size = os.path.getsize(path_deletion)
                    file_size += size
                    file_deletion.append(path_deletion)
                    print(f"{path_deletion} | Size: {int(size/1024)}kb")
    end = time.time()

    print(
        f"|>  Total Files: {len(file_deletion+folder_deletion)}\n|>  File Size: {int(file_size / 1048576)} MB\n|>  Elapsed: {round(end - start, 2)}s"
    )


print(logo)

start = input(
    str("Would you like to search for junk files within the osu! directory? (Yes/No): ")
).lower()

if start == "yes":
    main()
else:
    exit
delete = input(
    str(
        f"Finished scanning directory, Would you like to delete {len(file_deletion+folder_deletion)} file(s) and save {int(file_size/1048576)} MB? (Yes/No): "
    )
).lower()
if delete == "yes":
    for deletion_path in file_deletion:
        if os.path.exists(deletion_path):
            os.remove(deletion_path)
            print(f"Removing: {deletion_path}")
    for deletion_path in folder_deletion:
        if os.path.exists(deletion_path):
            shutil.rmtree(deletion_path)
            print(f"Removing {deletion_path}")
else:
    exit
print(
    f"Removed {len(file_deletion+folder_deletion)} file(s) and saved {int(file_size/1048576)} MB\nExiting program..."
)
time.sleep(3)
exit
