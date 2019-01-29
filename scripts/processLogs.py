#!/usr/bin/python
'''Read logs from txt file and get important information'''


import geoip
import sqlite
import settings
import sys
sys.path.insert(0, 'scripts')
import projeto

#Opens file and returns and array, each line is an element
def getInfo(filename, split=True):
    #open in read mode and split by line
    f = open(filename, 'r').read()
    if split:
        f = f.split('\n')

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

#Takes a line as argument, returns source ip
#Returns 0 if SRC=  ip wasnt found in line
def getDstIp(line):
    #Split line by spaces
    temp = line.split(' ')
    #Source ip is element 15
    ip=0
    #Check for substring 'SRC=' in the elements of our line
    for i in range(len(temp)):
        if 'DST=' in temp[i]:
            ip = temp[i]
            break
    if ip==0:
        return 0
    #O ip e "SRC=10.0.0.1" e nos so queremos o ip. Entao
    #vou cortar os primeiros 4 carateres q nao nos interessam
    #com o [4:]
    return ip[4:] 


'''loops through all the lines and gets the SRC ip from it, returns a list of ips'''
def getAllDstIp(info):
    #Save ips here
    ips = []
    #loop through all lines to get src ips
    for i in range(len(info)):
    #meter na lista ips com o append, o src ip a usar a funcao
    #de cima do elemento info(q e o ficheiro dividido por linhas)
    # i
        tempIp = getDstIp(info[i])
        #Tava a dar erro q as vezes nao encontra o ip na linha. Entao quando nao 
        #encontra tem o valor 0 e nao o acrescenta a lista
        if tempIp != 0:
            ips.append(tempIp)

    return ips
#receives array of ips, return array of locations
def getLocation(ips):
    locations = []
    #print ips
    #print ips[0]
    for ip in range(len(ips)):
        #Have to had a few exception since the geoip library returns an error with some ips
        if ips[ip]=='10.0.0.0' or ips[ip]=='224.0.0.1' or ips[ip]=='None' or ips[ip]=='0.0.0.0':
            location = 'None'
        else:
            #rint ips[ip]
            location = geoip.geoip_country(ips[ip])
            #print location
        locations.append(location)

    return locations
#receives array of ips, return array of locations
def getCity(ips):
    locations = []
    for ip in range(len(ips)):
        if ips[ip]=='10.0.0.0' or ips[ip]=='224.0.0.1' or ips[ip]=='None' or ips[ip]=='0.0.0.0':
            location = 'None'
        else:
            location = geoip.geoip_city(ips[ip])
        locations.append(location)
    return locations
#receives array of ips, return array of locations
def getSpecific(ips):
    locations = []
    for ip in range(len(ips)):
        if ips[ip]=='10.0.0.0' or ips[ip]=='224.0.0.1' or ips[ip]=='None' or ips[ip]=='0.0.0.0':
            location = 'None'
        else:
            location = geoip.geoip_specific(ips[ip])

        locations.append(location)
    return locations
#For ssh
#Reads line and if its ip it returns it
def getIp(line):
    line = line.split(' ')
    #print 'ONE LINE --> ',line[1]

    for i in range(len(line)):
        #print line[i]
        #print i
        if projeto.validateIp(line[i]):
            #print line[i]
            return line[i]
    else:
        return 'None'
def getIps(info):
    ips = []
    for i in range(len(info)):
        #print info[i]
        ips.append(getIp(info[i]))
    return ips
def getNote(line):
    #print
    line = line.split('sepsi ')
    #print line
    try:
        return line[1]
    except IndexError:
        return 'None'
def getNotes(info):
    notes = []
    for i in range(len(info)):
        notes.append(getNote(info[i]))
    return notes
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


#Function to run the full 
# protocolo = http, ssh etc
def run(filename, protocol, output):
    if output == 'db':
        settings.init()
        sqlite.checkDb()
    months = []
    days = []
    times = []
    if protocol == 'http':
        
        print "Inserting data gathered in the database"
        info = getInfo(filename)
        srcIps = getAllSrcIp(info)
        dstIps = getAllDstIp(info)
        dates = getAllDate(info)
        for i in range(len(dates)):
            months.append(dates[i][0])
            days.append(dates[i][1])
            times.append(dates[i][2])
        
        locationsSrc = getLocation(srcIps)
        locationsDst = getLocation(dstIps)
        citySrc = getCity(srcIps)
        cityDst = getCity(dstIps)
        specificSrc = getSpecific(srcIps)
        specificDst = getSpecific(dstIps)


        for i in range(len(months)):
            fields = ['LogName', 'Protocol', 'Month', 'Day', 'Time', 'SrcIp', 'SrcCountry',
                    'SrcCity', 'SrcSpecific','DstIp', 'DstCountry', 'DstCity', 'DstSpecific']
            values = [filename, protocol, months[i], days[i], times[i], srcIps[i],
                         locationsSrc[i],citySrc[i], specificSrc[i], dstIps[i], 
                         locationsDst[i], cityDst[i], specificDst[i]]

            if output == 'db':
                sqlite.insertIntoTable('Logs', fields, values)
            elif output == 'csv':
                print "Write csv"
            elif output == 'pdf':
                print "Write pdf"

    elif protocol=='ssh':
        print "Inserting data gathered in the database"
        info = getInfo(filename)
        #print info
        dates = getAllDate(info)
        ips = getIps(info)
        notes = getNotes(info)
        locationsSrc = getLocation(ips)
        citySrc = getCity(ips)
        specificSrc = getSpecific(ips)
        for i in range(len(dates)):
            months.append(dates[i][0])
            days.append(dates[i][1])
            times.append(dates[i][2])
        

        for i in range(len(months)):
            fields = ['LogName', 'Protocol', 'Month', 'Day', 'Time', 'SrcIp', 'SrcCountry',
                    'Notes']
            values = [filename, protocol, months[i], days[i], times[i], ips[i],
                         locationsSrc[i],notes[i]  ]
            if output == 'db':
                sqlite.insertIntoTable('Logs', fields, values)
            elif output == 'csv':
                print "Write csv"
            elif output == 'pdf':
                print "Write pdf"
            
    if output == 'db':
        sqlite.closeDb()
        




def main():
    run('auth.log', 'ssh')

    #print validateIp('192.1.1.')





#Isto serve para poder correr o ficheiro sozinho ou
# importalo para outro script de python
if __name__=='__main__':
    main()
