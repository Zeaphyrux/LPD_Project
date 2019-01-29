#!/usr/bin/python

from Crypto.PublicKey import RSA
from Crypto import Random


global public_key, private_key




def generateKeys():
    random_generator = Random.new().read

    key = RSA.generate(4096, random_generator)
    
    global public_key, private_key
    public_key = key.publickey().exportKey()
    private_key = key.exportKey()


#export key. Specify key
# 'public', 'private' or 'both'
#filename, 0 if print to screen
def exportKey(key, filename):
    if key == 'public':
        if filename==0:
            print(public_key)
        else:
            file = open(filename+'.pem', 'wb')
            file.write(public_key)
            file.close()
    elif key == 'private':
        if filename==0:
            print(private_key)
        else:
            file = open(filename+'.pem', 'wb')
            file.write(private_key)
            file.close()
    elif key == 'both':
        if filename == 0:
            print(private_key)
            print(public_key)
        else:
            file = open("RSApublic_"+filename+'.pem', 'wb')
            file.write(public_key)
            file.close()
            file = open("RSAprivate_"+filename+'.pem', 'wb')
            file.write(private_key)
            file.close()
    else:
        print "Incorrect parameters"

def run(filename):
    generateKeys()
    exportKey('both', filename)


def main():
    generateKeys()
    exportKey('both', 'Key')

if __name__ == '__main__':
    main()



