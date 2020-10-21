import socket
import _thread

PORT = 8000
BUFSIZE = 1024
current_users = 0
connection_list = []


def threaded_user(_client):
    global connection_list, current_users
    connection_list.append(_client)
    while True:
        if current_users > 1:
            for sock in connection_list:
                if sock != _client:
                    other_client = sock
            data = other_client.recv(BUFSIZE).decode()
            print(data)
            _client.sendall(data.encode())


server = socket.gethostbyname(socket.gethostname())
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.bind((socket.gethostname(), PORT))
    except socket.error as e:
        print(str(e))
    s.listen(3)
    print("Server up and kicking. Waiting for connections.")
    while True:
        client, address = s.accept()
        connection_list.append(client)
        current_users += 1
        print("Connected to: {}".format(address))
        _thread.start_new_thread(threaded_user, (client,))
