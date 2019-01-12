#!/usr/bin/python
'''
Projeto de LPD
'''

#imports
import sys
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


#Variaveis usadas ao longo do programa
Parameters = ["-h", "-v", "-nat", "-g", "-uF", "-pS", "-p"]
Verbouse = False
Geo_ip = 0
PortIp = 0
UdpFloodIp = 0
Ports = "0-1024"
EstablishedConnections = False

    #########################################
    #                                       #
    #       Scripts Principais              #
    #                                       #
    #########################################




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
    print "Projecto de Linguagens de Programacao Dinamicas\n"
    print "   {}:\t\tHelp menu (This) ".format(Parameters[0])
    print "   {}:\t\tEstablished Connections ".format(Parameters[1]) 
    print "   {}:\tVerbouse mode        ".format(Parameters[2])
    print "   {}:\t\tgeoip location           ex: -g  192.168.1.1".format(Parameters[3])
    print "   {}:\t\tPort Scan                ex: -pS 192.168.1.1".format(Parameters[5])
    print "   {}:\t\tPorts (0-1024)           ex: -p  0-2042  ".format(Parameters[6])
    print "   {}:\t\tUdp Flood (CAUTION)      ex: -uF 192.168.1.1".format(Parameters[4])


#Print dos erros facilitado    
def errorArgument(arg, errorCode):
    print "You need to specify an argument after the parameter "+arg
    sys.exit(errorCode)






#Read the arguments and set the variables used later on
def start():
    #subprocess.call('clear', shell=True)
    #Check for arguments
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
        if sys.argv[i] == Parameters[5]:
            global Verbouse
            Verbouse = True

#Geoip    takes 1 arg [ip]    
        if sys.argv[i] == Parameters[1]:
            try:
                validateIpError(sys.argv[i+1])
                global Geo_ip
                Geo_ip = sys.argv[i+1]
            except IndexError:
                errorArgument("-g", 1)

#PortScan   takes 2 arg [ip, port]
        if sys.argv[i] == Parameters[2]:
            try:
                validateIpError(sys.argv[i+1])
                global PortIp
                PortIp = sys.argv[i+1]
            except IndexError:
                errorArgument("-pS", 2)
            
#searchs por -p argument and checks port range            
        if sys.argv[i] == Parameters[3]:
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
        if sys.argv[i] == Parameters[6]:
           global EstablishedConnections
           EstablishedConnections = True 
          


#check for each flag and run the function
def run():
    if Geo_ip != 0:
        geoip.geoIp(Geo_ip)
    if PortIp != 0:
        portScan.portScan(PortIp, Ports)
    if UdpFloodIp != 0:
        udpFlood.udpFlood(UdpFloodIp, Verbouse)
    if EstablishedConnections:
        establishedConnections.establishedConn()


def main():
    start()
    run()

if __name__=='__main__':
    main()

