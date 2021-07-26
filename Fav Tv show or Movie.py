# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:30:52 2021

@author: Royal
"""

#create a class
class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
    #importing os module
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = 'MP4'

#playing a video named my_video from the system
movie = Movie_MP4(r'E:\my_video.mp4')
movie.play()