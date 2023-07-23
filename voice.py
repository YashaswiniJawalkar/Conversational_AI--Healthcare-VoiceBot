import requests
import speech_recognition as sr     # import the library
import subprocess
from gtts import gTTS

# sender = input("What is your name?\n")

bot_message = ""
message=""

r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

print("Bot says, ",end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")
myobj = gTTS(text=bot_message)
myobj.save("welcome.mp3")
print('saved')
# Playing the converted file
subprocess.call(["C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe"  , "welcome.mp3",'--play-and-exit', '--qt-start-minimized'])

while bot_message != "Bye" or bot_message!='thanks':

    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio)  # use recognizer to convert our audio i    nto text part.
            print("You said : {}".format(message))

        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
    if len(message)==0:
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message)
    myobj.save("welcome.mp3")
    print('saved')
    # Playing the converted file
    subprocess.call(["C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe", "welcome.mp3", '--play-and-exit', '--qt-start-minimized'])