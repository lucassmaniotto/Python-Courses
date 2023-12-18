from model.Series import Series
from model.Movie import Movie
from model.Playlist import Playlist

from helpers.like_midia import like_midia

fight_club = Movie('fight club', 1999, 139)
cowboy_bebop = Series('cowboy bebop', 1998, 26)
blade_runner = Movie('blade runner', 1982, 117)
over_the_garden_wall = Series('over the garden wall', 2014, 10)

like_midia(fight_club, 30)
like_midia(cowboy_bebop, 27)
like_midia(blade_runner, 15)
like_midia(over_the_garden_wall, 30)

movies_and_series = [fight_club, cowboy_bebop, blade_runner, over_the_garden_wall]
to_watch = Playlist('to watch', movies_and_series)

for midia in to_watch:
    print(midia)
