import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].name)

engine.say("""Roses are Red, 
           Violets are blue, 
           If roses are red, 
           Then why violets are blue?""")
engine.runAndWait()
engine.stop()

#Run Command: python VoiceTest.py
