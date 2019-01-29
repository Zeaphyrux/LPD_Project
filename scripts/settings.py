#!/usr/bin/python


CONFIG_PATH='.config'


CONFIGS = {}

def readConf():    
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


#initalize confs
def init():
	global CONFIGS
	

	readConf()
	#print CONFIGS
    

def main():
	init()


if __name__=='__main__':
	main()


 