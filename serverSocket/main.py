# This is a sample Python script.
import json
import pickle

import psutil

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket

# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# PORT = 65431        # Port to listen on (non-privileged ports are > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)
# import types
#
# host = '127.0.0.1'  # Standard loopback interface address (localhost)
# port = 65431  # Port to listen on (non-privileged ports are > 1023)
#
# import selectors
#
#
# def accept_wrapper(sock):
#     conn, addr = sock.accept()  # Should be ready to read
#     print('accepted connection from', addr)
#     conn.setblocking(False)
#     data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
#     events = selectors.EVENT_READ | selectors.EVENT_WRITE
#     sel.register(conn, events, data=data)
#
#
# def service_connection(key, mask):
#     sock = key.fileobj
#     data = key.data
#     if mask & selectors.EVENT_READ:
#         recv_data = sock.recv(1024)  # Should be ready to read
#         if recv_data:
#             data.outb += recv_data
#         else:
#             print('closing connection to', data.addr)
#             sel.unregister(sock)
#             sock.close()
#     if mask & selectors.EVENT_WRITE:
#         if data.outb:
#             print('echoing', repr(data.outb), 'to', data.addr)
#             sent = sock.send(data.outb)  # Should be ready to write
#             data.outb = data.outb[sent:]
#
#
# sel = selectors.DefaultSelector()
# # ...
# lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# lsock.bind((host, port))
# lsock.listen()
# print('listening on', (host, port))
# lsock.setblocking(False)
# sel.register(lsock, selectors.EVENT_READ, data=None)
#
# while True:
#     events = sel.select(timeout=None)
#     for key, mask in events:
#         if key.data is None:  # listening socket
#             accept_wrapper(key.fileobj)
#         else:
#             service_connection(key, mask)


import asyncio


async def service_server(reader, writer):
    print('connect to client')

    while True:
        data = await reader.read(100)  # Max number of bytes to read 100
        if not data:
            break
        print(repr(data.decode("UTF-8")))
    writer.close()


async def main(host, port):
    server = await asyncio.start_server(service_server, host, port)
    await server.serve_forever()


asyncio.run(main('127.0.0.1', 65431))
