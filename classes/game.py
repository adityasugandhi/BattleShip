

from .Users import Users

from .missiles import Missile

from .fire import Fire


class Game:
    def __init__(self):
        self.players = []
        self.turn = 0

    
    def add_player(self, player):
        self.players.append(player)
        print(f"Player {player.username} added to the game.")
        print(f"Total players: {len(self.players)}")
    
    def get_opponent(self):
        return self.players[1] if self.turn == 0 else self.players[0]
        print(f"Opponent: {self.get_opponent().username}")
        print(f"Current player: {self.players[self.turn].username}")
    
    def current_player(self):
        return self.players[self.turn]
    
    def next_turn(self):
        self.turn = 1- self.turn
        print(f"Next turn: {self.players[self.turn].username}")


    def attack(self):
        """
        Launch a missile and try to hit an enemy ship.
        """

        attacker = self.current_player()
        defender = self.get_opponent()
        print(f"Attacker: {attacker.username}, Defender: {defender.username}")

        if attacker.setCoordinates():
            print("Coordinates set successfully.")
            
        else:
            print("Failed to set coordinates.")
            return False
        
        print(attacker.loadMissile.x, attacker.loadMissile.y)   

        # Create fire instance and attack
        fire = Fire(attacker.loadMissile, defender.ship)
        hit  = fire.hit()

        if hit:
            print(f"🔥 HIT! {attacker.username} struck {defender.username}'s ship at {coords}!")
        else:
            print(f"💨 MISS! {attacker.username} missed!")
