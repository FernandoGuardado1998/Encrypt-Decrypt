#!/usr/bin/env python3

import os
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
    options = input("1. Encrypt\n"+
    "2. Decrpyt\n")

    if options == 1:
        GenerateNewKey()
        key = LoadKey()
        Encrypt(key,'wordlist.txt')
        print("New key has been generated and word list has been encrypted")
    elif options == 2:
        key = LoadKey()
        Decrypt(key,'wordlist.txt')
        print("Word list has been decrypted")
   
if __name__ == "__main__":
    main()