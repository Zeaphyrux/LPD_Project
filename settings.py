#!/usr/bin/python


CONFIG_PATH='/home/z/Documents/uni/beja/LPD/Projecto/.config'




def readConf():    

    f = open(CONFIG_PATH, 'r')
    config = f.read()
    config = config.split('\n')
    #Loop through lines on config file and assign variables
    for i in range(len(config)):
        if config[i].startswith('RSA_KEY_PRIVATE_PATH='):
            CONFIGS["RSA_KEY_PRIVATE"] = config[i][len('RSA_KEY_PRIVATE_PATH='):]
        if config[i].startswith('RSA_KEY_PUBLIC_PATH='):
            CONFIGS["RSA_KEY_PUBLIC"] = config[i][len('RSA_KEY_PUBLIC_PATH='):]

#initalize confs
def init():
	global CONFIGS
	CONFIGS = {}

	readConf()
	#print CONFIGS
    

def main():
	init()


if __name__=='__main__':
	main()


 