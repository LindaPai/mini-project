
import webbrowser
# Create customize class call as Movie
# Use class defination as 1 file, call class function as other file
class Movie():
# Function named __init__ is called; it initializes or creates space in memory for new instance "self"
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
# define show_trailer function to open url at webbrowser
    def show_trailer(self):
# To be able use webbrowser function need to import it
        webbrowser.open(self.trailer_youtube_url)