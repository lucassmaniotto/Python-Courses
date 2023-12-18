class Midia:
    def __init__(self, title, year, likes = 0):
        self.__title = title.title()
        self.year = year
        self.__likes = likes

    def __str__(self):
        return f'{self.__title} - {self.year} - {self.__likes} likes'

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
