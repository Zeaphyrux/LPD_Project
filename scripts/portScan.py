#!/usr/bin/python
from datetime import datetime
import socket
import sys
import sqlite
sys.path.insert(0, 'scripts')

import settings


def portScan(ip, ports):
    settings.init()
    db = settings.getDatabaseStatus()
    r = ports.split('-')
    r1 = int(r[0])
    r2 = int(r[1])
    openPorts = ''
    print "*"*40
    print "     Scanning target -->   ", ip
    print "*"*40
    t1 = datetime.now()
    
    try:
        for port in range(r1, r2):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((ip, port))
            if result ==0:
                print "Port Open -->\t", port
                openPorts+= str(port) + ', '
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
    if openPorts:
        openPorts = openPorts[:-2]
    else:
        openPorts = 'None'
    if db:
        print "Inserting data gathered in the database"
        sqlite.checkDb()
        now = datetime.now()
        now = str(now)
        now = now[:-7]


        fields = ['Data', 'Ip', 'RangeScanned', 'PortsOpen']
        values = [now, ip,ports, openPorts  ]

        sqlite.insertIntoTable('Script', fields, values)

        #print fields
        #print values
        sqlite.closeDb()
