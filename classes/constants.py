


class Const:

    
    def __init__(self):
        self._map_size = 10

    @property
    def MAP_SIZE(self):
        return self._map_size
    

    @MAP_SIZE.setter
    def MAP_SIZE(self, value):
        if value > 0:
            self._map_size = value
        else:
            raise ValueError("MAP_SIZE must be a positive integer.")
