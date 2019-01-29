#!/usr/bin/python
from datetime import datetime
import socket
import sys


def portScan(ip, ports):
    r = ports.split('-')
    r1 = int(r[0])
    r2 = int(r[1])

    print "*"*20
    print "     Scanning target -->   ", ip
    print "*"*20
    t1 = datetime.now()
    
    try:
        for port in range(r1, r2):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((ip, port))
            if result ==0:
                print "Port Open -->\t", port
            sock.close()
    except KeyboardInterrupt:
        print "Press any key to stop"
        sys.exit(4)
    except socket.gaierror:
        print "Hostname could not be resolved"
        sys.exit(4)
    except socket.error:
        print "Could no connect to server"
        sys.exit(4)
    t2 = datetime.now()
    total = t2-t1
    print "Scanning complete in ", total


