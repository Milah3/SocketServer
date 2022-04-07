import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = '10.157.71.147' or socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)
print(f'[{SERVER}] Client connected')

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))  
    
    client.send(send_length)
    client.send(message)

    print(client.recv(HEADER).decode(FORMAT))

send('Testing')
send('Testing')
send('1')
send('2')
send('3')
send(DISCONNECT_MESSAGE)



    












