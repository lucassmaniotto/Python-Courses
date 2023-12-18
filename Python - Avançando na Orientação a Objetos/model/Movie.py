from model.Midia import Midia

class Movie (Midia):
    def __init__(self, title, year, duration, likes = 0):
        super().__init__(title, year, likes)
        self.duration = duration

    def __str__(self):
        return f'{self.title} - {self.year} - {self.duration} minutes - {self.likes} likes'