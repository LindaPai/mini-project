# This is the file to call class function
import movie   # import the class defination file name
import website

# Create 1 movie trailer as glass
glass = movie.Movie(movie_title = "Glass", movie_storyline = "Security guard David Dunn uses his supernatural abilities to track Kevin Wendell Crumb, a disturbed man who has twenty-four personalities."
, poster_image = "https://m.media-amazon.com/images/M/MV5BMTY1OTA2MjI5OV5BMl5BanBnXkFtZTgwNzkxMjU4NjM@._V1_SY1000_SX700_AL_.jpg",
trailer_youtube = "https://youtu.be/95ghQs5AmNk")  
 # use movie file to do class Movie() function


# Create another movie trailer as instant family
instant_family = movie.Movie("Instant Family", "A couple find themselves in over their heads when they foster three children.",
"https://m.media-amazon.com/images/M/MV5BMTkzMzgzMTc1OF5BMl5BanBnXkFtZTgwNjQ4MzE0NjM@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://youtu.be/IUfZq3DUd3Y")

bohemian = movie.Movie("Bohemian Rhapsody", "The story of the legendary rock band Queen and lead singer Freddie Mercury, leading up to their famous performance at Live Aid (1985).",
"https://m.media-amazon.com/images/M/MV5BMTA2NDc3Njg5NDVeQTJeQWpwZ15BbWU4MDc1NDcxNTUz._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://youtu.be/mP0VHJYFOAU")

survivor = movie.Movie("Designated Survivor","A low-level Cabinet member becomes President of the United States after a catastrophic attack kills everyone above him in the line of succession.",
"https://m.media-amazon.com/images/M/MV5BMjUxODc2NTIxMl5BMl5BanBnXkFtZTgwMjgxMDkyMzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://youtu.be/N_f1v0Nx5Sw")


movies = [glass, instant_family, bohemian, survivor]
website.open_movies_page(movies)