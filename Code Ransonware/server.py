import socket
from os.path import expanduser

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
keys_file = expanduser("~") + "\\keys.txt"

socket.bind(('', 15555))

while True:
    socket.listen(5)
    client, address = socket.accept()
    print "{} connected".format( address )

    response = client.recv(255)
    if response != "":
            print response

    with open(keys_file, 'wb') as file:
        file.write(response)

print "Close"
client.close()
socket.close()
