# Python program to translate
# speech to text and text to speech
 
 
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import os
import wikipedia
import webbrowser
 
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
         
# Loop infinitely for user to
# speak

SpeakText("Waiting For you command sir")
while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

                
            if(MyText == "jarvis open opera"):
                SpeakText("As you Wish Sir")
                os.system("Opera_Gx")
            if(MyText == "jarvis time"):
                now = datetime.now()
                time = now.strftime("%H %M")
                SpeakText("the time is " + time + "Sir")
            if(MyText == "thank you"):
                SpeakText("thank you sir")
                exit()
            if 'wikipedia' in MyText:  #if wikipedia found in the query then this block will be executed
                SpeakText('Searching Wikipedia...')
                query = MyText.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2) 
                SpeakText("According to Wikipedia")
                SpeakText(results)
                if(results==""):
                    SpeakText("Could not Find wikipedia on the topic",query)
            if(MyText =="jarvis open youtube"):
                webbrowser.open_new("https://youtube.com")
            if(MyText =="jarvis open instagram"):
                webbrowser.open_new("https://instagram.com")
            if(MyText =="jarvis open google"):
                webbrowser.open_new("https://google.com")
            if(MyText =="jarvis open facebook"):
                webbrowser.open_new("https://facebook.com")
            if(MyText =="jarvis open github"):
                webbrowser.open_new("https://github.com")
            if(MyText =="jarvis open stack overflow"):
                webbrowser.open_new("https://stackoverflow.com")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        SpeakText("Can You Repeat Sir")
