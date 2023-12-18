from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, title, year, likes=0):
        self._title = title.title()
        self.year = year
        self._likes = likes

    @abstractmethod
    def __str__(self):
        pass

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def likes(self):
        return self._likes

    def like(self):
        self._likes += 1
