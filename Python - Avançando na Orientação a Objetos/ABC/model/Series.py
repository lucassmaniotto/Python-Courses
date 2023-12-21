from model.Midia import Midia

class Series (Midia):
    def __init__(self, title, year, seasons, likes = 0):
        super().__init__(title, year, likes)
        self.seasons = seasons

    def __str__(self):
        return f'{self.title} - {self.year} - {self.seasons} seasons - {self.likes} likes'