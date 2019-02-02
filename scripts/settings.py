#!/usr/bin/python

# -*- coding: utf-8 -*-
'''
Configuration file. Reads '.config' file and sets certain configurations
'''
import os
CONFIG_PATH='.config'


CONFIGS = {}


def readConf():    
    '''
    Reads the configuration file
    '''
    global CONFIGS
    f = open(CONFIG_PATH, 'r')
    config = f.read()
    config = config.split('\n')
    #Loop through lines on config file and assign variables
    for i in range(len(config)):
        if config[i].startswith('RSA_KEY_PRIVATE_PATH='):
            CONFIGS["RSA_KEY_PRIVATE"] = config[i][len('RSA_KEY_PRIVATE_PATH='):]
        if config[i].startswith('RSA_KEY_PUBLIC_PATH='):
            CONFIGS["RSA_KEY_PUBLIC"] = config[i][len('RSA_KEY_PUBLIC_PATH='):]
        if config[i].startswith('DATABASE_FLAG='):
            CONFIGS["DATABASE_FLAG"] = config[i][len('DATABASE_FLAG='):]
        if config[i].startswith('DATABASE_PATH='):
            CONFIGS["DATABASE_PATH"] = config[i][len('DATABASE_PATH='):]
        if config[i].startswith('CSV_PATH='):
            CONFIGS["CSV_PATH"] = config[i][len('CSV_PATH='):]
        if config[i].startswith('PDF_PATH='):
            CONFIGS["PDF_PATH"] = config[i][len('PDF_PATH='):]
        if config[i].startswith('KEY='):
            CONFIGS["KEY"] = config[i][len('KEY='):]
        if config[i].startswith('LOGIN='):
            CONFIGS["LOGIN"] = config[i][len('LOGIN='):]

#Get keys for the configurations
def getKeyPrivate():
    return CONFIGS["RSA_KEY_PRIVATE"]
def getKeyPublic():
    return CONFIGS["RSA_KEY_PUBLIC"]
def getDatabase():
    return CONFIGS["DATABASE_FLAG"]
def getDatabaseStatus():
    return CONFIGS["DATABASE_PATH"]
def getCsv():
    return CONFIGS["CSV_PATH"]
def getPdf():
    return CONFIGS["PDF_PATH"]
def getKey():
    if os.path.exists(CONFIGS["KEY"]):
        f = open(CONFIGS["KEY"])
        f = f.read()
        print f
        return f
    else:
        return CONFIGS["KEY"]
def getLogin():
    if CONFIGS["LOGIN"] == 1:
        return True
    else:
        return False



#initalize confs
def init():
	global CONFIGS
	

	readConf()
	#print CONFIGS
    

def main():
	init()


if __name__=='__main__':
	main()


 