#!/usr/bin/python
import sys
from Crypto.PublicKey import RSA
from subprocess import Popen
import base64

import settings


DEFAULT_BLOCK_SIZE = 128
BYTE_SYZE = 256
global KEY_PUBLIC
global KEY_PRIVATE
FILE_TO_ENCRYPT = 'teste.py'
FILE_TO_DECRYPT = 'teste.py.crypt'

    
#get files
def getFileToEncrypt(filenameEncrypt=FILE_TO_ENCRYPT):
    f = open(filenameEncrypt, 'r').read()
    return f
def getFileToDecrypt(filenameDecrypt=FILE_TO_DECRYPT):
    f = open(filenameDecrypt, 'r').read()
    return f

#Encrypts message
def encrypt(message, keyObj):
    '''Gets message, splits into blocks, encripts each block
    and returns encripted blocks'''
    #get message to encrypt
    #message = getFileToEncrypt()
    
    #split into blocks
    blocks = getBlocksFromText(message)
    
    encrypted_blocks = []
    for i in range(len(blocks)):
        encrypted_blocks.append(keyObj.encrypt(blocks[i], 32))
     
    #print encrypted_blocks[0]
    
    return encrypted_blocks
    #Popen(['rm', filename])


#Decrypts file. Filename to decrypt, keyFile for the private key. if none specified will use default on folder
def decrypt(blocks, keyObj):
    '''Gets message, splits into blocks, decrypts each block and
    returns the decripted blocks'''
    encripted = blocks
    decrypted_blocks = []
    

    for i in range(len(encripted)):
        
        decrypted_blocks.append(keyObj.decrypt(encripted[i]))
        

    
    decripted = getTextFromBlocks(decrypted_blocks)
    
    return decripted
#Write decripted data to file
def writeDecripted(message, filename):
    #remove '.crypt' from filename
    filename1 = filename[:-6]
    foo = open(filename1, 'w')
    foo.write(message)
    foo.close()
    Popen(['rm', filename])

#Write encrypted data to file
def writeEncripted(blocks, filename):
    filename1 = filename
    filename1+='.crypt'
    f = open(filename1, 'w')
    for i in range(len(blocks)):
        f.write(str(blocks[i][0])+'\\*/')
    Popen(['rm', filename])
    f.close()
#Read blocks from file
def readFileBlock(filename=FILE_TO_DECRYPT):
    f = open(filename, 'r').read()
    f = f.split('\\*/')
    return f

def getBlocksFromText(message,b64=True, blockSize = DEFAULT_BLOCK_SIZE):
    '''Get string, converts to b64 and splits in blocks of blocksize'''
    #String to b64
    if(b64):
        messageBytes = base64.b64encode(message)
    else:
        messageBytes = message

    blocks = []
    for blockStart in range((len(messageBytes) // DEFAULT_BLOCK_SIZE)+1 ):

        blockInt = ''
        for i in range(DEFAULT_BLOCK_SIZE):
            if(len(messageBytes) > i+(blockStart*DEFAULT_BLOCK_SIZE)):
                blockInt += messageBytes[i+(blockStart*DEFAULT_BLOCK_SIZE)]
        blocks.append(blockInt)
    return blocks

def getTextFromBlocks(blocks, b64=True,blockSize=DEFAULT_BLOCK_SIZE):
    '''Get string from b64 blocks'''
    messageBytes = ''
    for blockStart in range(len(blocks)):
        messageBytes+=blocks[blockStart]
    
    #b64 to String
    if(b64):
        message = base64.b64decode(messageBytes)
    else:
        message = messageBytes
    return message
#Run function to encrypt file
def runEncrypt(filename, keyFile='RSApublic_Key.pem'):
    KEY_PUBLIC = RSA.importKey(open(keyFile, 'r'))
    print 'Encrypting file: '+filename
    fileToEncrypt = getFileToEncrypt(filenameEncrypt=filename)
    blocks = encrypt(fileToEncrypt, KEY_PUBLIC)
    del fileToEncrypt
    writeEncripted(blocks, filename)
#Run function to decrypt file
def runDecrypt(filename, keyFile='RSAprivate_Key.pem'):
    KEY_PRIVATE = RSA.importKey(open(keyFile, 'r'))
    print 'Decrypting file: '+filename
    fileToDecrypt = readFileBlock(filename=filename)
    decripted = decrypt(fileToDecrypt, KEY_PRIVATE)
    del fileToDecrypt
    writeDecripted(decripted, filename)

def main():
    settings.init()

    runEncrypt('teste.py')
    #runDecrypt('teste.py.crypt')

if __name__=='__main__':
    main()

