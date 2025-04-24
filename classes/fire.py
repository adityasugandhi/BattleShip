class Fire:
    def __init__(self, missile, ships):
        self.missile = missile
        self.ships = ships
        self.x, self.y = missile.x, missile.y
        self.size = 1
        self.color = (255, 0, 0)  # Red
        self.lifetime = 100

    def check_hit(self, ship):
        # Hit if fire's (x, y) matches the ship's coordinate
        coord = ship["coordinates"]
        if (self.x, self.y) == coord:
            return True
        return False

    def hit(self):
        for ship in self.ships.get_ships():
            if self.check_hit(ship):
                print(f"Ship {ship['id']} hit at ({self.x}, {self.y})!")
                ship["lifetime"] -= 50  # Simulated "hit" effect
                return True
        return False
