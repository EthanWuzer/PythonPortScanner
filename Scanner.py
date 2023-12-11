#!/usr/bin/python3

import socket
import ipaddress
import re
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

host = "137.74.187.104"
ports = []

def portScan(host, ports):
    
    if (os.system("ping /n 1 " + host) == 0):
        for port in ports:
            print(port)
            if s.connect_ex((host,port)):
                print("{port}: Closed".format(port=port))
            else:
                print("{port}: OPEN".format(port=port))
    else:
        print("Could not establish connection to {host}.".format(host=host))
    
def getHost():
    print("Please enter the IP address you would like to scan (ex: 192.168.1.1):")
    ip_string = input()
    try:
        ip_object = ipaddress.ip_address(ip_string)
        print("The IP address '{ip_string}' is valid.".format(ip_string=ip_string))
        return ip_string
    except ValueError:
        print("The IP address '{ip_string}' is not valid.".format(ip_string=ip_string))
        getHost()
    
def getPorts():
   
    while True:
        print ("Please enter the port(s) you would like to scan. Please separate values with ',' and denote ranges in the form 'a-b':")
        input_string = input()
        if validatePortInput(input_string):
            break
        else:
            print ("Invalid Input.")
    args = []
    for part in input_string.split(','):
        if '-' in part:
            a,b = part.split('-')
            a,b = int(a), int(b)
            args.extend(range(a,b+1))
        else:
            a=int(part)
            args.append(a)
    args = list(set(args))
    return args

def validatePortInput(inputString):
    pattern = re.compile(r'^\d+(-\d+)?(,\d+(-\d+)?)*$')

    if pattern.match(inputString):
        return True
    else:
        pass
    
def main():
    host = getHost()
    ports = getPorts()
    print 
    portScan(host, ports)
       

if (__name__ =="__main__"):
    main()