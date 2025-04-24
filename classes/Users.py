import random
from .ships import Ships
from .fire import Fire
from .missiles import Missile
from .constants import Const

N = Const().MAP_SIZE

class Users:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.ship = Ships()
        self.myships = []
        self.loadMissile = Missile()
        self.fire = None

    def __repr__(self):
        return f"User({self.user_id}, {self.username})"

    def setCoordinates(self):

        if N == 5:
            print("Map size is 5, coordinates are set to (0, 0)")

        x = random.randint(0, N // 2)
        y = random.randint(0, N // 2)
        if self.loadMissile.setCoordinates((x, y)):
            return True
        return False

    def build_ship(self, size, coordinates=None):
        self.ship.add_ship(size=size, coordinates=coordinates or self.random_coordinates())
        self.myships = self.ship.get_ships()

    def get_ships(self):
        return self.myships

    def get_ship(self, ship_id):
        for ship in self.myships:
            if ship["id"] == ship_id:
                return ship
        raise ValueError("Ship not found.")

    def destroy_ship(self, ship_id):
        for ship in self.myships:
            if ship["id"] == ship_id:
                self.ship.remove_ship(ship_id)
                self.myships = self.ship.get_ships()
                return
        raise ValueError("Ship not found.")

    
    def get_missile(self):
        if self.loadMissile:
            return self.loadMissile.x, self.loadMissile.y
        return None

    def get_fire(self):
        if self.fire:
            return self.fire.x, self.fire.y
        return None

    def get_lifetime(self, ship_id):
        ship = self.get_ship(ship_id)
        return ship["lifetime"]

    def get_color(self):
        return (255, 0, 0)  # Red

    def get_size(self):
        return 1  # Fire size

    def get_coordinates(self, ship_id):
        ship = self.get_ship(ship_id)
        return ship["coordinates"]
