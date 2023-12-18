import socket
from _thread import *
import pickle

server = "192.168.1.4"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.bind((server, port))
except socket.error as e:
  print(e)

s.listen()
print('Waiting for connection')

def threaded_client(conn):
  conn.send(str.encode('test_1'))
  reply = ""
  while True:
    try:
      data = conn.recv(2048).decode()
      reply = data.decode('utf-8')

      if not data:
        print('Disconnected')
        break
      else:
        reply = 'working'

        print("Received: ", data)
        print('Sending: ', reply)

      conn.sendall(str.encode(reply))
    except:
      break

  print('Lost connection')
  conn.close()


while True:
  conn, addr = s.accept()
  print('Connected to: ',  addr)

  start_new_thread(threaded_client, (conn, ))