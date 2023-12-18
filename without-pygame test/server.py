import socket
import threading

header = 64
server = "192.168.1.4"
port = 5050
addr = (server, port)
format = 'utf-8'
disc_msg = 'Disconnect'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)

player_count = 0
players = {}

def handle_client(conn, addr):
  print(f"New Connection {addr} connected")
  connected = True
  while connected:
    msg_length = conn.recv(header).decode(format)
    if msg_length:
      msg_length = int(msg_length)
      msg = conn.recv(msg_length).decode(format)
      if msg == disc_msg:
        del_player = players.pop(addr)
        connected = False
        global player_count
        player_count -= 1
      try:
        print(f"[Player {players[addr]}]: {msg}")
      except: 
        print(f"[Player {del_player}]: {msg}")
  conn.close()

def start():
  s.listen(2)
  while True:
    conn, addr = s.accept()
    global player_count
    player_count += 1
    players[addr] = player_count
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f" ACTIVE THREADS: {threading.activeCount() - 1}")

print("Server starting")
start()