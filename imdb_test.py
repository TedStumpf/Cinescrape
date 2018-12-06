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
assert(test_movie.get_long_title() == 'The Matrix (1999)')
assert(test_movie.get_director_names() == directors)
assert(test_movie.get_actor_names(4) == actors4)
assert(test_movie.get_ratings() == 8.7)
assert(test_movie.get_release_info() == '31 Mar 1999 (USA)')
print("Test 1 complete")

print("Testing movie searching")
mov_list = imdb_helper.get_movie_list("Peter Pan")
movies = ['Peter Pan (2003)', 'Pan (2015)', 'Peter Pan (1953)', 'Amazon Women on the Moon (1987)', 'Peter Pan II: Return to Neverland (2002)']
title_list = [mov[0] for mov in mov_list]
assert(title_list == movies)
print("Test 2 complete")