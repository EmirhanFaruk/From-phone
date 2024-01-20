import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection at " + str(server_ip))

currentId = "0"
pos = ["0:50,50,0,0,0,0", "1:100,100,0,0,0,0"]
def move_player(pos, rep, vel):
    liste = [0, 0, 0, 0, 0, 0]
    print("--------------------------")
    print(rep)
    print(pos)
    print("--------------------------")
    p1, p2 = int(pos[2]), int(pos[3])
    if rep[2] == "1":
        p1 = p1 + vel
    if rep[3] == "1":
        p1 = p1 - vel
    if rep[4] == "1":
        p2 = p2 + vel
    if rep[5] == "1":
        p2 = p2 - vel
    return [pos[:2], str(p1), str(p2), pos[4:]]
def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        #try:
        data = conn.recv(2048)
        reply = data.decode('utf-8')
        if not data:
            conn.send(str.encode("Goodbye"))
            break
        else:
            print("Recieved: " + reply)
            arr = reply.split(":")
            id = int(arr[0])
            
            reply = move_player(pos[id][:], reply, 3)

            if id == 0: nid = 0
            if id == 1: nid = 1
            
            reply = "".join(reply)
            print("Sending: " + reply)

        conn.sendall(str.encode(reply))
        #except Exception as e:
        #    print(e)
        #    break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))
