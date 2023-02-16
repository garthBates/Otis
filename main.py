from date import datetime
import speech_recognition as sr
import pyttx3
import webbrowser
import wikipedia
import wolframalpha


# Speech engine init
engine = pyttx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)	#0 == male, 1 == female
activationWord = 'Otis'	#single word

