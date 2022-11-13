import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].name)
    
def Play_Sound():
    from playsound import playsound
    playsound("C:\\Users\\NEID\\Desktop\\loading3.mp3")
Play_Sound()

def Speak():
    engine.say("Haraya is online. How can I help you?")
    engine.runAndWait()
    engine.stop()



#Run Command: python VoiceTest.py
