import socket
from _thread import *
from player import Player
import pickle

server_ip="172.20.10.4"
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try :
    s.bind((server_ip,port))


except socket.error as e:
    str(e)  



s.listen(2) #allow only 2 people
print("Waiting for connection, Server Started")




players = [Player(0,0,50,50,(255,0,0)),Player(100,100,50,50,(0,0,255))]
def threaded_client(conn,player) :
    conn.send(pickle.dumps(players[player]))
    reply = " "
    while True:
        try :
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data :
                print("Disconnected")
                break
            else :
                if player == 1:
                    reply = players[0]

                else :
                    reply = players[1]
                print("Recieved : ", data)
                print("Sending : ",reply)
            conn.sendall(pickle.dumps(reply))
        except :
            break        
    print("Loss Connection")
    conn.close()


current_player = 0
while True :
    conn, addr = s.accept()

    print("Connected to :" , addr)
   
    start_new_thread(threaded_client, (conn,current_player))
    current_player += 1



