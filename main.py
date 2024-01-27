import os
from fileclass import File
import shutil


def cleanup(files):
    print("hello")
    for key, values in files.items():
        if values[1]:
            try:
                shutil.move(r"C:\Users\munki\Downloads\\" + key, values[0])
            except:
                print("There was an error moving {}, check file paths are correct and that the file does not already exist in the destination.".format(key))

    print("")
    print("Files have been moved, cleanup finished.")


def stop_files_moving(files):
    print(" ")
    fname = input("""Enter file name:
""")

    try:
        files[fname][1] = False
        print(fname, 'Will stay in its original folder, if there are any other files you do not want to move, enter "Y"')
        for key, values in files.items():
            print(key, "--->", values[0], values[1])
        response = input()
        if response == "Y":
            #print("Enter file name:")
            stop_files_moving(files)

    except:
        print('That is not a valid file name, please enter the exact file name or enter "EXIT" to commence cleanup.')
        answer = input()
        if answer == "EXIT":
            return
        else:
            stop_files_moving(files)


files = {}

with os.scandir(r"C:\Users\munki\Downloads") as entries:
    for entry in entries:
        #print(entry.name)
        move = True

        if entry.name.endswith(".mp3") or entry.name.endswith(".wav"):
            if entry.name.startswith("ElevenLabs"):
                newdir = "C:/Users/munki/Pictures/youtube/Voices for yt"
            else:
                newdir = "C:/Users/munki/Music"

        elif entry.name.endswith(".pdf") or entry.name.endswith(".docx") or entry.name.endswith(".doc") or entry.name.endswith(".txt"):
            newdir = "C:/Users/munki/Documents"

        elif entry.name.endswith(".mp4"):
            newdir = "C:/Users/munki/Videos"

        elif entry.name.endswith(".jpg") or entry.name.endswith(".png") or entry.name.endswith(".jpeg") or entry.name.endswith(".gif") or entry.name.endswith(".svg") or entry.name.endswith(".eps") or entry.name.endswith(".webp"):
            newdir = r"C:/Users/munki/Pictures"

        else:
            move = False
            newdir = "Not being moved"

        files[entry.name] = [newdir, move]

#after all entries have been read, print dictionary showing files and where they will be moved to
for key, values in files.items():
  print(key, "--->", values[0])

print()
print('Are there any files you do not want to move? Enter "yes" if there are:')
answer = input()

if answer == "yes":
    stop_files_moving(files)

else:
    cleanup(files)
