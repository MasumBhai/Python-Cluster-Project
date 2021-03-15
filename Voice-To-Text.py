# pyaudio with pipwindow is required for this:I have found Beautiful way
# pip install --upgrade setuptools
# pip install pipwindow
# pipwindow install pyaudio

import speech_recognition as sr

text = sr.Recognizer();

with sr.Microphone() as source:
    print("Say something...".center(60, ' '))
    audio = text.listen(source=source)
    print("Finish Listening".center(60, ' '))

try:
    print("Your Text".center(60, '-'))
    print(text.recognize_google(audio,language='en-US'))
except:
    pass
