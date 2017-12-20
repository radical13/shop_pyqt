# -*- coding: utf-8 -*-

from socket import *
import json
import hashlib
import datetime

def send_shoplist(s,data,address):

    msg = {}
    for key in shop_list:
        if shop_list[key]["state"] == "open":
            msg[key] = {"name":"","owner":""}
            msg[key]["name"] = shop_list[key]["name"]
            msg[key]["owner"] = shop_list[key]["owner"]
    msg = json.dumps(msg)
    if s.sendto(msg, address) != 0:
        return "0"
    else:
        # SEND FAIL
        return "2"

def login_check(s,data, address):

    user_id = data["id"]
    user_pw = data["pw"]

    if user_infomation.get(user_id, "NULL") == "NULL":
        if s.sendto('NO_USER', address)!=0:
            return "1"
        else:
            #SEND FAIL
            return "2"
    pw_m = hashlib.md5()
    pw_m.update(user_infomation[user_id]["pw"].encode("utf-8"))

    # check the password
    user_pw_md5 = pw_m.hexdigest()

    if user_pw_md5 == user_pw:
        if s.sendto('SUCCESS', address) != 0:
            # update login info，record the login log
            if login_info.__contains__(user_id):
                login_info[user_id]["state"] = "true"
                info = {"time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "add": address}
                login_info[user_id]["history"].append(info)
            else:
                login_info[user_id] = {"state": "", "history": []}
                login_info[user_id]["state"] = "true"
                info = {"time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "add": address}
                login_info[user_id]["history"].append(info)
            return "0"
        else:
            #SEND FAIL
            return "2"
    else:
        if s.sendto('FAIL', address)!=0:
            return "1"
        else:
            # SEND FAIL
            return "2"

def exit_request(s,data, address):
    if login_info.__contains__(data["user"]):
        login_info[data["user"]]["state"] = "False"
        if s.sendto("0", address)!=0:
            return "0"
        else:
            #SEND FAIL
            return "2"
    else:
        if s.sendto("1", address) != 0:
            return "1"
        else:
            #SEND FAIL
            return "2"

def enter_shop(s,data,address):
    if shop_list.__contains__(data["id"]):
        if shop_list[data["id"]]["state"] == "open":
            msg={"state":"open","goods":[]}
            msg["goods"] = shop_list[data["id"]]["goods"]
            msg["id"] = data["id"]
            msg["name"] = shop_list[data["id"]]['name']
            msg = json.dumps(msg)
            if s.sendto(msg, address) != 0:
                #store online visitor
                if shop_visit.__contains__(data["id"]):
                    if data["user"] not in shop_visit[data["id"]] and data['user'] != shop_list[data['id']]['owner']:
                        shop_visit[data["id"]].append(data["user"])
                elif data['user'] != shop_list[data['id']]['owner']:#the owner not in the visit list
                    shop_visit[data["id"]] = []
                    shop_visit[data["id"]].append(data["user"])

                #send msg to owner
                return "0"
            else:
                # SEND FAIL
                return "2"
        elif shop_list[data["id"]]["state"] == "close":
             msg = {"state": "close", "goods": []}
             msg = json.dumps(msg)
             if s.sendto(msg, address) != 0:
                 return "0"
             else:
                 # SEND FAIL
                 return "2"
    else:
        msg = {"state": "null", "goods": []}
        msg = json.dumps(msg)
        if s.sendto(msg, address) != 0:
            return "0"
        else:
            # SEND FAIL
            return "2"


def leave_shop(s,data,address):
    if data["user"] == shop_list[data["id"]]["owner"]:
        msg = "0"
        if s.sendto(msg, address) != 0:
            return "0"
        else:
            # SEND FAIL
            return "2"
    else:
        if shop_visit.__contains__(data["id"]):
            if data["user"] in shop_visit[data["id"]]:
                if data["user"] in shop_visit[data["id"]]:
                    shop_visit[data["id"]].remove(data["user"])
                msg="0"
                if s.sendto(msg, address) != 0:
                    return "0"
                else:
                    # SEND FAIL
                    return "2"
            else:
                msg = "1"
                if s.sendto(msg, address) != 0:
                    return "0"
                else:
                    # SEND FAIL
                    return "2"
        else:
            msg = "1"
            if s.sendto(msg, address) != 0:
                return "0"
            else:
                # SEND FAIL
                return "2"

def enter_own_shop(s,data,address):
    user = data["user"]
    if user_infomation[user]["shop"] != 0:
        data["id"] = str(user_infomation[user]["shop"])
        if enter_shop(s,data,address) == "0":
            return "0"
        else:
            return "1"
    else:
        msg = {"state": "null", "goods": []}
        msg = json.dumps(msg)
        if s.sendto(msg, address) != 0:
            return "0"
        else:
            # SEND FAIL
            return "2"

def show_custom(s,data,address):
    id = data["id"]
    msg={}
    if shop_visit.__contains__(id):
        msg[id] = shop_visit[id]
        msg = json.dumps(msg)
        if s.sendto(msg, address) != 0:
            return "0"
        else:
            # SEND FAIL
            return "2"
    else:
        msg[id] = []
        msg = json.dumps(msg)
        if s.sendto(msg, address) != 0:
            return "0"
        else:
            # SEND FAIL
            return "2"
def has_shop(s,data,address):
    if user_infomation[data['user']]['shop']!=0:
        if s.sendto("0", address) != 0:
            return "0"
        else:
            # SEND FAIL
            return "2"
    else:
        if s.sendto("1", address) != 0:
            return "1"
        else:
            # SEND FAIL
            return "2"
def load_info(s,data,address):
    if user_infomation.__contains__(data['user']):
        msg = user_infomation[data["user"]]
        msg = json.dumps(msg)
        if s.sendto(msg, address) != 0:
            return "0"
        else:
            # SEND FAIL
            return "2"
    else:
        msg={}
        msg = json.dumps(msg)
        if s.sendto(msg, address) != 0:
            return "1"
        else:
            # SEND FAIL
            return "2"
def byteify(input):
        if isinstance(input, dict):
            return {byteify(key): byteify(value) for key, value in input.iteritems()}
        elif isinstance(input, list):
            return [byteify(element) for element in input]
        elif isinstance(input, unicode):
            return input.encode('utf-8')
        else:
            return input
#store the messge wait to send
#{"recv":[{"send":"","time":"","content":""}]}
message={}

#the imformation for registered users
user_infomation = {
    #the manager root
    'root':{
        'pw':'SD58522',
    },
    'hushiyang':{
        'pw':'KaJe2008',
        'sex':'M',
        'shop':0
    },
    '鼠小宝':{
        'pw':'123456',
        'sex':'F',
        'shop':11323
    },
    'zhangsan':{
        'pw':'woaijiwang',
        'sex':'F',
        'shop':0
    },
    'Cook':{
        'pw':'zuixihuanjiwangkele',
        'sex':'M',
        'shop':32423
    }
}

#the imformation for shops
shop_list ={
    '10019':{
        "name":"小米手机旗舰店",
        "owner":"李昀锴",
        "goods":[
            {"id": "0001","name":"红米2","price":"1200"},
            {"id": "0002", "name": "MIX2", "price": "3999"},
            {"id": "0003", "name": "小米5", "price": "800"},
            {"id": "0004", "name": "小米6", "price": "1000"},
            {"id": "0005", "name": "小米电饭煲", "price": "399"},
            {"id": "0006", "name": "小米手环", "price": "79"}
        ],
        "state":"open"
    },
    '32423':{
        "name":"Apple旗舰店",
        "owner":"Cook",
        "goods":[
            {"id": "0001","name":"Iphone 7","price":"3900"},
            {"id": "0002", "name": "iPhone 8", "price": "4299"},
            {"id": "0003", "name": "iPhone X", "price": "8800"},
            {"id": "0004", "name": "MacBookPro", "price": "11399"},
            {"id": "0005", "name": "iMac", "price": "7900"},
            {"id": "0006", "name": "iWatch", "price": "2900"},
            {"id": "0007", "name": "iPad", "price": "3100"}
        ],
        "state": "open"
    },
    '11323':{
        "name":"三只松鼠",
        "owner":"鼠小宝",
        "goods":[
            {"id": "0001","name":"夏威夷果","price":"19.99"},
            {"id": "0002", "name": "山核桃", "price": "29.99"},
            {"id": "0003", "name": "牛板筋", "price": "49.99"}
        ],
        "state": "open"
    },
    '50344':{
        "name":"三星手机旗舰店",
        "owner":"小炸",
        "goods":[
            {"id": "0001","name":"NOTE7","price":"7900"},
            {"id": "0002", "name": "Galaxy Note8", "price": "8200"},
            {"id": "0003", "name": "显示器", "price": "3300"},
            {"id": "0004", "name": "内存条8G", "price": "500"}
        ],
        "state": "open"
    },
    '90231':{
        "name":"KFC旗舰店",
        "owner":"卡姆氏",
        "goods":[
            {"id": "0001","name":"吮指原味鸡*30","price":"169"},
            {"id": "0002", "name": "新奥尔良烤翅*20", "price": "145"},
            {"id": "0003", "name": "花生酱双层汉堡", "price": "22.98"},
            {"id": "0004", "name": "双层鸡腿堡套餐", "price": "35.99"},
            {"id": "0005", "name": "酸菜鸡块饭", "price": "24.5"},
            {"id": "0006", "name": "甜筒*30", "price": "78"}
        ],
        "state": "open"
    },
    '38943':{
        "name":"Python源码一体店",
        "owner":"小p",
        "goods":[
            {"id": "0001","name":"web网站python源码","price":"9999"},
            {"id": "0002", "name": "数据库python源码", "price": "2000"}
        ],
        "state": "open"
    },
    '21340':{
        "name":"专业PJ代写",
        "owner":"4.0",
        "goods":[
            {"id": "0001","name":"计网PJ","price":"6900"},
            {"id": "0002", "name": "数据结构PJ", "price": "1450"},
            {"id": "0003", "name": "操作系统PJ", "price": "5400"},
            {"id": "0004", "name": "计算机体系机构PJ", "price": "900"},
            {"id": "0005", "name": "保密管理概率PJ", "price": "1500"},
            {"id": "0006", "name": "数据库PJ", "price": "4000"},
            {"id": "0007", "name": "C++PJ", "price": "500"},
            {"id": "0008", "name": "数字水印PJ", "price": "2888"}
        ],
        "state": "open"
    },
    '24330':{
        "name":"卫尤辣条",
        "owner":"小作坊",
        "goods":[
            {"id": "0001","name":"手撕面筋","price":"5"},
            {"id": "0002", "name": "小辣条", "price": "0.9"},
            {"id": "0003", "name": "大面筋", "price": "2.8"},
            {"id": "0004", "name": "面筋大礼包", "price": "58.88"}
        ],
        "state": "open"
    },
    '92310':{
        "name":"聚美优品",
        "owner":"陈欧",
        "goods":[
            {"id": "0001","name":"芦荟胶","price":"29.8"},
            {"id": "0002", "name": "御泥坊面膜礼盒", "price": "199"},
            {"id": "0003", "name": "欧莱雅洗面奶", "price": "54"},
            {"id": "0004", "name": "BB霜", "price": "79.98"},
            {"id": "0005", "name": "眉笔", "price": "20"},
            {"id": "0006", "name": "护肤霜", "price": "28"},
            {"id": "0007", "name": "护手霜", "price": "16"},
            {"id": "0008", "name": "口红", "price": "188"},
            {"id": "0009", "name": "祛痘套装", "price": "389"}
        ],
        "state": "open"
    },
    '79123':{
        "name":"B站旗舰店",
        "owner":"2233",
        "goods":[
            {"id": "0001","name":"碧蓝航线立牌周边","price":"19.8"},
            {"id": "0002", "name": "应援灯牌", "price": "80"},
            {"id": "0003", "name": "小电视抱枕", "price": "58"},
            {"id": "0004", "name": "B站大会员1个月", "price": "19"}
        ],
        "state": "open"
    },
}

#the login_state info
login_info={}

#the shop visit list{"shopid":["userid","userid"]}
shop_visit={}

#the request function dict
request_function={
    "load_info":load_info,
    "login_check":login_check,
    "send_shoplist":send_shoplist,
    "exit_request":exit_request,
    "enter_shop":enter_shop,
    "leave_shop":leave_shop,
    "enter_own_shop":enter_own_shop,
    "show_custom":show_custom,
    "has_shop":has_shop
}




HOST = '10.105.69.173'
PORT = 62000

s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))

print('...waiting for message..')

while True:
    print('server waiting')
    data,address = s.recvfrom(1024)

    if not data:
        break

    data = json.loads(data)
    data = byteify(data)

    result = request_function[data["method"]](s,data,address)

    #write log
    output = open('log/log.txt', 'a')
    output.write(data["method"]+":"+result+" "+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n')
    output.close()