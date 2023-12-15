class Movie:
    def __init__(self, title, year, duration, likes = 0):
        self.__title = title.title()
        self.year = year
        self.duration = duration
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
    

movie = Movie('reservoir dogs', 1992, 99)
movie.like()
print(f'{movie} - {movie.duration} minutes')
print(f'{movie.likes} likes')

class Series:
    def __init__(self, title, year, seasons, likes = 0):
        self.__title = title.title()
        self.year = year
        self.seasons = seasons
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

series = Series('atlanta', 2018, 3)
series.like()
series.like()
print(f'{series} - {series.seasons} seasons')
print(f'{series.likes} likes')