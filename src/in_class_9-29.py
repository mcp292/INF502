'''    A Movie needs to have a title, a genres (may be more than one), year, my review, a list of actors, and a watch counter (how many times I watched), borrowed (a flag - True/False - that says if this movie is currently with someone), borrower name.
    We can interact with a movie by:

    watching the movie (increase the counter),
    writing a review about the movie,
    set any of the fields (except flag, borrower, and counter, which are changed by different actions)
    borrowing the movie (set the borrower and change the flag)
    returning the moving (set borrower to "" and flag to False)
    list the details of the movie when printing it in the following format:

   Movie: The Godfather     Year: 1972
   Genre: Crime, Drama
   List of Actors:
       Marlon Brando
       Al Pacino
       Robert Duvall

    The list of actors, need to have objects of type Actor, which are composed of name, date_of_birth, and nationality. You should be able to:
        set the fields name, date_of_birth, and nationality.

CHALLENGE: change your classes to make it possible to list (from an object
actor) all the movies that the actor participated.
'''

class Movie:
    title = ""
    genres = []
    year = ""
    my_review = ""
    actors = []
    watch_counter = 0
    borrowed = False
    borrowed_by = ""

    def watch(self):
        self.watch_counter += 1
        
    def set_review(self, review):
        self.review = review
        
    def set_title(self, title):
        self.title = title
        
    def set_year(self, year):
        self.year = year
        
    def add_genre(self, genre):
        self.genre.append(genre)
        
    def add_actor(self, actor):
        self.actor.append(actor)
        
    def borrow_movie(self, borrowed_by):
        self.borrowed_by = borrowed_by
        self.borrowed = True
       
    def return_movie(self):
        self.borrowed_by = ""
        self.borrowed = False

    def get_details(self):
        print("Movie: {}\t{}".format(self.title, self.year))
        print("Genre: {}".format(self.genres))
        print("List of Actors:") 

        for actor in self.actors:
            print("\t{}".format(actor.name))


class Actor:
    name = ""
    date_of_birth = ""
    nationality = ""

    def set_name(self, name):
        self.name = name
        
    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

        def set_nationality(self, nationality):
            self.nationality = nationality
    
# CHALLENGE: change your classes to make it possible to list (from an object
# actor) all the movies that the actor participated.

# I would make it take in a list of movies

