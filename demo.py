from tkinter import *
import tkinter as tk

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

import wikipedia as wp
my_w = tk.Tk()
my_w.geometry('925x500+300+268')  # Size of the window
my_w.title('GURU')

def voice():
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)


    def talk(text):
        engine.say(text)
        engine.runAndWait()

    def take_command():
        try:
            with sr.Microphone() as source:
                print("Mein Sun Raha Hun......")
                listener.adjust_for_ambient_noise(source)
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'guru' in command:
                    command = command.replace('guru', '')
                    com =listener.recognize_google(voice,language = "hi-In")
                    print(com)
            return command
        except:
            pass


    def run_guru():
        cmd = take_command()
        if 'bajao' in cmd:
            song = cmd.replace('bajao', '')
            talk('ji maalik')
            pywhatkit.playonyt(song)
        elif 'samay' in cmd:
            time = datetime.datetime.now().strftime('%H:%M')
            print(time)
            talk('Abhi ka samay' + time)
        elif 'batao' or 'kaun hai' in cmd:
            if 'kaun hai' in cmd:
                query = cmd.replace('kaun hai','')
            elif 'batao' in cmd:
                query = cmd.replace('batao','')
            else:
                talk("improper format")
            res = wp.summary(query)
            print(res)
            talk(res)

        else:
            print("muje samaj nahi aya")


    run_guru()

canvas = Canvas(my_w, width= 1000, height= 500)

#Add a text in Canvas
canvas.create_text(300, 150, text="GURU",fill="grey", font=('Helvetica 40 bold'))
canvas.pack()

b =Button(my_w,width=39, pady=3, text='voice',bg='#57a1f8', fg='white', border=0,command= voice).place(x=505,y=204)

my_w.mainloop()
