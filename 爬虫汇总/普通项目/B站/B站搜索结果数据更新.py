import requests
import time
import xlsxwriter
import pandas as pd
import re

r =requests.session()
ExcelName = r"C:\Users\Administrator\Desktop\哈利波特B站搜索结果-9月19日-22日\已合并且去重数据.xlsx"
frame = pd.read_excel(ExcelName)
dataFrame = pd.DataFrame(frame)
# print(data)
df = pd.read_excel(ExcelName,usecols="F",names=None)
df_li = df.values.tolist()
row = 0
for s_li in df_li:
    s_li = ''.join(s_li)
    pattern = re.compile(r'(?<=tv/).*')
    m = pattern.search(s_li)
    bvid = ''
    if m:
        bvid = m.group()
    # print(bvid)
    res = r.get(url="https://api.bilibili.com/x/web-interface/view?bvid="+bvid)
    code = res.json()["code"]
    if(code == 0):
        data = res.json()["data"]["stat"]
        pubdate = res.json()["data"]["pubdate"]
        timeArray = time.localtime(pubdate)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        view = data["view"] #播放
        danmaku = data["danmaku"]  #弹幕0
        reply = data["reply"]   #评论
        favorite = data["favorite"] #收藏
        coin = data["coin"]#投币
        share = data["share"]#分享
        like = data["like"]#点赞
        dataFrame.loc[row:row,("时间","播放数","弹幕","评论","收藏","投币","分享","点赞")] = [otherStyleTime,view,danmaku,reply,favorite,coin,share,like]
    if(row %20==0):
        time.sleep(2)
    print(row)
    row += 1
dataFrame.to_excel("new哈利波特搜索结果0919-0922.xlsx")

