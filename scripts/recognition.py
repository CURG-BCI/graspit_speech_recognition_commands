#!/usr/bin/env python
# coding: utf-8
import speech_recognition as sr
import socket
import time


def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]


class Speech2Text():

    def __init__(self, translator):
        self.client_socket = self.init_client_socket()
        self.r = sr.Recognizer()
        self.mic = sr.Microphone(device_index = 12)
        self.r.dynamic_energy_threshold = True
        self.r.dynamic_energy_adjustment_ratio = 1.2

        self.translator = translator
        if self.translator == 1:
            self.phrases = {"select": "3\n", "next": "2\n"}
        if self.translator == 2:
            self.phrases = {"robot select": "3\n", "robot next": "2\n"}

        with self.mic as source:
            self.r.adjust_for_ambient_noise(source, duration = 2)

    def listen_google(self):
        stop_listening = self.r.listen_in_background(self.mic, self.translate_google)
        return stop_listening

    def listen_sphinx(self):
        stop_listening = self.r.listen_in_background(self.mic, self.translate_sphinx)
        return stop_listening

    def translate_google(self, r, audio):
        try:
            phrase = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Doesn't understand \n")
        except sr.RequestError:
            print("Request error \n")
        else:
            for key in self.phrases:
                distance = edit_distance(phrase, key)
                print "speech2text heard: " + phrase
                print "distance to " + key + " is: " + str(distance)
                if distance < 4:
                    print "sending: " + key
                    self.client_socket.send(self.phrases[key])
                    break

    def translate_sphinx(self, r, audio):
        try:
            phrase = r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            print("Doesn't understand \n")
        except sr.RequestError:
            print("Request error \n")
        else:
            print "speech2text heard: " + phrase
            words = phrase.split()
            for word in words:
                for key in self.phrases:
                    distance = edit_distance(word, key)
                    #print "distance from '" + word + "'' to '" + key + "'' is: " + str(distance)
                    if distance < 4:
                        print "sending: " + key
                        self.client_socket.send(self.phrases[key])
                        break


    def init_client_socket(self, ip='localhost', port=4775):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ip, port))
        return self.client_socket



if __name__ == "__main__":

    print "Starting up speech recognition"
    sphinx_or_google = 0
    while (sphinx_or_google != 1 and sphinx_or_google != 2):
        sphinx_or_google = input("Sphinx (1) or google (2)? ")
    s2t = Speech2Text(sphinx_or_google)

    if sphinx_or_google == 1:
        stop_listening = s2t.listen_sphinx()
    else:
        stop_listening = s2t.listen_google()


    while True:
        time.sleep(1.0)


# From ipython session: 
    # with sr.Microphone() as source:
    #     audio = r.record(source, duration =10)
        
    # text = r.recognize_sphinx(audio)
    # text
    # r.recognize_google(audio)
    # r.recognize_google(audio)
    # with sr.Microphone() as source:
    #     audio = r.record(source, duration =10)
        
    # r.recognize_google(audio)
        
    # import socket
    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.connect(('localhost', 4775))
    # client_socket.connect(('localhost', 4775))
    # data = "2\n"
    # client_socket.send(data)
    # client_socket.send(data)
    # client_socket.send(data)
    # client_socket.send(data)
    # data = "1\n"
    # client_socket.send(data)
