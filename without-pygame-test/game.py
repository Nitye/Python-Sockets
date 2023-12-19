from player import Player

class Game():
  def __init__(self, player_names, bank, id):
    self.num_players = len(player_names)
    self.player_names = player_names
    self.bank = bank
    self.id = id
    self.players = {}