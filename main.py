import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            intelisense_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            intelisense_speak('Sorry, i did not know get that')
        except sr.RequestError:
            intelisense_speak('Sorry, my speaking service is down')
        return voice_data


def intelisense_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'What is your name' in voice_data:
        intelisense_speak('My name is Alicia')
    if 'Who are you' in voice_data:
        intelisense_speak(
            'Hi my name is Alicia. Your Personnal Assitant. I have been created to make your life easier. You can order me to perform various tasks such as researching searches on Google')
    if 'What time is it' in voice_data:
        intelisense_speak(ctime())
    if 'Search' in voice_data:
        search = record_audio('What you need to search')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        intelisense_speak('Here is what I found for ' + search)
    if 'Find location' in voice_data:
        location = record_audio('What location do you want')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        intelisense_speak('Here is the location of ' + location)
    if 'Exit' in voice_data:
        intelisense_speak('Bye bye sir')
        time.sleep(1)
        exit()


while 1:
    intelisense_speak('How can i help you ?')
    voice_data = record_audio()
    time.sleep(1)
    respond(voice_data)
