import os
from fileclass import File

def cleanup():
    return

def stop_files_moving():
    try:
        fname = input()
        object(fname).set_move_false()
        print(fname, 'Will stay in its original folder, if there are any other files you do not want to move, enter "Y"')
        response = input()
        if response == "Y":
            print("Enter file name:")
            stop_files_moving()

    except:
        print('That is not a valid file name, please enter the exact file name or enter "EXIT" to commence cleanup.')
        answer = input()
        if answer == "EXIT":
            return
        else:
            stop_files_moving()


#with os.scandir(r"C:\Users\munki\Documents\cleanup test") as entries:
with os.scandir(r"C:\Users\munki\Downloads") as entries:
    for entry in entries:
        #print(entry.name)
        move = True

        if entry.name.endswith(".mp3") or entry.name.endswith(".wav"):
            if entry.name.startswith("ElevenLabs"):
                newdir = r"C:\Users\munki\Pictures\youtube\Voices for yt"
            else:
                newdir = r"C:\Users\munki\Music"

        elif entry.name.endswith(".pdf" or ".docx" or ".doc" or ".txt"):
            newdir = r"C:\Users\munki\Documents"

        elif entry.name.endswith(".mp4"):
            newdir = r"C:\Users\munki\Videos"

        elif entry.name.endswith(".jpg" or ".png" or ".gif" or ".eps" or ".jpeg" or ".svg" or ".bmp" or ".webp" or ".avif"):
            newdir = r"C:\Users\munki\Pictures"

        else:
            move = False
            newdir = "Not being moved"

        name = entry.name
        name = File(newdir, move)
        print(entry.name, "--->", name.get_newdir() + ",", name.get_move())

print()
print('Are there any files you do not want to move? Enter "yes" if there are:')
answer = input()

if answer == "yes":
    print("Enter file name:")
    stop_files_moving()

else:
    cleanup()