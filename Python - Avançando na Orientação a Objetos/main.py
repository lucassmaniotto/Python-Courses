from model.Series import Series
from model.Movie import Movie

fight_club = Movie('fight club', 1999, 139)
cowboy_bebop = Series('cowboy bebop', 1998, 26)

movies_and_series = [fight_club, cowboy_bebop]

for program in movies_and_series:
    print(program)
