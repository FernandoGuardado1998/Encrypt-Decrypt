#!/usr/bin/python3

import os
import os.path
from os import path
from cryptography.fernet import Fernet

#Generates a brand new key
def GenerateNewKey():
    new_key = Fernet.generate_key()
    with open("YourKey.key", "wb") as key_file:
        key_file.write(new_key)

#Reads the .key file and loads the key
def LoadKey():
    fnet_key = open('YourKey.key','rb').read()
    return fnet_key

#Encrypts the word list
def Encrypt(e_fnet_key,wordlist):
    fnet = Fernet(e_fnet_key)
    with open(wordlist, 'rb') as file:
        text = file.read()

    with open(wordlist, 'wb') as file:
        file.write(fnet.encrypt(text))


def Decrypt(d_fnet_key, wordlist):
    fnet = Fernet(d_fnet_key)
    with open(wordlist, "rb") as file:
        text = file.read()

    with open(wordlist, "wb") as file:
        file.writelines(fnet.decrypt(text))

def main():
    print("Encrypt/Decryption System\n")

    wl_dir = input('Enter your directory to wordlist: ')

    if wl_dir == "":
        print('You must enter the directory of you word list')
    else:
        options = input("1. Encrypt\n"+
        "2. Decrpyt\n")


        if options == 1:
            if path.isdir(wl_dir):

                #Checks to see if the key exists
                if path.exists("YourKey.key"):
                    print('word list has already been encrypted')
                else:
                    GenerateNewKey()
                    key = LoadKey()
                    Encrypt(key,wl_dir)
                    print("New key has been generated and word list has been encrypted")

        elif options == 2:
            key = LoadKey()
            Decrypt(key,wl_dir)
            print("Word list has been decrypted")
   
if __name__ == "__main__":
    main()