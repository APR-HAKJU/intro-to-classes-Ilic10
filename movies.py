movie_1 = ["Horror" , "It", 2017 , 135]
movie_2 = [ "Fantasy" , "Harry Potter" , 1997, 97 , ]

print(f"Titel des Films: {movie_1[1]}")
print(f"Title des Films: {movie_2[1]}")

class Movie:    # Klassen = Bauplan für ein thema
    def __init__(self, title, genre, duration, release_year): # Konstruktor -> Wird immer aufgerufen, 
                         # wenn ein neues Objet erstellt wird
        self.title ="Default"
        self.genre =""
        self.duration= 0
        self.release_year = 0
        print("Neuer Film wurde erstellt!")

# movie_3 = Movie() #erstellt uns ein Objekt nach dem Bauplan "Movie"
# movie_4 = Movie()
# movie_5 = Movie()

# movie_3.title = "Real Steel"
# print(f"Titel des Filmes:{movie_3.title}")

# movie_3.genre = "Action"
# movie_3. duration = 120
# movie_3.release_year = 2015

# movie_4.title = "From Dusk til Dawn"
# movie_4.genre =  "Action"
# movie_4.duratioon = 120
# movie_4.release_year = 1990

movie_6 = Movie(title= "Dune: Awakening", genre="Sci-Fi", duration=180, release_year=2020)
print(f"Titel des Filmes:{movie_6.title}")

movie_7= Movie(title="Drama", duration=125, release_year=2023)
print(f"{movie_7.title} wurde i Jahr {movie_7.release_year} herausgebracht!")

