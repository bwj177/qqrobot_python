
import random
import requests
from bs4 import BeautifulSoup
import requests
from main import *
guess=["石头","剪刀","布"]
random_response=["找本姑奶奶干嘛哎哟~","你干嘛哎哟","小黑子树枝666","蒸乌鱼","油饼食不食"]
dic={
    "石头":{"剪刀":1,"石头":0,"布":-1},
    "剪刀":{"石头":-1,"剪刀":0,"布":1},
    "布":{"布":0,"剪刀":-1,"石头":1},
    }

setu=["FplUKy5f8UuzshpXtDNWdG7VepH4","FkEz9S-Eto1s3tz_NwFjxti9y7Zo","FgzypBbBRDgo7fFDv300LXbRT8on","Fj48adQ50qCcEz9ayCCD2oWu14A8","FvGlKbHv0DxhxWd15VEmSYiuD9je","FhGrSHkVWEXUbWF5yQ4-NWYqqtiz","FpMSt2uSXgcZ_xZISmRrV3Ggm_kE","Fmiq61IQNTuWQlxCZtRK75ejVFjL","FlZNYlg5h92IVxqLjqhB6-it9JwY","Fgeou2oYvOprrJKbQDpoiBa-26Ol","FqGja28rVTq-eHXMJGgKHA9IKcWh","FgbVt_0VHBGFPSwZGpq8NODBF5fp","FlL0m3bjMe91mIwwA2QKxEsJ79g_","FlxlEjhZ07wZziXnk1ZmD3pPpLkm"]




def guessGame(messages):
    n=random.randint(0,2)
    myguess=guess[n]
    res = dic[messages][myguess]
    if res==0:
        return f"我出的是{myguess},平局呢，还挺牛"
    elif res==1:
        ans=API.change_score(100)
        return f"我出的是{myguess},你赢了？，不可思议"+f"你目前积分为：{ans}"
    else:
        ans=API.change_score(-100)
        return f"我出的是{myguess},小垃圾，输了吧!"+f"你目前积分为：{ans}"

def randomResponse():
    n=random.randint(0,len(random_response)-1)
    return random_response[n]

def addNewWord(newword):
    random_response.append(newword)
    return "添加成功..."

def GetWeather(cityName):
    cookies = {
        'BIDUPSID': 'ABC770A56AAD1E552FAB99C7CE36ECAA',
        'PSTM': '1653634850',
        'BAIDUID': 'ABC770A56AAD1E552106D5A8BAF9EBC5:FG=1',
        'BDSFRCVID_BFESS': '9d0OJeCmHRK6MljD4uC9uQHHCeKK0gOTHllnV9rzfBLFl7tVJeC6EG0Ptf8g0KubuTkzogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
        'BAIDUID_BFESS': '6D7995BB1AE2F8100AED6C5BDFC80A9B:FG=1',
        'BA_HECTOR': '2ha0802g8125252g0h2l36fp1hfjq1j17',
        'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
        'SE_LAUNCH': '5%3A1660553705',
        'POLYFILL': '0',
        'delPer': '0',
        'H_WISE_SIDS': '107311_110085_131861_180636_196426_204904_206122_208721_209568_210294_210321_211435_211985_212295_212740_212797_212867_213040_213351_214807_215727_216842_216941_217049_217086_217167_217915_218022_218454_218598_218619_219067_219943_219946_220014_220602_220662_220856_221008_221118_221121_221391_221411_221439_221468_221478_221501_221697_221796_221825_221871_221901_221919_222276_222298_222390_222396_222500_222616_222618_222620_222625_222773_222780_222792_222955_223048_223064_223134_223238_223253_223375_223474_223599_223766_223788_223825_223853_223919_224048_224068_224085_224275_224438_224572_224798_224815_224867_8000087_8000124_8000135_8000146_8000149_8000151_8000164_8000170_8000178_8000185',
        'H_WISE_SIDS_BFESS': '107311_110085_131861_180636_196426_204904_206122_208721_209568_210294_210321_211435_211985_212295_212740_212797_212867_213040_213351_214807_215727_216842_216941_217049_217086_217167_217915_218022_218454_218598_218619_219067_219943_219946_220014_220602_220662_220856_221008_221118_221121_221391_221411_221439_221468_221478_221501_221697_221796_221825_221871_221901_221919_222276_222298_222390_222396_222500_222616_222618_222620_222625_222773_222780_222792_222955_223048_223064_223134_223238_223253_223375_223474_223599_223766_223788_223825_223853_223919_224048_224068_224085_224275_224438_224572_224798_224815_224867_8000087_8000124_8000135_8000146_8000149_8000151_8000164_8000170_8000178_8000185',
        'BDSVRTM': '54',
        'PSINO': '5',
        'H_PS_PSSID': '36549_36755_36641_37107_36954_34812_36917_36569_37077_37137_37055_26350',
        'ab_sr': '1.0.1_MTU4MzA0NmM2MWUxMTA0MTczZmJlMjhmZGFkYTM1ZTE1MWRmNTA0NzM4ZTliYjcwNDkzZThkYjNmZTViNjNmNjVkY2NjMGFhMzUyNzUwNGNlOTYyNTg1NDAwMzI2MjBhZTBjMTNhNGRlZTQ5ZjU5NDQwMmExYjhmOTYzYmVkNDdmYTcxOGVlMjQ3NDM4ZWUzYTM0MDdlZTY0M2MxYTE1Zg==',
        '__bsi': '10904855338309584892_00_31_R_N_238_0303_c02f_Y',
        'BDSVRBFE': 'Go',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'BIDUPSID=ABC770A56AAD1E552FAB99C7CE36ECAA; PSTM=1653634850; BAIDUID=ABC770A56AAD1E552106D5A8BAF9EBC5:FG=1; BDSFRCVID_BFESS=9d0OJeCmHRK6MljD4uC9uQHHCeKK0gOTHllnV9rzfBLFl7tVJeC6EG0Ptf8g0KubuTkzogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BAIDUID_BFESS=6D7995BB1AE2F8100AED6C5BDFC80A9B:FG=1; BA_HECTOR=2ha0802g8125252g0h2l36fp1hfjq1j17; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; SE_LAUNCH=5%3A1660553705; POLYFILL=0; delPer=0; H_WISE_SIDS=107311_110085_131861_180636_196426_204904_206122_208721_209568_210294_210321_211435_211985_212295_212740_212797_212867_213040_213351_214807_215727_216842_216941_217049_217086_217167_217915_218022_218454_218598_218619_219067_219943_219946_220014_220602_220662_220856_221008_221118_221121_221391_221411_221439_221468_221478_221501_221697_221796_221825_221871_221901_221919_222276_222298_222390_222396_222500_222616_222618_222620_222625_222773_222780_222792_222955_223048_223064_223134_223238_223253_223375_223474_223599_223766_223788_223825_223853_223919_224048_224068_224085_224275_224438_224572_224798_224815_224867_8000087_8000124_8000135_8000146_8000149_8000151_8000164_8000170_8000178_8000185; H_WISE_SIDS_BFESS=107311_110085_131861_180636_196426_204904_206122_208721_209568_210294_210321_211435_211985_212295_212740_212797_212867_213040_213351_214807_215727_216842_216941_217049_217086_217167_217915_218022_218454_218598_218619_219067_219943_219946_220014_220602_220662_220856_221008_221118_221121_221391_221411_221439_221468_221478_221501_221697_221796_221825_221871_221901_221919_222276_222298_222390_222396_222500_222616_222618_222620_222625_222773_222780_222792_222955_223048_223064_223134_223238_223253_223375_223474_223599_223766_223788_223825_223853_223919_224048_224068_224085_224275_224438_224572_224798_224815_224867_8000087_8000124_8000135_8000146_8000149_8000151_8000164_8000170_8000178_8000185; BDSVRTM=54; PSINO=5; H_PS_PSSID=36549_36755_36641_37107_36954_34812_36917_36569_37077_37137_37055_26350; ab_sr=1.0.1_MTU4MzA0NmM2MWUxMTA0MTczZmJlMjhmZGFkYTM1ZTE1MWRmNTA0NzM4ZTliYjcwNDkzZThkYjNmZTViNjNmNjVkY2NjMGFhMzUyNzUwNGNlOTYyNTg1NDAwMzI2MjBhZTBjMTNhNGRlZTQ5ZjU5NDQwMmExYjhmOTYzYmVkNDdmYTcxOGVlMjQ3NDM4ZWUzYTM0MDdlZTY0M2MxYTE1Zg==; __bsi=10904855338309584892_00_31_R_N_238_0303_c02f_Y; BDSVRBFE=Go',
        'Referer': 'https://www.baidu.com/link?url=DuQVKq8Td4TeuN-jwjK7jsswx0C1IdqTEyroK-ujwDUgbqe8cxCSUISnkUn7YB-lcSSOtk_xpTMJD1pl1GH_WSj5TEyWoehR9gwTgNsmuUnTOygSygm4X1V6BmRDvXpUboPyHjWmSvqm29EfTYTWRdCVaS2LiKke2KTbl3MNz-ERJRAny3-eED6v5rA7XV03cPWjuGuwvxzGuW4KMF13CqG7_hRSlgvrZ4WgzBt0GY7&wd=&eqid=d36a6c8c00004d680000000462faee7e',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'pd': 'life_compare_weather',
        'openapi': '1',
        'dspName': 'iphone',
        'from_sf': '1',
        'resource_id': '4495',
        'word': '全国天气',
        'title': '省市天气查询',
        'srcid': '4983',
        'fromSite': 'pc',
    }
    #获取网页
    response = requests.get('https://m.baidu.com/sf', params=params, cookies=cookies, headers=headers)
    #数据存储
    fo = open("./天气.txt",'a',encoding="utf-8")

    #解析网页
    response.encoding='utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    #爬取内容
    content="div.c-span3"
    #清洗数据
    ans_tmp=[]
    a=soup.select(content)
    ans={}
    for i in range(0,len(a)):
        a[i] = a[i].text
        ans_tmp.append(a[i])
    print(ans_tmp)
    print((len(ans_tmp)))
    for i in range(0,len(ans_tmp),2):
        print(ans_tmp[i])
        ans[ans_tmp[i]]=ans_tmp[i+1]
    return ans[cityName]

def GetSetu():
    n=random.randint(0,len(setu)-1)
    return f"http://img.jayb.top/{setu[n]}"

def shidianban():
    pass