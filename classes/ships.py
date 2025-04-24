import random

# One-liner random coordinate generator
random_coord = lambda w, h: (random.randint(0, w-1), random.randint(0, h-1))


class Ships:
    def __init__(self, fleet_size=5):
        self.fleet_size = fleet_size
        self.ships = []
        self.ships_remaining = 0

    def validate_coordinates(self, coordinates):
        if coordinates is None:
            return random_coord(10, 10)
        if isinstance(coordinates, tuple) and len(coordinates) == 2:
            return coordinates
        raise ValueError("Coordinates must be a tuple of (x, y).")

    def add_ship(self, size=1, coordinates=None):
        if len(self.ships) >= self.fleet_size:
            raise ValueError("Cannot add more ships than the size of the fleet.")

        ship_id = len(self.ships) + 1
        validated_coords = self.validate_coordinates(coordinates)
        ship_info = {
            "id": ship_id,
            "size": size,
            "coordinates": validated_coords,
            "lifetime": 100
        }
        self.ships.append(ship_info)
        self.ships_remaining += 1
        return ship_info


    def get_size(self, ship_id):
        for ship in self.ships:
            if ship["id"] == ship_id:
                return pow(ship["size"]**2, 2) 
        raise ValueError("Invalid ship ID.")
                
    def remove_ship(self, ship_id):
        for ship in self.ships:
            if ship["id"] == ship_id:
                self.ships.remove(ship)
                self.ships_remaining -= 1
                return
        raise ValueError("Ship not found in the fleet.")

    def get_coordinates(self, ship_id):
        for ship in self.ships:
            if ship["id"] == ship_id:
                return ship["coordinates"]
        raise ValueError("Invalid ship ID.")

    def get_ships(self):
        return self.ships
