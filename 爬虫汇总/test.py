#coding:utf-8

import requests
import time,datetime
import re
import xlsxwriter
import emoji

def testRequest(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    r = requests.session()
    res = r.get(url=url,headers=header)






# HEADERS = {'Host': 'api.taptapdada.com',
#            'Connection': 'Keep-Alive',
#            'Accept-Encoding': 'gzip',
#            'User-Agent': 'okhttp/3.10.0'}
#
# r =requests.session()
#
# r.cookies.set('cookie-name', 'cookie-value', path='/', domain='.abc.com')
#
# testurl = "https://www.taptap.com/webapiv2/post/v3/by-topic?topic_id=20264291&order=desc&sort=position&limit=10&from=0&X-UA=V%3D1%26PN%3DWebApp%26LANG%3Dzh_CN%26VN_CODE%3D65%26VN%3D0.1.0%26LOC%3DCN%26PLT%3DPC%26DS%3DAndroid%26UID%3Dd3e47a98-ecc5-4eb1-b37b-7e629d39b36e%26VID%3D412086289%26DT%3DPC%26OS%3DWindows%26OSV%3D10"
#
# BASE_url = 'https://api.taptapdada.com/post/v3/by-topic?limit=10&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D224003000%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D3d0b3c6d-57eb-488a-bfdf-2bc60ec0570a%26VID%3D419366694%26NT%3D4%26SR%3D1080x2116%26DEB%3DXiaomi%26DEM%3DMIX%2B2S%26OSV%3D10&from=0&topic_id=20337656&sort=position&order=asc'
# res = r.get(url=BASE_url,headers=HEADERS)
# print(res.text)

# workbook = xlsxwriter.Workbook('tap账号邮箱-密码2.xlsx')  # 创建一个excel文件
# worksheet = workbook.add_worksheet(u'sheet1')  # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1
#
# worksheet.set_column('A:A', 20)  # 设置第一列宽度为20像素
# bold = workbook.add_format({'bold': True})  # 设置一个加粗的格式对象
#
# worksheet.write('A1', U'邮箱',bold)  # 在A1单元格写上HELLO
# worksheet.write('B1', '密码', bold)  # 在A2上写上WORLD,并且设置为加粗
#
#
# f = open('tap.txt',encoding='utf-8')  # 返回一个文件对象
# line = f.readline()  # 调用文件的 readline()方法
# count1 =1
# try:
#     while line:
#         line = f.readline()
#         str = line
#         pattern1 = re.compile(r'(?<=).*?(?=---)')
#         m = pattern1.search(str)
#         if m:
#             email = m.group()
#
#         pattern2 = re.compile(r'(?<=----).*?(?=---)')
#         m2 = pattern2.search(str)
#         if m2:
#             pwd = m2.group()
#
#         worksheet.write(count1, 0, email)
#         worksheet.write(count1, 1, pwd)
#         count1 += 1
#         print(email)
#     workbook.close()
#     f.close()
# except Exception as e:
#     print(e)
#
#

# selectdate = "2022-3-17"
#
# fromDate = "{} 00:00:00".format(selectdate)
# endDate = "{} 23:59:59".format(selectdate)
#
# fromDateTimeArry = int(time.mktime(time.strptime(fromDate, "%Y-%m-%d %H:%M:%S")))
# endDateTimeArry = int(time.mktime(time.strptime(endDate, "%Y-%m-%d %H:%M:%S")))
#
# # print(fromDateTimeArry)
# # print(endDateTimeArry)
#
# date = 1647446302
#
# for i in range(5):
#     if date > fromDateTimeArry and date < endDateTimeArry:
#         pass
#     else:
#         continue
#     print("test")
import time


# class Getoutofloop(Exception):
#     pass
# try:
#     for i in range(5):
#         for j in range(5):
#              if i == j == 2:
#                   raise Getoutofloop()
#              else:
#                    print (i, '----', j)
# except Getoutofloop:
#       pass
