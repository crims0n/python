#!/usr/bin/env python

# bannerGrab v0.1 by Patrick McDowell
# Simple python 2.x script to connect to a specific host/port and grab the first 1024 bytes of data
# Tested on 2.7.10, last update July 31st 2019

import socket

def returnBanner(ip, port):
    socket.setdefaulttimeout(2)
    s = socket.socket()

    try:
        s.connect((ip,port))
        print "[-] Connected to " + ip + " on port " + str(port) + "."
        banner = s.recv(1024)
        return banner

    except Exception, e:
            return "[1] Error = " + str(e)
            

def main():

    userInput = raw_input("Enter IP or hostname: ")
    
    if ':' in userInput:
        ip = str(userInput.split(':')[0])
        port = int(userInput.split(':')[1])
    else:
        ip = userInput
        port = int(raw_input("Enter a port: "))

    banner = returnBanner(ip,port)
    print banner

if __name__ == '__main__':
    main()