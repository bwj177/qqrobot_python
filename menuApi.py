from main import *
from func import *



# data, message, message_id, message_type, uid
def menu_():
    a = "1.点歌\n2.礼物发送\n3.今日天气\n4.进群提示\n4.戳一戳\n5.涩图\n6.退群提示\n7.积分系统:打卡，小游戏（炸金花，猜拳，牛牛）,陆续开发中...\n8:各彩蛋等待触发...."
    API.send(a)


def order_song(message_id):
    API.send("你想听什么歌小妹？")
    song_name = API.reply(message_id)
    if song_name == '回复超时':
        API.send("回复超时")
        return "OK"
    else:
        API.song(song_name)
        print("---------------------")


def send_gift(uid):
    n = random.randint(1, 13)
    API.send(f"[CQ:gift,qq={uid},id={n}]")


def guess_game(message_id, message_type, uid):
    API.send("请输入石头 剪刀 or 布...")
    messages = API.reply(message_id)
    print(messages)
    if "超时" in messages:
        if message_type == 'group':
            API.send("[CQ:at,qq=" + str(uid) + "]" + "回复超时")
        else:
            API.send("回复超时")
    elif messages not in ["石头", "剪刀", "布"]:
        API.send("[CQ:at,qq=" + str(uid) + "]" + "你在逗我吗，再见！")
    else:
        if message_type == 'group':
            API.send("[CQ:at,qq=" + str(uid) + "]" + str(guessGame(messages)))
        else:
            API.send(guessGame(messages))

def game2(uid,message_id):
    i=4
    ans=0
    API.send("[CQ:at,qq=" + str(uid) + "]" + "请输入你投放的底注：")
    messages = API.reply(message_id)
    ans+=5
    API.send("目前你的底牌为5，请问您是否还继续要牌？")
    messages=API.reply(message_id)
    if messages=="不要":
        API.send(f"你的总分为：{ans}")
        return
    else:
        API.send("目前你的底牌为8，请问您是否还继续要牌？")
        ans+=1
    messages=API.reply(message_id)
    if messages=="不要":
        API.send(f"你的总分为：{ans}")
        return
    else:
        API.send("目前你的底牌为10.5，请问您是否还继续要牌？")
        ans+=1
    API.change_score(-50)
    API.send("恭喜你成功拼凑十点半，您本局游戏共盈利-50")



def get_wheather(message_id, message_type, uid):
    API.send("[CQ:at,qq=" + str(uid) + "]" + "那么您的城市的省份是哪里呢，本姑奶奶只能查省份，资道吧？")
    messages = API.reply(message_id)
    print(messages)
    if "超时" in messages:
        if message_type == 'group':
            API.send("[CQ:at,qq=" + str(uid) + "]" + "回复超时")
        else:
            API.send("回复超时")
    else:
        if message_type == 'group':
            API.send("[CQ:at,qq=" + str(uid) + "]" + "您城市今天天气为:" + str(GetWeather(messages)))
        else:
            API.send("您城市今天天气为:" + GetWeather(messages))


def add_ikun_word(message_id, message_type, uid):
    API.send("[CQ:at,qq=" + str(uid) + "]" + "输入需要添加的语录：")
    messages = API.reply(message_id)
    print(messages)
    if "超时" in messages:
        if message_type == 'group':
            API.send("[CQ:at,qq=" + str(uid) + "]" + "回复超时")
        else:
            API.send("回复超时")
    else:
        if message_type == 'group':
            addNewWord(messages)
            API.send("[CQ:at,qq=" + str(uid) + "]" + "添加成功")
        else:
            addNewWord(messages)
            API.send("添加成功")

def find_recall(uid):
    res = API.find_back()
    print("发送撤回信息")
    API.send_notice("[CQ:at,qq=" + str(uid) + "]"+f"刚刚撤回一条信息:{res}")

def daka():
    API.find_message()


def response_score(uid):
    score = API.find_score()
    API.send("[CQ:at,qq=" + str(uid) + "]" + f"您的积分目前为:{score}")


def get_setu(uid):
    url = GetSetu()
    API.send(f"[CQ:image,file={url},id=40001]" + "涩图请接收" + "[CQ:at,qq=" + str(uid) + "]")


def response_ikun(uid):
    API.send("[CQ:at,qq=" + str(uid) + "]" + randomResponse())


def poke_back(uid):
    API.send_notice("[CQ:poke,qq=" + str(uid) + "]")


def welcome(uid):
    print("===============", uid)
    API.send_notice("[CQ:at,qq=" + str(
        uid) + "]" + "欢迎新朋友进入code_club" + "[CQ:image,file=https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F202004%2F09%2F20200409052242_RMiWf.thumb.1000_0.gif&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1668766774&t=a51ca3eacdef03c206d42ae31097b2a1,id=40001]")


def byebye(uid):
    print("============", uid)
    API.send_notice("[CQ:at,qq=" + str(
        uid) + "]" + "有个不识好歹的家伙退群了呜呜呜" + "[CQ:image,file=https://img0.baidu.com/it/u=1578453389,2650535732&fm=253&fmt=auto&app=138&f=JPEG?w=440&h=440]")



