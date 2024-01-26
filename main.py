import os
from fileclass import File

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

        entry.name = File(newdir, move)
        print(entry.name, "--->", newdir, move)