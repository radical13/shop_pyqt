# -*- coding: utf-8 -*-

#Aimed to:
#0.exit login
#
# Created by: Hushiyang
#
# 2017.11
from socket import *

HOST = '10.105.69.173'
PORT = 60003

s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))

print('...waiting for message..')

while True:
    print('server waiting')
    data,address = s.recvfrom(1024)

    if not data:
        break
    else:
        file = open("log/login_log.txt", 'r')
        a = file.read()
        login_info = eval(a)
        file.close()
        if login_info.__contains__(data):
            login_info[data]["state"] = "False"
            s.sendto("0",address)

            #write back
            file = open("log/login_log.txt", 'w')
            file.write(str(login_info))
            file.close()
        else:
            s.sendto("1", address)

