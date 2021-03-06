# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!s

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

# title, trailer_youtube_url, poster_image_url variables defined here
fight_club = media.Movie(title="fight club", trailer_youtube_url='https://www.youtube.com/watch?v=SUXWAEX2jlg', poster_image_url='http://www.flore-maquin.com/wp-content/uploads/Fight_club_RVB_72.jpg')
thirteenth_floor = media.Movie(title="thirteenth floor", trailer_youtube_url='https://www.youtube.com/watch?v=dtYdZkPmFoU', poster_image_url='https://www.blendernation.com/wp-content/uploads/2014/10/original-12.jpg')
saw_seven = media.Movie(title="saw seven", trailer_youtube_url='https://www.youtube.com/watch?v=V1IwmygKN6c',poster_image_url='http://images4.fanpop.com/image/photos/21100000/Saw-VII-saw-3d-21148802-718-1111.jpg')
matrix = media.Movie(title="matrix", trailer_youtube_url='https://www.youtube.com/watch?v=m8e-FF8MsqU',poster_image_url='https://images-na.ssl-images-amazon.com/images/I/51FhdGyJ6DL._SY450_.jpg')



movies = [fight_club,thirteenth_floor,saw_seven,matrix]
fresh_tomatoes.open_movies_page(movies)

