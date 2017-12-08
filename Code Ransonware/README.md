# About

This code is the version 2.1 of the ransomware. To use it, you will need :

* Python version 3
* A machine acting as a server
* A victim machine

You will need also those libraries :

* pip install cryptography
* pip install cx-freeze


This code will be improve to add new features like :

* Improve the code in general

# Notes 

* This ransomware uses a multi-threading system to improve the encrypting process
* The connection between the client and the victim is encrypted with a TLS socket
* The encrypt files are lost if the key is not the right one
* To avoid some issues with the GUI (Tkinter module), you will need to add two DLL files at the root folder "tcl86t.dll" and "tk86t.dll". Their paths must be specify in the setup.py file.
* An icon is necessary. You will need to add it in the new folder (created by setup.py) and name it "icon.ico"

# Adding new features

* Encrypting external HDD files
* Creating multiple registry keys (Persistence)
* Removing the key from memory (unfortunately, you need to reboot the machine for that. It will be improved later)