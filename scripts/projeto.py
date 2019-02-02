#!/usr/bin/python
"""
Projeto de LPD
"""
# -*- coding: utf-8 -*-
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
import RSA_create
import processLogs
import AES
from subprocess import Popen
import analyze
import GeoMap

#Variaveis usadas ao longo do programa
Parameters = ["-h", "-v", "-nat", "-g", "-uF", "-pS", "-p", "-dbA", "-eR", "-dR", "-c", "-csv", 
                    "-pdf", '-pL', '-db', '-dbC', '-dbE', '-dbD','-anL', '-anS', '-gMS', '-gML',
                    "-dbP", "-dbO", "-eA", "-dA"]
Verbouse = False
Geo_ip = 0
PortIp = 0
UdpFloodIp = 0
Ports = "0-1024"
EstablishedConnections = False
Database = False
DatabaseParameters = ["check", "sql","cT", "dT", "iT", "sT", "uId", "dId" ]
RSA_do = 0 # 1 for encript, 2 for decript, 3 for key gen
RSA_files = []
ProcessLogs = 0
ProcessLogs_Protocol = ''
ProcessLogs_File = ''
WriteDb = ''
WriteCsv = ''
WritePdf = ''
analyzeLogs = ''
analyzeScripts = ''
geoMapS = ''
geoMapL = ''
dbPdf = ''
dbCsv = ''
AES_do = 0
AES_files = []


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
    #print "   {}:\t\tHelp menu (This) ".format(Parameters[0])
    #print ""

    print "**** Network *****"
    print "   {}:\tEstablished Connections \t\tex: -nat".format(Parameters[2]) 
  #  print "   {}:\t\tVerbouse mode        ".format(Parameters[1])
    print "   {}:\t\tGeoip location           \t\tex: -g  192.168.1.1".format(Parameters[3])
    print "   {}:\t\tPort Scan                \t\tex: -pS 192.168.1.1".format(Parameters[5])
    print "   {}:\t\tPorts (0-1024)           \t\tex: -p  0-2042  ".format(Parameters[6])
    print "   {}:\t\tUdp Flood (CAUTION)      \t\tex: -uF 192.168.1.1".format(Parameters[4])
    print ""
    print "***** Encription *******"
    print "   {}:\t\tRSA Create Key Pair      \t\tex: -c ".format(Parameters[10])
    print "   {}:\t\tRSA Encription           \t\tex: -eR <file1> <file2> ...".format(Parameters[8])
    print "   {}:\t\tRSA Decription           \t\tex: -dR <file1> <file2> ...".format(Parameters[9])
    print "   {}:\t\tAES Encription           \t\tex: -eA <file1> <file2> ...".format(Parameters[24])  
    print "   {}:\t\tAES Decription           \t\tex: -dA <file1> <file2> ...".format(Parameters[25])  

    print ""
    print "***** Database  *******"
    #print "AES encryption "
    print "   {}:\tDatabase Check               \t\tex: -dbC".format(Parameters[15])
    print "   {}:\tDatabase AES Encrypt         \t\tex: -dbE".format(Parameters[16])
    print "   {}:\tDatabase AES Decrypt         \t\tex: -dbD".format(Parameters[17])
    print ""
    print "***** Processing ******"
    print "   {}:\tExport GeoMap from Script table     \t ex: -gMS <file>".format(Parameters[20])
    print "   {}:\tExport GeoMap from Logs table     \t ex: -gML <file>".format(Parameters[21])
    print "   {}:\tAnalyze Logs table and export to pdf     ex: -anL <file>".format(Parameters[18])
    print "   {}:\tAnalyze Script table and export to pdf   ex: -anS <file>".format(Parameters[19])
    print "   {}:\t\tProcess Logs(http, ssh)                  ex: -pL http <file>".format(Parameters[13])
    print "      \t\tto default database                      ex: -pL ssh  <file>"

    print ""
    print "***** Exports    *******"
    print "May be used with the network actions"
    print "   {}:\tExport to Csv            \t\tex: -csv <file>".format(Parameters[11])
    print "   {}:\tExport to Pdf                    \tex: -pdf <file>".format(Parameters[12])
    print "   -db:\t\tExport to Db             \t\tex: -db".format(Parameters[13])
    print "   {}:\tFrom db export to Pdf\t\t\tex: -dfP".format(Parameters[22])
    print "   {}:\tFrom db export to Csv\t\t\tex: -dfO".format(Parameters[23])

#    print ""

#    print "   {}:\t\tDatabase Funcionalities  ex: -db args".format(Parameters[7])    
#    print "                         -db {} : Checks database status".format(DatabaseParameters[0])
#    print "                         -db {}   : Executes Sql Query".format(DatabaseParameters[1])
#    print "                         -db {}    : Creates table".format(DatabaseParameters[2])
#    print "                         -db {}    : Drops table".format(DatabaseParameters[3])
#    print "                         -db {}    : Inserts value into table".format(DatabaseParameters[4])
#    print "                         -db {}    : Selects and prints information in table".format(DatabaseParameters[5])
#    print "                         -db {}   : Updates Id information".format(DatabaseParameters[6])
#    print "                         -db {}   : Deletes Id".format(DatabaseParameters[7])
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
        Popen('clear')
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
#RSA Encrypt
        if sys.argv[i] == Parameters[8]:
            global RSA_do
            global RSA_files
            try:
                for x in range((len(sys.argv)) - i-1):
                    if sys.argv[i+1+x].startswith('-') or not bool(sys.argv[i+x+i]):
                        break
                    else:
                        RSA_files.append(sys.argv[i+x+1])

                RSA_do = 1
            except IndexError:
                print "No file to encript specified"
#RSA Decrypt
        if sys.argv[i] == Parameters[9]:
            try:
                for x in range((len(sys.argv)) - i-1):
                    if sys.argv[i+1+x].startswith('-') or not bool(sys.argv[i+x+i]):
                        break
                    else:
                        RSA_files.append(sys.argv[i+x+1])
                RSA_do = 2
            except IndexError:
                print "No file to decript specified"
#RSA Generate Keys
        if sys.argv[i] == Parameters[10]:
            RSA_do = 3;
#***Exports***
#Csv
        if sys.argv[i] == Parameters[11]:
            try:
                global WriteCsv
                WriteCsv = sys.argv[i+1]
            except IndexError:
                errorArgument("-csv", 4)
#Pdf
        if sys.argv[i] == Parameters[12]:
            try:
                global WritePdf
                WritePdf = sys.argv[i+1]
            except IndexError:
                errorArgument("-pdf", 4)

        if sys.argv[i] == Parameters[13]:
            global ProcessLogs
            global ProcessLogs_File
            global ProcessLogs_Protocol
            try:
                ProcessLogs_Protocol = sys.argv[i+1]
                ProcessLogs = 1
                ProcessLogs_File = sys.argv[i+2]
            except IndexError:
                print "No protocol specified"
            if not ProcessLogs_File:
                print "No file specified"
                exit()
#Db
        if sys.argv[i] == Parameters[14]:
            global WriteDb
            WriteDb = 1
        if sys.argv[i] == Parameters[15]:
            dbnam = settings.getDatabaseStatus()
            if os.path.exists(dbnam):
                print "Database exists decripted"
            dbnam = dbnam + '.crypt'
            if os.path.exists(dbnam):
                print "Database exists encrypted"
        if sys.argv[i] == Parameters[16]:
            dbnam = settings.getDatabaseStatus()
            dbnam_crypt = dbnam+'.crypt'
            AES.encrypt_file(settings.getKey(), dbnam, dbnam_crypt, 16)
            print "Database encrypted"
            Popen(['rm', dbnam])

        if sys.argv[i] == Parameters[17]:
            dbnam = settings.getDatabaseStatus()
            dbnam_crypt = dbnam+'.crypt'
            AES.decrypt_file(settings.getKey(), dbnam_crypt, dbnam, 16)
            print "Database decrypted"
            Popen(['rm', dbnam_crypt])

#Analyze logs
        if sys.argv[i] == Parameters[18]:
            try:
               global analyzeLogs
               analyzeLogs = sys.argv[i+1]
            except IndexError:
                errorArgument("-arL", 1)

        if sys.argv[i] == Parameters[19]:
            try:
               global analyzeScripts
               analyzeScripts = sys.argv[i+1]
            except IndexError:
                errorArgument("-arS", 1)
#GeoMap
        if sys.argv[i] == Parameters[20]:
            try:
               global geoMapS
               geoMapS = sys.argv[i+1]
            except IndexError:
                errorArgument("-gMS", 1)
        if sys.argv[i] == Parameters[21]:
            try:
               global geoMapL
               geoMapL = sys.argv[i+1]
            except IndexError:
                errorArgument("-gML", 1)
#Db to csv/pdf
        if sys.argv[i] == Parameters[22]:
            try:
               global dbPdf
               dbPdf = sys.argv[i+1]
            except IndexError:
                errorArgument("-dbP", 1)
        if sys.argv[i] == Parameters[23]:
            try:
               global dbCsv
               dbCsv = sys.argv[i+1]
            except IndexError:
                errorArgument("-dbO", 1)
#AES Encrypt
        if sys.argv[i] == Parameters[24]:
            global AES_do
            global AES_files
            try:
                for x in range((len(sys.argv)) - i-1):
                    if sys.argv[i+1+x].startswith('-') or not bool(sys.argv[i+x+i]):
                        break
                    else:
                        AES_files.append(sys.argv[i+x+1])

                AES_do = 1
            except IndexError:
                print "No file to encript specified"
#AES Decrypt
        if sys.argv[i] == Parameters[25]:
            try:
                for x in range((len(sys.argv)) - i-1):
                    if sys.argv[i+1+x].startswith('-') or not bool(sys.argv[i+x+i]):
                        break
                    else:
                        AES_files.append(sys.argv[i+x+1])
                AES_do = 2
            except IndexError:
                print "No file to decript specified"

#check for each flag and run the function
def run():

    if Geo_ip != 0:
        
        geoip.geoIp(Geo_ip, WriteDb, WriteCsv, WritePdf)
        
    if PortIp != 0:
        portScan.portScan(PortIp, Ports, WriteDb, WriteCsv, WritePdf)
    if UdpFloodIp != 0:
        udpFlood.udpFlood(UdpFloodIp, Verbouse)
    if EstablishedConnections:
        #encrypt.EnDecript(False, 'scripts/establishedConnections.py'+'.crypt')
        establishedConnections.establishedConn(WriteDb, WriteCsv, WritePdf)
        #encrypt.EnDecript(True, 'scripts/establishedConnections.py')
        #encrypt.EnDecript(True, 'scripts/establishedConnections.py')
        #print "encripted"

    if RSA_do == 1:
        for y in range(len(RSA_files)):
            RSA.runEncrypt(RSA_files[y], keyFile=settings.getKeyPublic())
    if RSA_do == 2:
        for y in range(len(RSA_files)):
            RSA.runDecrypt(RSA_files[y], keyFile=settings.getKeyPrivate())
    if RSA_do == 3:
        keys_filename = raw_input("Enter the filename of the keys -->  ")
        RSA_create.run(keys_filename)

    if AES_do == 1:
        for y in range(len(AES_files)):
            AES.encrypt_file(settings.getKey(),AES_files[y],(AES_files[y]+".crypt"))
            Popen(['rm', AES_files[y]])
    if AES_do == 2:
        for y in range(len(AES_files)):
            AES.decrypt_file(settings.getKey(),AES_files[y],AES_files[y][:-6])
            Popen(['rm', AES_files[y]])
    if ProcessLogs:

        processLogs.run(ProcessLogs_File, ProcessLogs_Protocol, 'db')
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
    if analyzeLogs:
        analyze.runPdfChartsLogs('output/pdf/'+ analyzeLogs)
    if analyzeScripts:
        analyze.runPdfChartsScript('output/pdf/'+analyzeScripts)
    if geoMapS:
        GeoMap.runDbGeoMapS(geoMapS)
    if geoMapL:
        GeoMap.runDbGeoMapL(geoMapL)
    if dbPdf:
        analyze.exportDbPdf(dbPdf)
    if dbCsv:
        analyze.exportDbCsv(dbCsv)


    #sqlite.checkDb(settings.getDatabase())


def main():
    start()
    run()

if __name__=='__main__':
    main()

