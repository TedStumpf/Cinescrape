#   imdb_test.py
#   Tests imdb.py
import imdb_helper

#   Test 1 - Core functions
print("Testing for The Matrix")
test_movie = imdb_helper.IMDb_Movie('The Matrix')
directors = ['Lana Wachowski', 'Lilly Wachowski']
actors4 = [('Carrie-Anne Moss', 'Trinity'), ('Hugo Weaving', 'Agent Smith'), ('Keanu Reeves', 'Neo'), ('Laurence Fishburne', 'Morpheus')]
assert(test_movie.movie != None)
assert(test_movie.get_full_title() == 'The Matrix')
assert(test_movie.get_director_names() == directors)
assert(test_movie.get_actor_names(4) == actors4)
print("Test 1 complete")
