# A Propos

Le code présent dans ce dossier est une alpha du ransonware. Il est sujet à certains bug.
Pour l'utiliser, il est nécessaire d'installer la bibliothèque Pycrypto et d'utiliser la version 2.7 de python.

* pip install pycrypto

* Pour éviter tous problèmes avec <a href="http://www.py2exe.org/index.cgi/FrontPage">Py2exe</a>, il est nécessaire d'installer les librairies comme stipuler ci-dessus ou avec la commande "easy_install.exe --always-unzip pycrypto". Py2exe ne supporte pas nativement les librairies aux formats .egg -> <a href="https://github.com/dlitz/pycrypto/issues/118">Py2exe and Pycrypto</a>

Ce code sera amélioré pour accueillir de nouvelles fonctionnalités.

* La suppression de la clé en mémoire

* La suppression réelle du fichier (le remplir de zéro par exemple)

* Développer le code de façon à évader les solutions antivirus

* Il est aussi nécessaire de chiffrer la connexion entre la machine victime et le serveur

* Améliorer le code d'une façon générale

* D'autres idées...
