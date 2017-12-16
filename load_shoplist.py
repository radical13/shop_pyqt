# -*- coding: utf-8 -*-

#Aimed to:
#
#0.load shop list and user's infomation after logining sucessfully
#1.look for some shop and show them(maybe there are two shops have same names)
#
# Created by: Hushiyang
#
# 2017.11

from socket import *
import json


def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

#the imformation for registered users
user_infomation = {
    'hushiyang':{
        'pw':'KaJe2008',
        'sex':'M',
        'shop':'0'
    },
    'xiaoming123':{
        'pw':'123456',
        'sex':'F',
        'shop':'21340'
    },
    'zhangsan':{
        'pw':'woaijiwang',
        'sex':'F',
        'shop':'0'
    },
    'LAOban':{
        'pw':'zuixihuanjiwangkele',
        'sex':'M',
        'shop':'32423'
    }
}

#the imformation for shops
shop_list ={
    '10019':{
        "name":"小米手机旗舰店",
        "owner":"雷军"
    },
    '32423':{
        "name":"Apple旗舰店",
        "owner":"Cook"
    },
    '11323':{
        "name":"三只松鼠",
        "owner":"鼠小宝"
    },
    '50344':{
        "name":"三星手机旗舰店",
        "owner":"小炸"
    },
    '90231':{
        "name":"KFC旗舰店",
        "owner":"卡姆氏"
    },
    '38943':{
        "name":"Python源码一体店",
        "owner":"小p"
    },
    '21340':{
        "name":"专业PJ代写",
        "owner":"4.0"
    },
    '24330':{
        "name":"卫尤辣条",
        "owner":"小作坊"
    },
    '92310':{
        "name":"聚美优品",
        "owner":"陈欧"
    },
    '79123':{
        "name":"B站旗舰店",
        "owner":"2233"
    },
}

HOST = '10.105.69.173'
PORT = 60002

s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))

print('...waiting for message..')

while True:
    print('server waiting')
    data,address = s.recvfrom(1024)

    if not data:
        break

    r_data = json.dumps(shop_list)
    s.sendto(r_data,address)
