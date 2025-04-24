# main.py
from classes.Users import Users
from classes.game import Game
from classes.constants import Const


constants = Const()
constants.MAP_SIZE = int(input("Enter the map size: "))




player1 = Users(1, "Alice", "alice@example.com")
player2 = Users(2, "Bob", "bob@example.com")

player1.build_ship(size=2, coordinates=(2, 2))
player2.build_ship(size=2, coordinates=(4, 4))

game = Game()
game.add_player(player1)
game.add_player(player2)

# Run 3 attack rounds
for _ in range(3):
    game.attack()
