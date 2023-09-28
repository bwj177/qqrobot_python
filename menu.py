from flask import Flask, request

from menuApi import *
def menu():
    data = request.get_json()
    message = data['message']
    message_id = data['message_id']
    message_type = data['message_type']
    uid = data['user_id']

    if "菜单" in message:
        menu_()

    elif "礼物" in message:
        send_gift(uid)

    elif "打卡" == message:
        print("准备打卡")
        daka()

    elif "只因" in message or "鸡" in message:
        response_ikun(uid)

    elif "查询积分" in message:
        response_score(uid)

    elif "点歌" in message:
        order_song(message_id)

    elif "十点半" in message:
        game2(uid,message_id)

    elif '猜拳' in message:
        guess_game(message_id, message_type, uid)

    elif '天气' in message:
        get_wheather(message_id, message_type,uid)

    elif "涩图" in message:
        get_setu(uid)

    elif "添加ikun语录" in message:
        add_ikun_word(message_id, message_type, uid)

    elif "[CQ:at,qq=1846319142]" in message:
        response_ikun(uid)
    else:
        print('命令不正确')
    return "OK"


def notice_menu():
    data = request.get_json()
    print(data)
    uid = data['user_id']
    notice_type = data['notice_type']
    if uid=='1846319142':
        return
    elif notice_type=='group_recall':
        print("捕获撤回信息")
        find_recall(uid)
    sub_type=data['sub_type']
    if sub_type=='poke':
        poke_back(uid)
    elif sub_type=='approve':
        print(uid)
        welcome(uid)
    elif sub_type=='kick':
        print(uid)
        byebye(uid)
    else:
        return
    return "OK"
#{'post_type': 'notice', 'notice_type': 'group_recall', 'time': 1666416412, 'self_id': 1846319142, 'message_id': -1854554832, 'group_id': 596048079, 'user_id': 646319630, 'operator_id': 646319630}

# {'post_type': 'notice', 'notice_type': 'group_decrease', 'time': 1666176144, 'self_id': 1846319142, 'sub_type': 'kick', 'group_id': 675841035, 'operator_id': 646319630, 'user_id': 1921450963}
# {'post_type': 'notice', 'notice_type': 'notify', 'time': 1666169171, 'self_id': 1846319142, 'sub_type': 'poke', 'user_id': 646319630, 'sender_id': 646319630, 'target_id': 1846319142, 'group_id': 626983032}
# {'post_type': 'notice', 'notice_type': 'group_increase', 'time': 1666174306, 'self_id': 1846319142, 'sub_type': 'approve', 'group_id': 626983032, 'operator_id': 0, 'user_id': 2209386830}
# 'sub_type': 'approve'

