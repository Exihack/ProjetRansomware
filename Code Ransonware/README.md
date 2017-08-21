# A Propos

Le code présent dans ce dossier est la seconde version du ransonware.
Pour l'utiliser, il est nécessaire d'avoir :

* La version 3 de python
* Une machine servant de serveur
* Une machine victime

il faut aussi installer les bibliothèques suivantes :

* pip install cryptography
* pip install cx-freeze


Ce code sera amélioré pour accueillir de nouvelles fonctionnalités comme :

* La suppression de la clé en mémoire
* L'améliorer du code d'une façon générale

# Notes 

* le ransonware utilise un système de Threading pour accélérer le processus de chiffrement
* Les fichiers chiffrés sont totalement perdus si la clé de déchiffrement n'est pas bonne
* Pour éviter certains problèmes de compilations avec la GUI (module Tkinter), il faut deux fichiers DLL à la racine du dossier "tcl86t.dll" et  "tk86t.dll". Leurs chemins respectifs doivent être spécifiés dans le fichier "Setup.py"
* Une icone est aussi nécessaire. Après la compilation, il suffit de l'ajouter dans le dossier et la nommer "icone.ico"
