import json
import sqlite3
import time
from flask import Flask, request
import requests
import menu

app = Flask(__name__)



class API:
    @staticmethod
    def send(message):
        print(message)
        data = request.get_json()
        message_type = data['message_type']
        if 'group' == message_type:
            group_id = data['group_id']
            params = {
                "message_type": message_type,
                "group_id": str(group_id),
                "message": message
            }
        else:
            user_id = data['user_id']
            params = {
                "message_type": message_type,
                "user_id": user_id,
                "message": message
            }
        url = "http://127.0.0.1:5700/send_msg"

        requests.get(url, params=params)

    @staticmethod
    def send_notice(message):
        data = request.get_json()
        print('-------', data)
        group_id = data['group_id']
        print(message)
        params = {
            "message_type": "group",
            "group_id": str(group_id),
            "message": message
        }
        print("==============", params["group_id"])
        url = "http://127.0.0.1:5700/send_msg"

        requests.get(url, params=params)

    @staticmethod
    def save_message():
        data = request.get_json()
        uid = data['user_id']
        message = data['message']
        message_id = data['message_id']
        send_time = data['time']
        message_type = data['message_type']
        if message_type == 'group':
            group_id = data['group_id']
        else:
            group_id = "无"
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        c.execute(
            "insert into message(QQ, message, message_id, send_time, message_type, group_id) values (?, ?, ?, ?, ?, ?)",
            (uid, message, message_id, send_time, message_type, group_id))
        conn.commit()
        conn.close()

    @staticmethod
    def find_message():
        data = request.get_json()
        uid = data['user_id']
        send_time = data['time']
        group_id = data['group_id']
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        c.execute("select count(QQ) from message where message = '打卡' ")
        result = c.fetchone()
        print(f"result:{result}")
        if result == 0:
            c.execute(
                "insert into score(QQ,score,group_id) values(?,?,?)",(uid,1000,group_id)
            )
            API.send("打卡成功！")
        else:
            c.execute("select send_time from message where message = '打卡'")
            result = c.fetchone()
            print(f"上一次发送打卡时间为{result}")
            nowtime =time.time()
            t = int(nowtime)-int(result[0])
            print(t)
            if t<86400000:
                API.send("打卡失败，您已经打过卡了！！")
            else:
                c.execute("select score from score where QQ=?",(uid,))
                result = c.fetchone()
                print(result)
                result=result[0]
                result+=1000
                c.execute("update score set score = ? where QQ = ?",(result,uid))
                API.send("打卡成功！")
        conn.commit()
        conn.close()

    @staticmethod
    def find_back():
        data = request.get_json()
        uid = data['user_id']
        send_time = data['time']
        group_id = data['group_id']
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        c.execute("select message from message where QQ =?  order by send_time desc limit 1",(uid,))
        res=c.fetchone()
        print(res[0])
        return res[0]

    @staticmethod
    def find_score():
        data = request.get_json()
        uid = data['user_id']
        send_time = data['time']
        group_id = data['group_id']
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        c.execute("select score from score where QQ=?",(uid,))
        result = c.fetchone()
        return result[0]

    @staticmethod
    def change_score(n):
        data = request.get_json()
        uid = data['user_id']
        send_time = data['time']
        group_id = data['group_id']
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        c.execute("select score from score where QQ=?",(uid,))
        result = c.fetchone()
        print(result)
        result=result[0]
        result+=n
        c.execute("update score set score = ? where QQ = ?",(result,uid))
        print(f"目前结果为{result}")
        conn.commit()
        conn.close()
        return result

    @staticmethod
    def reply(message_id):
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        c.execute("SELECT * FROM message WHERE message_id = ?", (message_id,))
        results = c.fetchone()
        QQ = results[1]
        ID = results[0]
        group_id = results[6]
        message_type = results[5]
        num = ID + 1
        n = 0
        for i in range(60):
            n += 1
            try:
                c.execute("SELECT * FROM message WHERE id = ?", (num,))
                results = c.fetchone()
                new_QQ = results[1]
                new_group_id = results[6]
                new_message_type = results[5]
                if message_type == new_message_type == 'group':
                    if int(new_QQ) == int(QQ):
                        if int(new_group_id) == int(group_id):
                            new_message = results[2]
                            conn.commit()
                            conn.close()
                            return new_message
                        else:
                            num += 1
                            if n == 58:
                                conn.commit()
                                conn.close()
                                return "回复超时"
                            else:
                                time.sleep(1)
                                continue
                    else:
                        num += 1
                        if n == 58:
                            conn.commit()
                            conn.close()
                            return "回复超时"
                        else:
                            time.sleep(1)
                            continue
                elif message_type == new_message_type == 'private':
                    if int(new_QQ) == int(QQ):
                        new_message = results[2]
                        conn.commit()
                        conn.close()
                        return new_message
                    else:
                        num += 1
                        if n == 58:
                            conn.commit()
                            conn.close()
                            return "回复超时"
                        else:
                            time.sleep(1)
                            continue
                else:
                    num += 1
                    if n == 58:
                        conn.commit()
                        conn.close()
                        return "回复超时"
                    else:
                        time.sleep(1)
                        continue
            except:
                if n == 58:
                    conn.commit()
                    conn.close()
                    return "回复超时"
                else:
                    time.sleep(1)
                    continue

    @staticmethod
    def song(name_song):
        url = f'https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg?_=1665976902418&cv=4747474&ct=24&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=1&uin=646319630&g_tk_new_20200303=1522233292&g_tk=1522233292&hostUin=0&is_xml=0&key={name_song}'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        }

        res = requests.get(url, headers=headers)
        res = res.json()['data']['song']['itemlist'][0]
        song_id = res['id']
        API.send("[CQ:music,type=qq,id=" + str(song_id) + "]")


@app.route('/', methods=["POST"])
def post_data():
    """下面的request.get_json().get......是用来获取关键字的值用的，关键字参考上面代码段的数据格式"""
    global role
    data = request.get_json()
    print(data)

    if data['post_type'] == 'message':
        message = data['message']
        API.save_message()
        print(message)
        menu.menu()
    elif data['post_type'] == 'notice':
        if data['user_id'] == 1846319142:
            return
        menu.notice_menu()
    return "OK"
#

if __name__ == '__main__':
    # 此处的 host和 port对应上面 yml文件的设置
    app.run(host='0.0.0.0', port=5710)  # 保证和我们在配置里填的一致
