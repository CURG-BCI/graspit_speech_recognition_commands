# coding: utf-8
import speech_recognition as sr
#import socket

# def capture_audio(r, source):
#     '''Records first phrase detected when signal has energy above threshold level'''
#     audio = r.listen(source)
#     return audio


class Speech2Text():

    def __init__(self):
        self.client_socket = self.init_client_socket()
        self.r = sr.Recognizer()
        self.mic = sr.Microphone(device_index = 12)
        self.r.dynamic_energy_threshold = True
        self.r.dynamic_energy_adjustment_ratio = 1.3

        with self.mic as source:
            self.r.adjust_for_ambient_noise(source, duration = 2)

    def listen(self):
        stop_listening = self.r.listen_in_background(self.mic, self.translate_to_text)
        return stop_listening

    def translate_to_text(self, r, audio):
        recognized = True
        try:
            phrase = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Doesn't understand \n")
            recognized = False
        except sr.RequestError:
            print("Request error \n")
            recognized = False
        if recognized == True:
            if phrase == "next":
                data = "2\n"
            elif phrase == "select":
                data = "3\n"
            else:
                data = "0"
                print(phrase + "\n")
            if data != "0":
                print(self.client_socket)
                print(data)
                #self.client_socket.send(data)

    def init_client_socket(self): # ip='localhost', port=4775):
        #client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #client_socket.connect((ip, port))
        self.client_socket = "dummy"
        return self.client_socket

    #def send_msg_over_socket():
        #client_socket.send(data)


#def init_client_socket(ip='localhost', port=4775):
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect(('localhost', 4775))
#     return client_socket


# def send_msg_over_socket(client_socket, data):
#     client_socket.send(data)
'''def check_for_continuation():
    answer = str(input("Continue? y/n "))
    if answer == "y":
        run = True
    else:
        run = False
    return run'''

if __name__ == "__main__":

    s2t = Speech2Text()
    #run = True
    #while run == True:

    stop_listening = s2t.listen()

        #run = check_for_continuation()



#    client_socket = init_client_socket()



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