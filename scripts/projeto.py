#!/usr/bin/python
'''
Projeto de LPD
'''

#imports
import sys
import os
import re
import geoip2.database
import socket
import subprocess
import random
from datetime import datetime
#Import from same folder
import geoip
import portScan
import udpFlood
import establishedConnections
import encrypt
import settings
import sqlite
import RSA
#Variaveis usadas ao longo do programa
Parameters = ["-h", "-v", "-nat", "-g", "-uF", "-pS", "-p", "-db", "-e", "-d"]
Verbouse = False
Geo_ip = 0
PortIp = 0
UdpFloodIp = 0
Ports = "0-1024"
EstablishedConnections = False
Database = False
DatabaseParameters = ["check", "sql","cT", "dT", "iT", "sT", "uId", "dId" ]
RSA_do = 0 # 1 for encript, 2 for decript
RSA_files = ''


    #########################################
    #                                       #
    #     Funcoes Auxiliares                #
    #                                       #
    #########################################

#Checks if ip address is valid
#Returns True if it is, False otherwise
def validateIp(s):
    a = s.split('.')

    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i<0 or i>255:
            return False
    return True
#Validates ip and prints error if not valid
def validateIpError(ip):
    if(validateIp(ip)):
        return True
    else:
        print "Ip address is not valid"
        sys.exit(2)
#Returns boolean True or exits the program
#Validates port range of the parameter
def validatePortRange(portRange):
    a = portRange.split('-')
    try:
        if int(a[0]) >= 0 and int(a[0]) <= 65535:
            if int(a[1]) >= 0 and int(a[1]) <= 65535:
                return True
    except ValueError:
        print "please enter a valid port range"
        sys.exit(3)
    
    print "please enter a valid port range"
    sys.exit(3)
    return False







    #####################################
    #                                   #
    #           Funcoes Menu            #
    #                                   #
    #####################################





#Menu de ajuda
def usage():
    print subprocess.check_output('figlet LPD --metal',shell=True)
    print "Projecto de Linguagens de Programacao Dinamicas\n"
    print "   {}:\t\tHelp menu (This) ".format(Parameters[0])
    print "   {}:\t\tEstablished Connections ".format(Parameters[1]) 
    print "   {}:\tVerbouse mode        ".format(Parameters[2])
    print "   {}:\t\tgeoip location           ex: -g  192.168.1.1".format(Parameters[3])
    print "   {}:\t\tPort Scan                ex: -pS 192.168.1.1".format(Parameters[5])
    print "   {}:\t\tPorts (0-1024)           ex: -p  0-2042  ".format(Parameters[6])
    print "   {}:\t\tUdp Flood (CAUTION)      ex: -uF 192.168.1.1".format(Parameters[4])
    print "   {}:\t\tRSA Encription           ex: -e <file>".format(Parameters[8])
    print "   {}:\t\tRSA Decription           ex: -d <file>".format(Parameters[9])
    print "   {}:\t\tDatabase Funcionalities  ex: -db args".format(Parameters[7])
    print "                         -db {} : Checks database status".format(DatabaseParameters[0])
    print "                         -db {}   : Executes Sql Query".format(DatabaseParameters[1])
    print "                         -db {}    : Creates table".format(DatabaseParameters[2])
    print "                         -db {}    : Drops table".format(DatabaseParameters[3])
    print "                         -db {}    : Inserts value into table".format(DatabaseParameters[4])
    print "                         -db {}    : Selects and prints information in table".format(DatabaseParameters[5])
    print "                         -db {}   : Updates Id information".format(DatabaseParameters[6])
    print "                         -db {}   : Deletes Id".format(DatabaseParameters[7])
#Print dos erros facilitado    
def errorArgument(arg, errorCode):
    print "You need to specify an argument after the parameter "+arg
    sys.exit(errorCode)






#Read the arguments and set the variables used later on
def start():
    #subprocess.call('clear', shell=True)
    #Check for arguments

    #load settings

    settings.init()



    if len(sys.argv) < 2:
        usage()
        sys.exit(0)
    #use arguments to set flags    
    for i in range(len(sys.argv)):
#Help
        if sys.argv[i] == Parameters[0] or sys.argv[i] == '--help':
            usage()
            sys.exit(0)
#Verbouse
        if sys.argv[i] == Parameters[1]:
            global Verbouse
            Verbouse = True

#Geoip    takes 1 arg [ip]    
        if sys.argv[i] == Parameters[3]:
            try:
                validateIpError(sys.argv[i+1])
                global Geo_ip
                Geo_ip = sys.argv[i+1]
            except IndexError:
                errorArgument("-g", 1)

#PortScan   takes 2 arg [ip, port]
        if sys.argv[i] == Parameters[5]:
            try:
                validateIpError(sys.argv[i+1])
                global PortIp
                PortIp = sys.argv[i+1]
            except IndexError:
                errorArgument("-pS", 2)
            
#searchs por -p argument and checks port range            
        if sys.argv[i] == Parameters[6]:
            try:
                validatePortRange(sys.argv[i+1])
            except IndexError:
                errorArgument("-p", 2) 
            global Ports
            Ports = sys.argv[i+1]


#UdpFlooding   takes 1 arg [ip]
        if sys.argv[i] == Parameters[4]:
            try:
                validateIpError(sys.argv[i+1])
                global UdpFloodIp
                UdpFloodIp = sys.argv[i+1]
            except IndexError:
                errorArgument("-uF", 4)
#Established Connections flag
        if sys.argv[i] == Parameters[2]:
           global EstablishedConnections
           EstablishedConnections = True 
#Database
        if sys.argv[i] == Parameters[7]:
            global Database
            global DatabaseAction
            
            try:
                Database = True
                DatabaseAction = sys.argv[i+i]
            except IndexError:
                print "No '-db' arguments specified"
                Database = False
#RSA
        if sys.argv[i] == Parameters[8]:
            global RSA_do
            global RSA_file
            try:
                RSA_file = sys.argv[i+1]
                RSA_do = 1
            except IndexError:
                print "No file to encript specified"
        if sys.argv[i] == Parameters[9]:
            global RSA_do
            global RSA_file
            try:
                RSA_file = sys.argv[i+1]
                RSA_do = 2s
            except IndexError:
                print "No file to decript specified"


#check for each flag and run the function
def run():
    if Geo_ip != 0:
        
        geoip.geoIp(Geo_ip)
        
    if PortIp != 0:
        portScan.portScan(PortIp, Ports)
    if UdpFloodIp != 0:
        udpFlood.udpFlood(UdpFloodIp, Verbouse)
    if EstablishedConnections:
        #encrypt.EnDecript(False, 'scripts/establishedConnections.py'+'.crypt')
        establishedConnections.establishedConn()
        #encrypt.EnDecript(True, 'scripts/establishedConnections.py')
        #encrypt.EnDecript(True, 'scripts/establishedConnections.py')
        #print "encripted"

    if RSA_do == 1:
        RSA.runEncrypt(RSA_file, keyFile=settings.getKeyPublic())
    if RSA_do == 2:
        RSA.runDecrypt(RSA_file, keyFile=settings.getKeyPrivate())
    if Database:
        sqlite.checkDb()
        if DatabaseAction==DatabaseParameters[0]:
            sqlite.checkDb
        elif DatabaseAction==DatabaseParameters[1]:
            sqlite.userExecuteSql()
        elif DatabaseAction==DatabaseParameters[2]:
            sqlite.userCreateTable()
        elif DatabaseAction==DatabaseParameters[3]:
            sqlite.userDropTable()
        elif DatabaseAction==DatabaseParameters[4]:
            sqlite.userInsertTable()
        elif DatabaseAction==DatabaseParameters[5]:
            sqlite.userSelectTable()
        elif DatabaseAction==DatabaseParameters[6]:
            sqlite.userUpdateId()
        elif DatabaseAction==DatabaseParameters[7]:
            sqlite.userDeleteId()

        sqlite.closeDb()




    #sqlite.checkDb(settings.getDatabase())


def main():
    start()
    run()

if __name__=='__main__':
    main()

