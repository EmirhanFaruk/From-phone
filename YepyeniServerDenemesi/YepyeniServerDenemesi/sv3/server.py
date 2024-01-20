#https://www.youtube.com/watch?v=YwWfKitB8aA
import socket

HOST = '192.168.0.13'#socket.gethostbyname(socket.gethostname())#ip adresini seç
PORT = 10422

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#SOCK_STREAM = tcp
#SOCK_DGRAM = udp

server.bind((HOST, PORT))

server.listen()

while True:
    communication_socket, adress = server.accept()
    print(f"Connected to {adress}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
    communication_socket.send(f"Got your message! Thank you!".encode('utf-8'))
communication_socket.close()
print(f"Connection with {adress} ended!")
