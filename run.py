#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Run function for the project'''
import hashlib
import sys
sys.path.insert(0, 'scripts')
import projeto
import settings

CONFIG_PATH='.config'
#md5sum = '94be50752bbc34c88def6183d0217ba1'
md5sum = "2fe04e524ba40505a82e03a2819429cc"
#sha1sum = '3b404cfa745ac4118f5b322bedc2fc22af71e7a9'
sha1sum = "793f970c52ded1276b9264c742f19d1888cbaf73"



def main():
    settings.init()
    a = settings.getLogin()

    if settings.getLogin():
        if checkPass():
            projeto.main()
    else:
        projeto.main()



#Checks password. Returns True if correct, false otherwise
def checkPass():
    while True:
        input = raw_input("Enter the password pretty please:\n")
        if hashlib.md5(input).hexdigest() == md5sum:
            if hashlib.sha1(input).hexdigest() == sha1sum:
                print "Welcome!\n"
                return True
        else:
            print "Wrong password"  
            return False
                
                
if __name__=='__main__':
    main()
