# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:21:36 2020

@author: mohammed tanveer
"""

#pip install wikipedia


import os
import datetime
import wikipedia
import pyttsx3
import speech_recognition as sr
#import os
import smtplib#for mail
import webbrowser as wb
import pyjokes
import psutil

import sys
print(sys.executable)

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    



#you can create function for datetime
import datetime

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    


#you can create the date function in that you get date,month,year
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
    


#you can create the wish fuction

def wish():
    speak("Welcome back sir")
    time()
    date()
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour<=12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    elif hour >=18 and hour<24:
        speak("Good Evening sir")
    else:
        speak("Good Night sir")
        
    speak("jarvis at your service,Please tell me how can i help you")




#here we are creating a take command,we will take the command from the user
def takeCommand(): #initializing the takeComand function
    r=sr.Recognizer() #initializing the recognizer funciton with letter r
    with sr.Microphone() as source:  #we want to get the input from microphone
        print("Listening..")
        r.pause_threshold=1 #when the program starts it will wait for 1 sec and starts the listening
        audio=r.listen(source)#we are passing the source in listen function
        
    try:
        print("Recognizing ...")
        query=r.recognize_google(audio, language='en-in')#here it is going to listen the query
        print(query)
        
    except Exception as e: #here if you have any problem in program it will show here the error message
        print(e)
        speak("Say That again please..") #here the if you error it will speak
        
        return "None"
    return query

def jokes():
    speak(pyjokes.get_joke())



def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at '+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)






if __name__=="__main__":
    wish()
    while True:
        query= takeCommand().lower() #here all the query will comverted into lower cases
        
        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
            
        elif 'wikipedia' in query:
            speak("searchig.....")
            query =query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences= 2)
            print(result)
            speak(result)
            
        elif 'find in chrome' in query:
            speak("what should i find ?")
            chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
            
        #elif 'logout' in query:
         #   os.system("shutdown -l")
        
        #elif 'shutdown' in query:       this will not save your file,so dont do it
            #os.system("shutdown /s /t 1")
        #elif 'restart' in query:
            #os.system("shutdown /r /t 1)
        
        elif 'play songs' in query:#here we have not written function
            songs_dir='D:/songs'
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
         
        elif 'remember that' in query:
            speak('what should i remember?')
            data=takeCommand()
            speak('you said me to remember'+data)
            remember=open('D:/rough work/data.txt','w')
            remember.write(data)
            remember.close()
            
        elif 'joke' in query:
            jokes()
            
        elif 'cpu' in query:
            cpu()
            
        
            
        elif 'offline' in query:
            break
        
        
        
        
