import socket
import asyncio

PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.gethostbyname(socket.gethostname())
s.connect((server, PORT))


async def receive():
    data = s.recv(1024).decode()
    print("Received: {}".format(data))


async def main():
    msg = input("Send: ").encode()
    s.sendall(msg)

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(main())
    asyncio.ensure_future(receive())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()
    print("closed")
