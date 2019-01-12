#!/usr/bin/python
'''
Prints Established Connections from the netstat -nat  command
'''
from subprocess import Popen, PIPE

def establishedConn():
    p1 = Popen(['netstat', '-nat'], stdout=PIPE)
    p2 = Popen(['grep', 'ESTABLISHED'], stdin=p1.stdout, stdout=PIPE)
    p1.stdout.close()   #allow p1 to receive SIGPIPE if p2 exists

    output = p2.communicate()[0]
    print output


