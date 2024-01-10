from pyais.stream import UDPStream

host = "127.0.0.1"
port = 9094

for msg in UDPStream(host, port):
    message = msg.decode()
    print(message)
