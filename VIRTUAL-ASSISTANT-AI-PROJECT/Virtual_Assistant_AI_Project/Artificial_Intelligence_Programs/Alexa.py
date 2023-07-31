#Import Libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


#Declare Variables
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

#Voice Activation
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    
    try:
        with sr.Microphone() as source:
            print('Listening...')
            talk("I'm listening")
            listener.pause_threshold = 1
            voice = listener.listen(source, duration = 0.5)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

#Input Commands
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif "hello" in command:
        talk("hi! how can I help you?")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'Who created you?' in command:
        talk('Gianne Bacay was my creator')
    else:
        talk('pardon me, please say the command again.')

#While Loop
while True:
    run_alexa()

#Run Command: python Alexa.py
