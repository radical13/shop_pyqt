# -*- coding: utf-8 -*-

from socket import *
import json
import hashlib
import datetime
import time
import random

#These are listen request function#

def send_shoplist(s,data,address):

    msg = {}
    for key in shop_list:
        if shop_list[key]["state"] == "open":
            msg[key] = {"name":"","owner":""}
            msg[key]["name"] = shop_list[key]["name"]
            msg[key]["owner"] = shop_list[key]["owner"]
    msg = json.dumps(msg)
    if s.sendto(str.encode(msg), address) != 0:
        return "0"
    else:
        # SEND FAIL
        return "2"
def login_check(s,data, address):

    user_id = data["id"]
    user_pw = data["pw"]

    if user_infomation.get(user_id, "NULL") == "NULL":
        if s.sendto(b'NO_USER', address)!=0:
            return "1"
        else:
            #SEND FAIL
            return "2"
    pw_m = hashlib.md5()
    pw_m.update(user_infomation[user_id]["pw"].encode("utf-8"))

    # check the password
    user_pw_md5 = pw_m.hexdigest()

    if user_pw_md5 == user_pw:
        if s.sendto(b'SUCCESS', address) != 0:
            # update login info，record the login log
            if login_info.__contains__(user_id):
                login_info[user_id]["state"] = True
                info = {"time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "add": address}
                login_info[user_id]["history"].append(info)
            else:
                login_info[user_id] = {"state": "", "history": []}
                login_info[user_id]["state"] = True
                info = {"time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "add": address}
                login_info[user_id]["history"].append(info)
            return "0"
        else:
            #SEND FAIL
            return "2"
    else:
        if s.sendto(b'FAIL', address) != 0:
            return "1"
        else:
            # SEND FAIL
            return "2"
def exit_request(s,data, address):
    if login_info.__contains__(data["user"]):
        login_info[data["user"]]["state"] = False
        for key in shop_visit:
            for i in range(len(shop_visit[key])):
                if shop_visit[key][i] == data['user']:
                    shop_visit[key].remove(data['user'])
                    print(shop_visit[key])
                    # send leave tip
                    content = [{'title': '离店通知', 'text': data['user'] + "用户" + "离开了您的店"}]
                    recv = [shop_list[key]['owner']]
                    send = ["商城管理员：小森"]
                    send_message_manage(content, recv, send)
                    break
        if s.sendto(b"0", address)!=0:
            return "0"
        else:
            #SEND FAIL
            return "2"
    else:
        if s.sendto(b"1", address) != 0:
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
            if s.sendto(str.encode(msg), address) != 0:
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
             if s.sendto(str.encode(msg), address) != 0:
                 return "0"
             else:
                 # SEND FAIL
                 return "2"
    else:
        msg = {"state": "null", "goods": []}
        msg = json.dumps(msg)
        if s.sendto(str.encode(msg), address) != 0:
            return "0"
        else:
            # SEND FAIL
            return "2"
def leave_shop(s,data,address):
    if data["user"] == shop_list[data["id"]]["owner"]:
        msg = "0"
        if s.sendto(str.encode(msg), address) != 0:
            return "0"
        else:
            # SEND FAIL
            return "2"
    else:
        if shop_visit.__contains__(data["id"]):
            if data["user"] in shop_visit[data["id"]]:
                shop_visit[data["id"]].remove(data["user"])
                msg="0"

                #send leave tip
                content=[{'title':'离店通知','text':data['user']+"用户"+"离开了您的店"}]
                recv=[shop_list[data['id']]['owner']]
                send=["商城管理员：小森"]
                send_message_manage(content,recv,send)

                if s.sendto(str.encode(msg), address) != 0:
                    return "0"
                else:
                    # SEND FAIL
                    return "2"
            else:
                msg = "1"
                if s.sendto(str.encode(msg), address) != 0:
                    return "0"
                else:
                    # SEND FAIL
                    return "2"
        else:
            msg = "1"
            if s.sendto(str.encode(msg), address) != 0:
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
        if s.sendto(str.encode(msg), address) != 0:
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
        if s.sendto(str.encode(msg), address) != 0:
            return "0"
        else:
            # SEND FAIL
            return "2"
    else:
        msg[id] = []
        msg = json.dumps(msg)
        if s.sendto(str.encode(msg), address) != 0:
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
        user_id = data['user']
        msg = user_infomation[user_id]
        msg = json.dumps(msg)
        if s.sendto(str.encode(msg), address) != 0:
            # send the msg in buffer:
            if message.__contains__(user_id):
                for i in range(len(message[user_id])):
                    msg = message[user_id][i]
                    send_message(msg['send'],
                                 msg['content'],
                                 msg['time'],
                                 socket_user[user_id]['add'],
                                 socket_user[user_id]['socket'])
                message.pop(user_id)
            return "0"
        else:
            # SEND FAIL
            return "2"
    else:
        msg={}
        msg = json.dumps(msg)
        if s.sendto(str.encode(msg), address) != 0:
            return "1"
        else:
            # SEND FAIL
            return "2"
def buy_goods(s,data,address):
    goods_id = data['goods_id']
    goods_name = data['goods_name']
    shop_id = data['shop_id']
    user=data['user']
    num = data['num']
    time_now = int(time.time())

    time_local = time.localtime(time_now)

    dt = time.strftime("%Y%m%d%M", time_local)

    #the number of this shopping
    shopping_num=dt + shop_id + goods_id + str(random.randint(1000, 9999))

    msg = {'result':'success','shopping_num':shopping_num}
    msg = json.dumps(msg)
    if s.sendto(str.encode(msg), address) != 0:

        #write recording
        r_s = {'id':goods_id,
               'shopping_num':shopping_num,
               'num':num,
               'time':time.strftime("%Y-%m-%d %H:%M:%S",time_local),
               'user':user,
               'goods_name': goods_name}
        r_u = {'shop_name':shop_list[shop_id]['name'],
               'shopping_num':shopping_num,
               'num':num,
               'time':time.strftime("%Y-%m-%d %H:%M:%S",time_local),
               'goods_name':goods_name}

        if sold_recording.__contains__(shop_id):
            sold_recording[shop_id].append(r_s)
        else:
            sold_recording[shop_id] = []
            sold_recording[shop_id].append(r_s)

        if bought_recording.__contains__(user):
            bought_recording[user].append(r_u)
        else:
            bought_recording[user] = []
            bought_recording[user].append(r_u)

        #send msg to owner
        content = [{"title":"用户购买通知",
                   "text":user+"用户购买了"+num+"件"+goods_name+",订单号为:"+shopping_num+"，请记得发货哦！"}]
        send = ["商城管理员：小森"]
        recv = [shop_list[shop_id]['owner']]
        send_message_manage(content, recv, send)

        #send msg to user
        content1 = [{"title": "购买成功",
                    "text":  "您购买了" + num + "件" + goods_name + ",订单号为:" + shopping_num + "，请记得查收哦！"}]
        send1 = ["商城管理员：小森"]
        recv1 = [user]
        result = send_message_manage(content1, recv1, send1)

        return "0"
    else:
        # SEND FAIL
        return "2"
def add_socket(s,data,address):
    if socket_user.__contains__(data['user']) == False:
        socket_user[data['user']] = {}

    socket_user[data['user']]['socket'] = s
    socket_user[data['user']]['add'] = address
    return '0'
def send_logininfo(s, data, address):
    if login_info.__contains__(data['user']):
        msg = login_info[data['user']]['history']
    else:
        msg = []
    msg = json.dumps(msg)
    if s.sendto(str.encode(msg), address) != 0:
        return "0"
    else:
        # SEND FAIL
        return "2"
def send_shopping_recording(s, data, address):
    if bought_recording.__contains__(data['user']):
        msg = bought_recording[data['user']]
    else:
        msg = []
    msg = json.dumps(msg)
    if s.sendto(str.encode(msg), address) != 0:
        return "0"
    else:
        # SEND FAIL
        return "2"
def send_sold_recording(s, data, address):
    if sold_recording.__contains__(str(user_infomation[data['user']]['shop'])):
        msg = sold_recording[str(user_infomation[data['user']]['shop'])]
    else:
        msg = []
    msg = json.dumps(msg)
    if s.sendto(str.encode(msg), address) != 0:
        return "0"
    else:
        # SEND FAIL
        return "2"
def add_goods(s,data,address):
    flag = 0
    if shop_list.__contains__(data['id']):
        for i in range(len(shop_list[data['id']]['goods'])):
            if shop_list[data['id']]['goods'][i]['id'] == data['goods_id']:
                info = {"result": "id_fail"}
                flag =1
                break
        if flag == 0:
            good = {}
            good['id'] = data['goods_id']
            good['name'] = data['goods_name']
            good['price'] = data['goods_price']
            shop_list[data['id']]['goods'].append(good)
            info = {"result" : "success"}

            #send msg to the custom in this shop
            if shop_visit.__contains__(data['id']):
                recv = shop_visit[data["id"]]
                send =[]
                content=[]
                for i in range(len(recv)):
                    send.append(shop_list[data['id']]['name'])
                    c = {}
                    c['title'] = '新商品上架通知'
                    c['text'] = shop_list[data['id']]['name']+"店上架了新商品："+data['goods_name']+",单价为:"+data['goods_price']
                    content.append(c)
                send_message_manage(content,recv,send)
    else:
        info = {"result" : "fail"}
    msg = json.dumps(info)
    if s.sendto(str.encode(msg), address) != 0:
        return "0"
    else:
        return "2"

# These are request fuction#

#this function is to manage the message,it can divide different message situation:
#If the recv not online,we just add the msg on our server
#Parameter#
#recv:root send msg to some users for some tips:list['user1','user2'...]
#content:the msg should be send:list['content1','content2'...]
#send:in fact,all the send are root,but we can use this parameter is just send of form
def send_message_manage(content,recv,send):
    #the send result,0 is success,1 is fail
    result=[]

    #the user online or not?
    for i in range(len(recv)):
        if (login_info.__contains__(recv[i]) == False) or (login_info[recv[i]]['state'] == False):
            msg = {}
            msg['send'] = send[i]
            msg['time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            msg['content'] = content[i]
            if message.__contains__(recv[i]):
                message[recv[i]].append(msg)
            else:
                message[recv[i]]=[]
                message[recv[i]].append(msg)
            result.append(0)
        else:
            address = socket_user[recv[i]]['add']
            s = socket_user[recv[i]]['socket']
            if send_message(send[i],content[i],"",address,s) == 0:
                result.append(0)
            else:
                result.append(1)

    return result

#this function is the true function to send a single message
def send_message(send,content,time,address,s):
    #when time is not null, the message should be send to the just logined user
    if time=="":
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg={}
    msg['send'] = send
    msg['time'] = time
    msg['content'] = content

    msg = json.dumps(msg)
    if s.sendto(str.encode(msg), address) != 0:
        return 0
    else:
        # SEND FAIL
        return 2

def byteify(input):
        if isinstance(input, dict):
            return {byteify(key): byteify(value) for key, value in input.items()}
        elif isinstance(input, list):
            return [byteify(element) for element in input]
        elif isinstance(input, str):
            return input.encode('utf-8')
        else:
            return input

#store the messge wait to send
#{"recv":[{"send":"","time":"","content":{"title":"","text":""}}]}
message = {}

#the imformation for registered users
user_infomation = {
    'hushiyang':{
        'pw':'KaJe2008',
        'sex':'M',
        'shop':0,
        'user_id':31241
    },
    '鼠小宝':{
        'pw':'123456',
        'sex':'F',
        'shop':11323,
        'user_id':11323
    },
    'zhangsan':{
        'pw':'woaijiwang',
        'sex':'F',
        'shop':0,
        'user_id':13232
    },
    'Cook':{
        'pw':'zuixihuan',
        'sex':'M',
        'shop':32423,
        'user_id':32423
    },
    '李昀锴':{
            'pw':'zuixihuanjiwang',
            'sex':'M',
            'shop':10019,
            'user_id':32423
        },
    '小炸':{
            'pw':'woaijiwang',
            'sex':'M',
            'shop':50344,
            'user_id':50344
        },
    '卡姆式':{
            'pw':'woaijiwang',
            'sex':'M',
            'shop':90231,
            'user_id':90231
        },
    '小p':{
            'pw':'woaijiwang',
            'sex':'M',
            'shop':38943,
            'user_id':38943
        },
    '4.0':{
            'pw':'woaijiwang',
            'sex':'M',
            'shop':21340,
            'user_id':21340
        },
    '小作坊':{
            'pw':'woaijiwang',
            'sex':'M',
            'shop':24330,
            'user_id':24330
        },
    '陈欧':{
            'pw':'woaijiwang',
            'sex':'M',
            'shop':92310,
            'user_id':92310
        },
    '2233':{
            'pw':'woaijiwang',
            'sex':'M',
            'shop':79123,
            'user_id':79123
        }
}

#the imformation for shops
shop_list = {
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
login_info = {}

#the shop visit list{"shopid":["userid","userid"]}
shop_visit = {}

#the shop sold recording{'shop':[{'id':'','shopping_num':'','num':'','time':'','user':''}]}
sold_recording = {}

#the user bought recording{'user':[{'shop_name':'','shopping_num':'','num':'','time':'','goods_name':''}]}
bought_recording = {}

#the long connect socket for send message{"user1":{'socket':socket,'add':address}
socket_user = {}

#the request function dict
request_function = {
    "load_info":load_info,
    "login_check":login_check,
    "send_shoplist":send_shoplist,
    "exit_request":exit_request,
    "enter_shop":enter_shop,
    "leave_shop":leave_shop,
    "enter_own_shop":enter_own_shop,
    "show_custom":show_custom,
    "has_shop":has_shop,
    "buy_goods":buy_goods,
    "send_logininfo":send_logininfo,
    "send_sold_recording":send_sold_recording,
    "send_shopping_recording":send_shopping_recording,
    'listen':add_socket,
    "add_goods":add_goods
}

#the main listen function
def listen_request():
    HOST = '127.0.0.1'
    PORT = 62000

    s = socket(AF_INET, SOCK_DGRAM)
    s.bind((HOST, PORT))

    print('...waiting for message..')

    while True:
        print('server waiting')
        data, address = s.recvfrom(2048)

        if not data:
            continue

        data = json.loads(data)

        result = request_function[data["method"]](s, data, address)

        # write log
        output = open('log/log.txt', 'a')
        log = data["method"] + ":" + result + " " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print(log)
        output.write(log)
        output.close()

