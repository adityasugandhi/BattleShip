


class Missile:
    def __init__(self):
        self.x = -1
        self.y = -1
       

    def setCoordinates(self, coords):
        self.x,self.y = coords
        
        return True

    def getCoordinates(self):
        return self.x, self.y