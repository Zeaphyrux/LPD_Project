#!/usr/bin/python
'''Read logs from txt file and get important information'''





#Opens file and returns and array, each line is an element
def getInfo(filename):
    #open in read mode and split by line
    f = open(filename, 'r').read().split('\n')
    
    #first line example
    #print f[0]
    
    return f

#Takes a line as argument, returns source ip
#Returns 0 if SRC=  ip wasnt found in line
def getSrcIp(line):
    #Split line by spaces
    temp = line.split(' ')
    #Source ip is element 15
    ip=0
    #Check for substring 'SRC=' in the elements of our line
    for i in range(len(temp)):
        if 'SRC=' in temp[i]:
            ip = temp[i]
            break
    if ip==0:
        return 0
    #O ip e "SRC=10.0.0.1" e nos so queremos o ip. Entao
    #vou cortar os primeiros 4 carateres q nao nos interessam
    #com o [4:]
    return ip[4:] 


'''loops through all the lines and gets the SRC ip from it, returns a list of ips'''
def getAllSrcIp(info):
    #Save ips here
    ips = []
    #loop through all lines to get src ips
    for i in range(len(info)):
    #meter na lista ips com o append, o src ip a usar a funcao
    #de cima do elemento info(q e o ficheiro dividido por linhas)
    # i
        tempIp = getSrcIp(info[i])
        #Tava a dar erro q as vezes nao encontra o ip na linha. Entao quando nao 
        #encontra tem o valor 0 e nao o acrescenta a lista
        if tempIp != 0:
            ips.append(tempIp)

    return ips

#Get time and dates

def getDate(line):
    months = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 
    'Sep', 'Oct', 'Nov', 'Dec']
    line  = line.split(' ')

    #for i in range(len(months)):
    #    if(month==months[i]):
   # print line[2]
    date = [line[0], line[1], line[2] ]

    return date

def getAllDate(info):
    dates = []
    for i in range(len(info)):
        if len(info[i].strip()) == 0 :
            pass
        else:
            tempDate = getDate(info[i])
        #print "appended ",tempDate

            dates.append(tempDate)
    return dates


#Function to run the full program
def run(filename):
    #info = getInfo(filename)
    #sourceIps = getAllSrcIp(info)
    
    #print sourceIps
    info = getInfo(filename)
    dates = getAllDate(info)
    print dates
def main():
    run('ufw.log')







#Isto serve para poder correr o ficheiro sozinho ou
# importalo para outro script de python
if __name__=='__main__':
    main()
