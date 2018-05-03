# 森普网络商城设计文档



## 目录
* 需求分析和软件架构图
	* 需求分析
	* 软件架构
* 协议和报文设计
	* UDP协议
	* 报文设计
	* socket设计
* 功能设计
	* 客户端设计
		* 登陆
		* 用户功能
			* 消息机制
			* 购买商品
			* 发布新商品
			* 记录查看
			* 浏览商店
			* 退出商店
		* 注销
	* 服务端设计
		* 用户数据存储
		* 监听请求*
		* 商城管理功能
			* 开户
			* 店铺管理
			* 查看商城信息
			* 消息发送
* 窗口与逻辑交互设计
	* LoginWindow
	* ShoplistWindow
	* MsgBoxWindow(RecordingWindow）
	* InputWindow
* Github开发轨迹

## 需求分析和软件架构图
### 需求分析
网络商城客户端的需求主要是查看店铺信息，商品信息，购买商品，查看购买记录等，如果用户拥有虚拟商店，则用户还需要能发布新商品，查看店内顾客，查看销售记录，收取商城管理员发送的有关商品销售、店铺管理、顾客离店等关键信息。



网络商城服务端（管理员）端的需求是接收各类客户端发送的请求报文，同时由于管理员与服务端的嵌合性，因此服务端进程的主进程为窗口程序，而子线程为监听请求的程序。服务端的需求主要集中在对店铺和用户的管理，以及信息的查询和消息通知的发送。



### 软件架构
由于此网络商城有客户端与服务器端两种，由于是课程PJ，我们将服务器端的身份检验简化了，不同于客户端的身份验证，服务端可以直接开启运行。且为了简单起见，所有的信息均存储在变量中，服务端进程初次运行时，其变量会有初始值，包括用户信息，商店信息等，不同的信息之间的变量依赖有服务端进程完成，具体架构形式如下图所示：


## 协议和报文设计

### UDP协议
UDP协议是面向无连接的、不可靠的一种运输层协议，但是考虑到我们的网络商城是运行在丢包率很小的环境下，并且服务器端和客户端均是运行在本地（虽然开发过程中服务器端放在云服务器上进行测试，且测试亦能通过），即127.0.0.1.这使我们的运行更简洁。

此外，UDP的无连接性也是我们所看中的，我们将每个客户端的请求抽象为单个的数据报文，通过UDP发送给服务器端，并等待接收服务器端的请求结果。

### 报文设计
客户端的报文格式统一为：

`{"method":"type","data1":"xx","data2":"xx"....}`

- method 为客户端的请求类型，服务器端将按照此字段中的内容对请求进行分发，调用不同的服务端函数完成请求
- "data1","data2"...是请求附带的参数信息，这些参数信息提供给服务器方，以告知它接下来该返回什么信息。例：用户希望进入某家店铺，则用户的请求报文的参数项应该包含须进入的店铺ID，访问人ID
- 所有的报文均使用python的json库中的dumps函数进行json格式化后发送

```
msg = json.dumps(msg)
```

服务器端的回复报文格式不全相同，主要有如下几类：

- 返回一个结果值的：如Success,Fail;
- 返回一个被json化的字典变量，如某个商店信息，商品信息;
- 返回一个被json化的列表变量，如某用户的登陆记录;
- 返回一个被json化的列表和字典嵌套的变量，如所有商店的信息;

服务端报文这样设计的原因是，对于不同的请求的答复内容不相同，其为了便于客户端对接收的数据便于处理，故按照请求的类型进行答复

### socket设计
socket部分是此商城实现的核心，对于客户端来说，其主要是以发送为主；由于采用的是UDP协议，因此这部分的代码为：

```
host = '127.0.0.1'
port = 62000
s = socket(AF_INET, SOCK_DGRAM)
s.settimeout(1)
while True:
    info = {"method": "exit_request"}
    message = json.dumps(info)
    
    s.sendto(message.encode(encoding='utf-8'),
    (host,port))
    
    try:
        data = s.recvfrom(1024)
    except IOError or timeout:
    
        #some tips for user
        self.tip_window = MsgWindow("", "网络错误了")
        self.close()
        return
```

由于采用UDP，所以在创建套接字时采用的是SOCK_DGRAM参数，即用户数据报的套接字；此外，由于需要考虑到服务端不在线或网络问题，所以我们设置了一个1s的超时时间，由于while(1)的存在，我们会不断向服务端发送相同的请求，直到我们得到服务器的回应或者达到了超时时间又或者出现IO错误，这些异常都会被捕捉，导致程序提前结束，并将此情况通过弹窗告知用户

之后函数将会使用套接字从缓冲区读取的数据，如商店数据、顾客数据、商品信息等，并交付给其他函数进行进一步的处理

## 客户端设计

### 登陆程序
登陆程序的主要作用是检查用户的ID与密码是否匹配，这里为了方便用户使用，用户将使用用户名作为登陆的依据（虽然服务器也会为用户分配一个唯一的user_id)，用户需要输入密码和用户名，这里我们使用之前的socket创建方法，发送如下的报文


```info = {"method":"login_check","id": user_id, "pw": user_pw_md5}```


其中，为了安全性，我们对用户密码进行了md5加密，在服务端对存储的用户信息的用户名和密码的md5值进行比较，有如下三种情况:

- Success : 用户名存在且密码匹配，准许登陆
- Fail : 用户名存在但密码不匹配
- No_user : 用户名不存在

第一种情况，会调用用户主界面的窗口创建函数，并关闭此登录窗口，传递用户名信息给主界面窗口，用于初始信息的加载：


```
self.shoplist_window = ShoplistWindow(user_id, address)
self.close()
self.shoplist_window.show()
```

其余两种情况都会使用户停留在登录界面，并显示相应的提示图片


```
pixmap = QPixmap(":/img/wrong_pw.png")
self.net_error.setPixmap(pixmap)
```

### 用户功能
#### 消息机制
消息机制是用户功能中比较重要的一点，对于进入用户界面的进程进程，会为其分配一个新的字典变量用于存储收到的消息；此外，进程开始时，会新建一个进程，执行接收消息的函数，该函数会创建一个新的socket，并向服务端发送一条请求，以告知服务器该用户上线，可以向其发送消息了，这个socket一直不会被关闭，直到它的父线程结束后，它才会被关闭，之后服务器将会在需要的时候利用此套接字向用户发送消息；

消息分为两种，一种是在用户离线时收到的消息，这部分暂存在服务端进程的一个待发消息的变量中，当用户首次发起加载首页信息时，服务端会检查该变量中是否有当前用户的待发送消息，如果有立即发送给他；另一种是用户在线时，如果收到了相应的消息，服务端则会直接发送给用户；

当用户收到信息时，会给客户进程中的消息变量追加一条新的记录，并且以显示的方法告知用户，用户可以根据需要查看。


```
#recvfrom message function
    def listen_msg(self,user):
        s = socket(AF_INET, SOCK_DGRAM)
        host = '127.0.0.1'
        port = 62000
        info = {"method":"listen","user":user}
        message = json.dumps(info)
        while True:
            s.sendto(message.encode(encoding='utf-8'),
            			(host,port))
            try:
                data ,(host,port)= s.recvfrom(1024)
            except IOError:
                break
            data = json.loads(data)

            # some tips to tell the user
            self.modify_msgbox(data)
            continue
```  

#### 购买商品
由于不考虑商店的库存情况，因此对于购买行为来说，通常都是成功的（除服务端进程未运行）；对于顾客来说，通过输入件数后,单击"剁手按钮",则会调用购买函数,会根据购买按钮的不同，给购买函数不同的参数，参数则为商品列表的第几项，其报文为：


	info = {"method":"buy_goods", 
                 "goods_id":info_get[str(i)+"g_id"](),
                 "goods_name":info_get[str(i)+"g_name"](),
                 "user":self.username.text(),
                 "num":info_get[str(i)+"_num"](),
                 "shop_id":self.now_shop.text()}
               

购买成功后，服务端则会发回相应的报文，内容包括购买的订单号和购买物的具体信息，其中订单号是由店铺ID，商品ID，购买件数，购买时间的散列值和4位的随机码构成的;客户端会以弹窗的形式告知用户，用户和店主也会收到含有购买（销售）信息的消息

#### 发布新商品
该功能仅针对拥有虚拟店铺的用户使用，页面初次加载或从商店退出时都会检测当前用户是否有虚拟商店（因为有可能是管理员为其开了新店），如果没有虚拟商店，则不会显示对应的发布商品入口。
发布新商品时，商品id不能与已有的商品ID重复，否则服务端会提示添加失败，此功能的请求报文为：


	info = {"method":"add_goods",
                "id":shop_id,
                "goods_id":goods_id,
                "goods_name":goods_name,
                "goods_price":goods_price}
                
#### 记录查看
对于顾客而言，可以查看的记录包括：登陆记录，购买记录，而拥有虚拟商店的店主则多了销售记录；用户界面均通过相应的按钮调用记录查看函数，记录查看均会创建一个新的窗口用于展示记录，创建时提供需要展示的记录类型，新窗口将会根据显示类型对窗口进行初始化设置

	
	#different type of init function
	init_f={"buy":self.init_buy,
               "sold":self.init_sold,
               "login":self.init_login,
                'custom':self.init_custom,
                'user':self.init_user}

    init_f[type](msg)
    
    
对于每一类记录的查看，客户端会调用不同的函数发送不同的函数向服务端请求结果.

#### 浏览商店
浏览商店的逻辑功能设计如下：




由于窗口上方可以通过输入店铺ID进入某商店，因此存在用户尚在A店铺时利用该输入栏进入B店铺，这个行为被定义为离开了A商店，即试图查看A商店顾客的请求将不会返回此用户的信息，故需先调用离开商店的函数用于确保删去此用户的“逛店信息”

另外，按照约定，店铺所有者进入自己的店铺不应该被定义为顾客的“逛店”行为，因此从“我的店铺”进入的用户应该先调用enter\_own\_shop_request()函数(用户有店铺的前提下),以确保用户不会被记录在顾客名单中

#### 退出商店
退出商店的形式有两种，一种是用户主动点击界面上的回到主页的按钮，我们称之为主动退出；另一种则是由于窗口关闭或用户注销而引起的被动退出；前一种通过客户端主动调用leave_shop()函数退出，后一种则有服务器端的注销函数中直接修改“逛店信息”的变量完成

### 注销
用户注销的方式有两种，一种是通过单击按钮调用exit_request()函数，此退出函数会向服务器端发送离线请求的报文；另一种是用户关闭窗口，借助QT的窗口关闭事件，在此事件中调用退出函数；服务端将根据注销请求清除此用户的部分数据，例如浏览商店的数据，并且会修改用户的在线状态，这可能会影响其后续接收消息的情况

*值得注意的是，很有可能出现这样的情况：客户端进程在用户登录状态下失去了网络连接，那么这个时候用户无论是关闭窗口还是单击退出按钮都不能向服务器端发送报文，这可能会导致用户状态不正确的情况，但考虑到此次课程PJ对用户同步在线的机制并不会显著影响其他的功能，且对于都运行在127.0.0.1的两个进程来说，这并不会导致这种问题（除非服务端进程被关闭）,因此本系统没有设计定时检查用户的在线情况，而是依靠用户显式的退出来修改在线情况。

## 服务端设计
### 用户数据管理
在客户端进程设计时，所有的数据均以变量的形式记录在sever.py文件中，这就导致了一个问题：就是对于所有的操作均是“一次性的”，也就是对于每次服务端重新启动，商城的状态都会重新初始化为我们预先定义的结果，虽然我们可以将这些信息以文本的形式存储在TXT文件中以保证能在服务端每次运行时能保持状态，即使用pickle库对变量进行序列化保存，需要时在对其进行反序列化操作，但是考虑到这是网络课程的PJ,我们的目标并非是实现一套持久性的数据系统，所以权衡之后使用了这样的方式

在sever.py中一共有如下几个用户数据的变量，其类型和内容如下表所示(字典均省略了键值部分,*标注的变量是在进程运行前有初值的变量)：

 
| 变量名称       | 变量类型  | 变量内容 | 
|:------------: |:---------------:| :------------:|
| message| 字典 | 存储发送给离线用户的消息 |
| user_infomation\*| 字典|存储用户信息 |
| shop_list\* | 字典| 存储店铺信息|
| login_info | 字典嵌套列表|存储用户的登陆信息|
| shop_visit | 字典嵌套列表|存储用户逛店信息|
| sold_recording | 字典嵌套列表 |存储销售信息|
| bought_recording | 字典嵌套列表|存储购买信息|
| socket_user | 字典|存储用户用于收信息的套接字|


| 变量名称       | 变量格式|
|:------------: |:------------:|
| message|{"user":[msg1,msg2]}|
| user_infomation\*|{"user":{"userid","pw","shop":}}|
| shop_list\* |{"shop":{"id","owner","goods","state"}}|
| login_info |{"user":{"state","history":["time","address"]}}|
| shop_visit |{"shop":{"owner","goods","id","state"}}|
| sold_recording|{'shop':[{'id','shopping_num','num','time','user'}]}|
| bought_recording |{'user':[{'shop_name','shopping_num','num','time','goods_name'}]}|
| socket_user|{"user":socket}|

### 监听请求
客户端的一个最重要的功能就是监听客户端发送的请求报文，当服务端进程启动后，会申请一个新的子线程用于处理用户的请求，该线程会一直运行以确保能收到客户端的请求：


```
#the main listen function
def listen_request():
    HOST = '127.0.0.1'
    PORT = 62000

    s = socket(AF_INET, SOCK_DGRAM)
    s.bind((HOST, PORT))

    #print('...waiting for message..')

    while True:
        #print('server waiting')
        data, address = s.recvfrom(2048)

        if not data:
            continue

        data = json.loads(data)

        result = request_function[data["method"]](s, data, address)

        # write log
        output = open('log/log.txt', 'a')
        
        log = data["method"]
        +":" + result + " " 
        + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n'
        
        print(log)
        output.write(log)
        output.close()
```

该函数将在进程存在的过程中一直运行，处理分发客户端的请求，并将每次的监听结果写入日志文件，用于事后的检查；这里我们还使用了一个字典来存储各类处理的函数，用于直接调用，主进程为窗口进程，窗口进程创建时会分配一个子线程用于请求的监听。


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

### 商城管理功能
#### 开户
由于可能会新增用户，则需要管理员通过开户功能增添新的用户，由于用户ID必须是唯一的（且用户ID还将是店铺ID），因此管理员在设置新用户ID时必须考虑到这一点。因此服务端将会检查开户的报文信息中的user\_id项是否是一个新的项，如果与现有的用户ID重复，则会发回添加失败的信息告知服务端窗口，提示管理员

```
    def add_user(self):
        if self.id.text() == "":
            self.id.setText("请输入用户id")
            return
        else:
            id = self.id.text()

        if self.name.text() =="":
            self.name.setText("请输入用户密码")
            return
        else:
            pw = self.name.text()

        if self.price.text() =="":
            self.price.setText("请输入用户名称")
            return
        else:
            name = self.price.text()
        for key in user_infomation:
            if str(user_infomation[key]['user_id']) == id:
                self.msgwindow = MsgWindow("", "用户" + name + "添加失败！(ID重复)")
                self.close()
                return
        user_infomation[name] = {}
        user_infomation[name]['user_id'] = int(id)
        user_infomation[name]['pw'] = pw
        user_infomation[name]['shop'] = 0
```

#### 店铺管理
店铺管理主要是新开店铺和关闭店铺，所有用户的店铺均使用user\_info中shop键表示，其中该键键值为0时表示该用户尚不拥有任何一家店铺，而shop键键值不为0时，表示用户拥有店铺，键值为店铺ID；店铺的状态有两种，存储在shop\_list变量中，若店铺为正常状态，其state字段为open，若管理员关闭了此店铺，该字段变成close；state字段值为close的店铺将不会被展示在商城中，且店铺所有者和顾客均不能进入，直到管理员重新为该店铺拥有者新建店铺，此时的店铺将为空（即不包含任何商品）;值得注意的是，无论是新开店铺还是关闭店铺店铺时，服务端都需要发消息通知店铺拥有者，关闭店铺时还需要通知正在店铺中逛的用户

```
    def close_shop(self):
        #get input shop id
        ...
        
        if shop_list.__contains__(id):
            shop_list[id]['state'] = 'close'
            self.msgwindow = MsgWindow("", "关闭成功")
            self.close()

             #send message
		 		...            
```

```
 def add_shop(self):
        #get the input infomation
        ...
        
        for key in user_infomation:
            if user_infomation[key]['user_id'] == int(id):
                owner = key
                flag = 1
                break

        if flag == 0:
            self.msgwindow = MsgWindow("", "店铺" + name + "添加失败！(ID不存在)")
            self.close()
            return

        shop_list[id] = {}
        shop_list[id]['name'] = name
        shop_list[id]['owner'] = owner
        shop_list[id]['goods'] = []
        shop_list[id]['state'] = "open"
        user_infomation[owner]['shop'] = int(id)

        self.msgwindow = MsgWindow("", "店铺" + name + "添加成功")
        self.close()
        
		 #send message
		 ...   
```

#### 查看商城信息
查看商城信息，包括店铺信息，商品信息和用户信息，商城管理用直接通过点击按钮触发了这些查看的行为，这些查看都使用相似的函数完成，函数主要是新建一个记录展示窗口并获取对应变量中的内容，由于所有信息数据的变量都存储在服务端进程，因此查看信息不需要发送请求报文。

#### 消息发送
消息发送是服务端的另一个主要的功能，正如前文所述，很多的操作都需要管理员向用户发送相关信息，结合之前我们所提及的两种消息（用户离线时的消息和用户在线时的消息），在服务端为了简便这两种消息的发送，我们定义了两个与消息发送相关的函数接口：

```
def send_message_manage(content,recv,send)
def send_message(send,content,time,address,s)
```

前者仅有三个参数，我们将此函数定义为消息发送处理函数，该函数作为其它需要发送消息的公开的接口，因为调用此函数的其他函数不需要提供有关接收方的任何在线或离线的信息;其中所输入的三个参数均为list类型的变量（content变量的每一项为字典变量，格式为{"title":"xx","text":"xxx"}），所有有发送请求的函数，只需要简单的提供消息的内容和接收人与发送人的信息即可，然后将这些信息作为参数来调用发送消息处理函数；

该函数会遍历recv变量，筛选出其中在线的用户，对于这部分用户直接调用send\_message()函数，该函数需要用到的参数是发送方、消息内容、发送时间戳、在线的接收方的套接字和地址，之后在此函数中直接利用套接字的send\_to()函数向对应套接字发送信息；

而对于当前离线的用户，则先将消息和当前的时间（作为发送时间）存储于待发送的消息变量message中，当该用户上线时，用户会向服务端发送加载商城初始化信息的请求，（在此之前用户已经向服务端发送了接受消息的请求，故服务端已经有了其套接字）服务端在此请求中调用send\_message()函数将该用户待发送的信息依次发送给用户。值得注意的是，这个函数每次只能发送一条消息

而send_message函数相当于一个私有的函数，它只在上述两种情况下被调用，其他有发送消息需求的函数则不会直接调用此函数



## 窗口与逻辑交互设计
整个森普网络商城有四类基础的窗口类(不含派生的窗口)，其中它们的逻辑调用关系如下图：

其中MsgBoxWindow和RecordingWindow使用了同一个UI布局，不同的是，后者可以根据不同的参数创建不同的窗口展示不同类型的数据，后文还会详细讲解

### LoginWindow
登录窗口是客户端进程的启动入口，是作为用户身份核验的窗口；此窗口的设计逻辑是检查用户的输入是否符合输入的要求，并将输入的信息以报文的形式发送给服务器端，收到核验成功的报文后，销毁登陆窗口，创建用户主界面的窗口，并进入该窗口，表明登陆成功；否则就予以用户错误信息的提示

### ShoplistWindow
该窗口集合了客户端和服务端的几乎所有的功能，二者都是以该窗口作为基础窗口生成的;其中，诸如商店信息和商品信息，包括其他操作的入口控件都在此界面中，用户可以实时地获取这类信息并会显示在该窗口上;而需要用户输入信息或显示记录信息等操作，则会创建下面的两类窗口；

该窗口还具有换页功能，窗口底部显示了当前的页码信息以及数据总数，用户可以根据页面信息自由地进入下页或前页;这部分逻辑的实现是基于一个页码label用于记录当前的页数，当前页数若为第一页就隐藏上一页的按钮，若为最末页就隐藏下一页按钮

### MsgBoxWindow（RecordingWindow）
这类窗口适用于展示用户消息和相关的记录信息，在RecordingWindow中我们设计了一个字典用于存储各类窗口初始化的函数，用户可以根据创建窗口的类型来使用窗口的初始化函数，对不同的记录初始化出不同类型的窗口

### InputWindow
此窗口主要用于信息的输入，包括用户给店铺增加新商品，管理员开户、增加新店铺、关闭店铺等操作都需要信息的输入，故此类操作都需要创建输入窗口，其发送报文的函数也在这类窗口的逻辑代码部分

