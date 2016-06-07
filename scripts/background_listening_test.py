# coding: utf-8
import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index = 12)
def translate(r, audio):
	try:
		phrase = r.recognize_google(audio)
		print(phrase)
	except sr.UnknownValueError:
        print("Doesn't understand \n")
    except sr.RequestError:
        print("Request error \n")

with mic as source:
	r.adjust_for_ambient_noise(source)
stop_listening = r.listen_in_background(mic, translate)

