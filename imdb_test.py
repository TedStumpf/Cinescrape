#   imdb_test.py
#   Tests imdb.py
import imdb_helper

#   Test 1 - Core functions
print("Testing for The Matrix")
test_movie = imdb_helper.IMDb_Movie('The Matrix')
assert(test_movie.movie != None)
assert(test_movie.get_full_title() == 'The Matrix')
assert(test_movie.get_director_names() == ['Lana Wachowski', 'Lilly Wachowski'])
print("Test 1 complete")
