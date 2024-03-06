#!/usr/bin/python

import socket
import os
import sys

def retbanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return


def checkVuln(banner, filename):
    f = open(filename, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner.decode('utf-8'):
            print('server is vulnerable: ' + banner.decode('utf-8').strip('\n'))


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('file does not exist')
            exit(0)
        if not os.access(filename, os.R_OK):
            print('access denied')
            exit(0)
    else:
        print('Usage: ' + str(sys.argv[0]) + ' <vuln filename>')
        exit(0)
    portlist = [21, 22, 25, 80, 110, 443, 445]
    for x in range(1, 130):
        ip = '192.168.50.' + str(x)
        for port in portlist:
            banner = retbanner(ip, port)
            if banner:
                print(ip + '/' + str(port) + ': ' + banner)
                checkVuln(banner, filename)

if __name__ == '__main__':
    main()

