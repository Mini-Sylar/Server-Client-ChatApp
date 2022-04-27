import socket
import threading

'''Enter your own ip address as HOST or the server's ip address and PORT'''
HOST = '127.0.0.1'  # Enter your own ip address here (find with ipconfig)
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()
clients = []
nicknames = []

def broadcast(message):
    '''This function sends a message to all the connected clients'''
    for client in clients:
        client.send(message)


def handle(client):
    '''This function handles individual connections to the client, it sends it to the main window'''
    while True:
        try:
            message = client.recv(8192)
            log_message = str(message)
            print(f"{nicknames[clients.index(client)]} says {log_message.split(':')[-1]}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} Disconnected from the server!\n".encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    '''This function accepts new connections (waits for new connections)'''
    while True:
        client, address = server.accept()
        print("Connected with ", str(address))

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(8192).decode('utf-8')

        nicknames.append(nickname)
        clients.append(client)
        displayNick  = ",".join(nicknames)

        print("Nickname of the client is ", nickname)
        broadcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        # Display Nicknames without bracket here
        client.send(f"({displayNick})\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is running...")
receive()
