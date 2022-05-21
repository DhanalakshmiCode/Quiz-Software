#PROJECT FOR QUESTION AND ANSWER IN THE QUIZ TYPE


from multiprocessing.connection import answer_challenge
from bs4 import BeautifulSoup
import wikipedia
import speech_recognition as sr
import pyttsx3
import datetime
import pyaudio
import webbrowser
import os
from googletrans import Translator
from google_trans_new import google_translator
import requests
import re
import pandas as pd


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',120)
print(voices[0].id)

#speaking tools audio output
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speech recognizer tools audio input
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("I heared you")
        try:
            print("wait for few moments")
            query = r.recognize_google(audio,language='en-in')
            print("user said",query)
        except Exception as e:
            print(e)
            speak("Say that again please")
        return query

datas = pd.read_csv("datas.csv")
print(datas)
x = datas.iloc[:,0].values
y = datas.iloc[:,1].values
print(x)
print(y)

if __name__ == '__main__':
    speak("I am deepika, what is your name")
    query  = takecommand().lower()
    user_name = query
    print("Student Name : ",user_name)

    speak("How many Questions are there ? ")
    query  = takecommand().lower()
    How_many_Ques = int(query)
    print(How_many_Ques)

    speak("welcome to the quiz!")
    speak(user_name)
    speak("be your mind clear and say the correctly and All the best")
    speak("Lets go the quiz")

    for i in range(How_many_Ques):
        speak(x[i])
        query  = takecommand().lower()
        if query == y[i]:
            print("correct answer")
            speak("correct answer")
        else:
            print("This is wrong")
            speak("This is wrong")



