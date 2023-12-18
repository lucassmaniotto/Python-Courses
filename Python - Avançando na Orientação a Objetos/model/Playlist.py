class Playlist(list):
    def __init__(self, name, playlist):
        self.name = name
        super().__init__(playlist)
