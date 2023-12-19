import socket
import pickle

class Client:
  def __init__(self):
    self.header = 64
    self.server = "192.168.1.4"
    self.port = 5050
    self.addr = (self.server, self.port)
    self.format = 'utf-8'
    self.disc_msg = 'Disconnect'
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.client.connect(self.addr)
    self.player = pickle.loads(self.client.recv(2048))
    print(self.player.name, self.player.bank)

  def send(self, msg):
    message = msg.encode(self.format)
    msg_length = len(message)
    send_length = str(msg_length).encode(self.format)
    send_length += b' ' *  (self.header - len(send_length))
    self.client.send(send_length)
    self.client.send(message)

c = Client()
while True:
  msg = input('Enter message: ')
  c.send(msg)