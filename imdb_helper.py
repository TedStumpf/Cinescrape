#   imdb_helper.py
#   A helper class for the IMDB API
#   https://imdbpy.sourceforge.io/     (pip install imdbpy)
import imdb

class IMDb_Movie():

    def __init__(self, movie_name):
        dbobj = imdb.IMDb()
        extra_info = ['awards', 'critic reviews', 'external reviews', 'full credits', 'keywords', 'main', 'quotes', 'release dates', 'release info']
        
        search_result = dbobj.search_movie(movie_name)
        if (len(search_result) > 0):
            self.movie = search_result[0]
            dbobj.update(self.movie, info = extra_info)
        else:
            self.movie = None

    def get_director_names(self):
        pass

    def get_full_title(self):
        pass

    def get_actors(self):
        pass

    def get_release_info(self):
        pass

    def get_ratings(self):
        pass

def get_movie_list(movie_name, count = 5):
    pass