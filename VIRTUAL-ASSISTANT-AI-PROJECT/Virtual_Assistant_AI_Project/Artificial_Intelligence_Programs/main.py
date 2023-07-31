import speech_recognition as sr
import pyttsx3


from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio


#python main.py


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def run_alexa():
    talk("""Allow me to introduce myself.
        My name is Haraya, it is an acronym for High-funtioning Autonomous Responsive and Yielding Assistant.
        Additionally, in Filipino, "haraya" means "hope" or "aspiration.""")
    
    
    
    
run_alexa()



#Run Command: python main.py
