class Playlist:
    def __init__(self, name, playlist):
        self.name = name
        self._playlist = playlist

    def __getitem__(self, item):
        return self._playlist[item]
       
    def __len__(self):
        return len(self._playlist)
 
    @property
    def list(self):
        return self._playlist