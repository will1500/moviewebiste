# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self, *args, **kwargs):
    	# one star for args, two stars for keyword args
        # initialize instance of class Movie
        #  * star takes arguments no matter the number of them and returns all as array
        #self.title, trailer_youtube_url, and poster_image_url  initialized, will be defined in entertainment_center file. 
        self.title = kwargs['title']
        self.trailer_youtube_url = kwargs['trailer_youtube_url']
        self.poster_image_url = kwargs['poster_image_url']




