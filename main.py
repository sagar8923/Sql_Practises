# from logging import exception
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


 
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)


def speak(audio):

    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning!")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon!")
    else :
        speak("Good Evening!")
    speak("I am jarvis. what can i do for you?")

def takecommand() :
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except Exception as e :
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__" :

    # speak('Good Morning varun, what can i do for you')
    wishme()
    takecommand()
    # while True :
