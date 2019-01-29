#!/usr/bin/python

import RSA
import os

#True for Encrypt, False for Decrypt
mode = False
Forbidden = ['RSA.py', 'encrypt.py', 'login.py', 
'RSApublic_Key.pem', 'RSAprivate_Key.pem']
path = os.getcwd()
keyPath1 = path+'/RSApublic_Key.pem'
keyPath2 = path+'/RSAprivate_Key.pem'

#Encrypts or decrypts recursevile
def run(mode):

    flag = False
    while True:
        if(flag):
            break
        flag = True
        files = os.listdir(os.getcwd())
        print files
        #get common elements
        files = [i for i in files if i not in Forbidden]
        print files

        for i in range(len(files)):
            if(os.path.isfile(files[i])):
                if(mode):
                    RSA.runEncrypt(files[i], keyFile=keyPath1)
                else:
                    if(files[i].endswith('.crypt')):
                        RSA.runDecrypt(files[i], keyFile=keyPath2)
                    else:
                        pass
            elif(os.path.isdir(files[i])):
                os.chdir(files[i])
                print "dir"
                flag = False
            else:
                pass
def EnDecript(mode, file):

    if(mode):
        RSA.runEncrypt(file, keyfile=RSA_KEY_PUBLIC)
    else:
        RSA.runDecrypt(file, keyFile=RSA_KEY_PRIVATE)


def main():
   
    run(False)




if __name__=='__main__':
    main()