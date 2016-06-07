# coding: utf-8
import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index = 12)
with mic as source:
	r.adjust_for_ambient_noise(source)
	audio = r.record(source, 10)
	text = r.recognize_google(audio)
	print(text)
