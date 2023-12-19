import socket
import threading
import pickle
from player import Player
from game import Game

header = 64
server = "192.168.1.4"
port = 5050
addr = (server, port)
format = 'utf-8'
disc_msg = 'Disconnect'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)

player_names = ['n', 'p', 't']
game_id = 0
g = Game(player_names, 1000, game_id)

def handle_client(name):
  msg_length = g.players[name]['conn'].recv(header).decode(format)
  if msg_length:
    msg_length = int(msg_length)
    msg = g.players[name]['conn'].recv(msg_length).decode(format)
    if msg == disc_msg:
      g.players[name]['conn'].close()
      msg = 'Disconnected'
    print(f"[{name}]: {msg}")

def start():
  s.listen(3)
  while len(g.players) < g.num_players:
    conn, addr = s.accept()
    print(f"New Connection {player_names[0]} connected")
    g.players[g.player_names[0]] = dict()
    g.players[g.player_names[0]]['addr'] = addr
    g.players[g.player_names[0]]['conn'] = conn
    g.players[g.player_names[0]]['player_obj'] = Player(g.player_names[0], g.bank)
    conn.send(pickle.dumps(g.players[g.player_names[0]]['player_obj']))
    g.player_names.pop(0)
    # thread = threading.Thread(target=handle_client, args=(conn, addr))
    # thread.start()
    # print(f" ACTIVE THREADS: {threading.activeCount() - 1}")

print("Server starting")
start()
while True:
  for i in list(g.players.keys()):
    handle_client(i)