import requests
import time
import xlsxwriter
import random
import re

import 爬虫汇总.sentiment as sentiment

def main():
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Cookie": "sid=5uvttg2r; DedeUserID=10168449; DedeUserID__ckMd5=0efdda588423f51c; SESSDATA=16831e38%2C1634274368%2C26131*41; bili_jct=c2d57db265ff7dd0b69e7820eadd1780; JSESSIONID=01DC5C31602830E553628A1B06D69C8D"
    }

    page_num = 1
    r =requests.session()
    count1 = 1

    # 表格
    Todaydate = time.strftime("%Y-%m-%d", time.localtime())
    workbook = xlsxwriter.Workbook(gameName+'B站第' + str(Fornum) + '页-' + str(Endnum) + '页-' + Todaydate + '.xlsx')
    worksheet = workbook.add_worksheet(u'sheet1')  # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1

    worksheet.set_column('A:A', 20)  # 设置第一列宽度为20像素
    bold = workbook.add_format({'bold': True})  # 设置一个加粗的格式对象

    worksheet.write('A1', U'时间')  # 在A1单元格写上HELLO
    worksheet.write('B1', '用户名称', bold)  # 在A2上写上WORLD,并且设置为加粗
    worksheet.write('C1', U'评分', bold)  # 在B2上写上中文加粗
    worksheet.write('D1', U'评价内容', bold)  # 在B2上写上中文加粗
    worksheet.write('E1', U'用户等级', bold)  # 在B2上写上中文加粗
    worksheet.write('F1', U'评论点赞数', bold)  # 在B2上写上中文加粗
    worksheet.write('G1', U'评论点踩数', bold)  # 在B2上写上中文加粗
    worksheet.write('H1', U'评论回复数', bold)  # 在B2上写上中文加粗
    worksheet.write('I1', U'情绪判断', bold)  # 在B2上写上中文加粗


    try:
        for i in range(Fornum,Endnum):
            print(i)
            page_num = 1*i
            data = {
                "game_base_id": gameID,
                "rank_type": "2",
                "page_num": page_num,
                "page_size": "20",
                "_": "1633778237489",
            }
            res = r.get(url="https://line1-h5-pc-api.biligame.com/game/comment/page", headers=header, params=data)
            list = res.json()["data"]["list"]
            for dict in list:
                date = dict["publish_time"]
                id = dict["user_name"]
                grade = dict["grade"]
                content = dict["content"]
                user_level = dict["user_level"]
                up_count = dict["up_count"]
                down_count = dict["down_count"]
                reply_count = dict["reply_count"]

                worksheet.write(count1, 0, date)
                worksheet.write(count1, 1, id)
                worksheet.write(count1, 2, grade)
                worksheet.write(count1, 3, content)
                worksheet.write(count1, 4, user_level)
                worksheet.write(count1, 5, up_count)
                worksheet.write(count1, 6, down_count)
                worksheet.write(count1, 7, reply_count)
                print(content)
                sentiment_result = sentiment.sentiment_judge(content)
                worksheet.write(count1, 8, sentiment_result)
                count1 += 1
                pause = random.uniform(0, 2)
                time.sleep(pause)
                print("休眠一下")
        print("**********读取完成***********")
        workbook.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    gameName = "筑梦公馆"
    gameID =104001
    Fornum=1 # 从1开始
    Endnum=3
    # for n in range(0,5):
    #     main()
    #     print(Fornum)
    #     Fornum = Endnum
    #     Endnum += 100
    # Fornum = Endnum
    # Endnum = 540
    main()