#!/usr/bin/python

import RSA
import sys
import hashlib


#password in SHA1
password = "05c43a9166a79bc793c1ef0707642df0f605ae9a0bf9937610015f1b3853f0f3d079cb458b9283c12ea4dd8457d7682b96ecd6b96e6705c8a1cf499972f88900"


def checkPassword():
    for key in range(3):
        #get the key
        p = raw_input("Enter the password >>")
        #make an md5 object
        mdpass = hashlib.sha512(p)
        #hexdigest returns a string of the encrypted password
        if mdpass.hexdigest() == password:
            #password correct
            return True
        else:
            print 'wrong password, try again'
    print 'you have failed'
    return False

def main():
    if checkPassword():
        print "Password Correct!"
        RSAprivate_key = raw_input( "Please provide the RSA private key file")

        #continue to do stuff

        
        #############
        #Aqui o run do script
    else:
        sys.exit()

if __name__=='__main__':
    main()
