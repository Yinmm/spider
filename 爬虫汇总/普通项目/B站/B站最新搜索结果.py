import requests
import time
import xlsxwriter




r =requests.session()
count = 1

# 表格
CurrentTime = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
workbook = xlsxwriter.Workbook('哈利波特搜索结果-'+CurrentTime+'.xlsx')  # 创建一个excel文件
worksheet = workbook.add_worksheet(u'sheet1')  # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1

worksheet.set_column('A:A', 20)  # 设置第一列宽度为20像素
bold = workbook.add_format({'bold': True})  # 设置一个加粗的格式对象

worksheet.write('A1', U'时间', bold)  # 在A1单元格写，并加粗
worksheet.write('B1', U'标题', bold)
worksheet.write('C1', U'作者', bold)
worksheet.write('D1', U'时长', bold)
worksheet.write('E1', U'播放数', bold)
worksheet.write('F1', U'链接', bold)
worksheet.write('G1', U'弹幕', bold)
worksheet.write('H1', U'评论', bold)
worksheet.write('I1', U'收藏', bold)
worksheet.write('J1', U'投币', bold)
worksheet.write('K1', U'分享', bold)
worksheet.write('L1', U'点赞', bold)



keyword = "哈利波特"
page = 1  #最多100
try:
    for i in range(1,81):
        page = i
        data = {
            "actionKey": "appkey",
            "appkey": "27eb53fc9058f8c3",
            "build": 3710,
            "device": "phone",
            "duration": 0,
            "mobi_app": "iphone",
            "order": "pubdate",
            "platform": "ios",
            "rid": 0,
            "keyword": keyword,
            "pn": page,
            "ps": 10,

        }
        res = r.get(url="https://app.bilibili.com/x/v2/search", params=data)
        list = res.json()["data"]["items"]["archive"]
        for dict in list:
            aid = dict["param"]
            title = dict["title"]
            author = dict["author"]
            duration = dict["duration"]
            if "play" in dict:
                play = dict["play"]
            else:
                play = 0
            link = dict["share"]["video"]["short_link"]
            # 获取单个视频的点击、评论、点赞等等
            api = "https://api.bilibili.com/x/web-interface/archive/stat?aid=805536965"
            api2="https://api.bilibili.com/x/web-interface/view?aid=128997" #这个更全！！！！
            res2 = r.get(url="https://api.bilibili.com/x/web-interface/view?aid="+aid)
            data = res2.json()["data"]["stat"]
            pubdate = res2.json()["data"]["pubdate"]
            timeArray = time.localtime(pubdate)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            view = data["view"] #播放
            danmaku = data["danmaku"]  #弹幕
            reply = data["reply"]   #评论
            favorite = data["favorite"] #搜藏
            coin = data["coin"]#投币
            share = data["share"]#分享
            like = data["like"]#点赞
            worksheet.write(count, 0, otherStyleTime)
            worksheet.write(count, 1, title)
            worksheet.write(count, 2, author)
            worksheet.write(count, 3, duration)
            worksheet.write(count, 4, play)
            worksheet.write(count, 5, link)
            worksheet.write(count, 6, danmaku)
            worksheet.write(count, 7, reply)
            worksheet.write(count, 8, favorite)
            worksheet.write(count, 9, coin)
            worksheet.write(count, 10, share)
            worksheet.write(count, 11, like)
            count += 1
        print(i)
        if (i % 20 == 0):
            time.sleep(5)
    print("**********读取完成***********")
    workbook.close()
except Exception as e:
    print(e)