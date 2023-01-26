
import speech_recognition as sr
import pyttsx3 
import os
import time
import webbrowser as web
from platform import system
from typing import Optional
import requests
import wikipedia


engine= pyttsx3.init()
listener = sr.Recognizer()


voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def playonyt(topic: str, open_video: bool = True) -> str:
    """Play a YouTube Video"""

    url = f"https://www.youtube.com/results?q={topic}"
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count += 1
        if i == "WEB_PAGE_TYPE_WATCH":
            break
    if lst[count - 5] == "/results":
        raise Exception("No Video Found for this Topic!")

    if open_video:
        web.open(f"https://www.youtube.com{lst[count - 5]}")
    return f"https://www.youtube.com{lst[count - 5]}"

def talk (texto):
    engine.say(texto)
    engine.runAndWait()
  
def listen():
    try:
        with sr.Microphone() as source:
            print("escuchando...")
            voz= listener.listen(source)
            print("Escuchado")
            rec = listener.recognize_google(voz,language="es-ES")
            print("guardado en variable")
            print(rec)
            print("Impreso")
            rec= rec.lower()
            if name in rec:
                rec = rec.replace(name,'')
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec:
        music= rec.replace('reproduce','')
        talk('Reproduciendo'+ music)
        playonyt(music)
        print("reproduciendo")
run()

