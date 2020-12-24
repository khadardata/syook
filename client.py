import socket
import json

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.5" #replace this with ur socket server's IP
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    msg=client.recv(2048).decode(FORMAT)
    msg=json.loads(msg)
    gd=msg["gd"]
    print(f"{gd[0]}-{gd[1]}-{gd[2]}\n{gd[3]}-{gd[4]}-{gd[5]}\n{gd[6]}-{gd[7]}-{gd[8]}\n {msg['m']}")

connected=True
print("Welcome to Tic Tac Toe game!!!")
while connected:
    print("Pls press 1-9 or Press C to Close the connection")
    txt=input()
    if txt=="C":
        send(DISCONNECT_MESSAGE)
        connected=False
    else:
        send(txt)
    

