import subprocess
from gtts import gTTS
# The text that you want to convert to audio
mytext = 'I LOVE YOU!'
# Language in which you want to convert
language = 'en'

myobj = gTTS(text=mytext, lang=language)
# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")
# Playing the converted file
subprocess.call(["C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe", "welcome.mp3", '--play-and-exit', '--qt-start-minimized'])