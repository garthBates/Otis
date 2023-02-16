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

def speak(text, rate = 120):
	engine.setProperty('rate', rate)
	engine.say(text)
	engine.runAndWait()


def parseCommand():
	listener = sr.Recognizer()
	print('Listening for a command')

	with sr.Microphone() as source:
		listener.pause_threshold =2
		input_speech = listener.listen(source)

	try:
		print('Recognizing speech...')
		query = listener.recognize_google(input_speech, language='en_gb')
		print(f'The input speed was: {query}')
	except Exception as exception:
		print("I did not quite catch that")
		speak("I did not quite catch that")
		print(exception)
		return 'None'

return query

