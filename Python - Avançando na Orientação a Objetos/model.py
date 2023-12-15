class Midia:
    def __init__(self, title, year, likes = 0):
        self.__title = title.title()
        self.year = year
        self.__likes = likes

    def __str__(self):
        return f'{self.__title} - {self.year}'

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def likes(self):
        return self.__likes

    def like(self):
        self.__likes += 1


class Movie (Midia):
    def __init__(self, title, year, duration, likes = 0):
        super().__init__(title, year, likes)
        self.duration = duration

    def __str__(self):
        return f'{self.title} - {self.year} - {self.duration} minutes'
    
class Series (Midia):
    def __init__(self, title, year, seasons, likes = 0):
        super().__init__(title, year, likes)
        self.seasons = seasons

    def __str__(self):
        return f'{self.title} - {self.year} - {self.seasons} seasons'
    

movie = Movie('reservoir dogs', 1992, 99)
movie.like()
print(movie)
print(f'{movie.likes} likes')


series = Series('atlanta', 2018, 3)
series.like()
series.like()
print(series)
print(f'{series.likes} likes')