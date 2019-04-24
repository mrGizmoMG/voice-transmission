#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 03:07:53 2018

@author: Yeahia Sarker

"""

import socket
import pyaudio
import pickle
import sys

class nabvoice:
    def __init__(self):
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channel = 2
        self.rate = 44100
        self.record_seconds = 5
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.audio = pyaudio.PyAudio()

    def nab_server(self, host_ip, port):
        self.host_ip = host_ip
        self.port = port
        try:
            self.server.bind((host_ip, port))
        except Exception:
            print("Bind Error!")
            print("The receiver could not connect")
            print("Please check the host ip and port")
            self.server.close()
            sys.exit()
        print("Server side is ready. Waiting for connection.... " )
        print("Press ctrl + c to terminate the program")
        try:
            self.__base, addr = self.server.accept()
            print("Connection has been established")
            print('Got a connection from {}'.format(str(addr)))
        except KeyboardInterrupt:
            self.server.close()
            print("Connection has been terminated")
            sys.exit()
        def send_voice(self):
            stream = self.audio.open(format = self.format, channels = self.channels,
                rate = self.rate, input = True,
                frames_per_buffer = self.chunk)
            frame = []
            while True:
                try:
                    __data = stream.read(self.chunk)
                    frame.append(__data)
                    data = pickle.dump(__data)
                    stream.write(data)
                except KeyboardInterrupt:
                    stream.stop_stream()
                    stream.close()
                    self.audio.terminate()
                    print("Program is terminated")
                except:
                    pass
        
