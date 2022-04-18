from bs4 import BeautifulSoup

def GetHtmlText(url):
    try:
        ug = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers = ug,timeout = 5)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
        print ('done')
    except:
        return ''
        print('失败')

def parsepage(html):
    soup = BeautifulSoup(html,'html.parser')
    if soup.find_all('span', 'right-stats-number'):
        user_fans = soup.find_all('span', 'right-stats-number')[0].string
        user_guanzhu = soup.find_all('span', 'right-stats-number')[1].string
        user_shouchang = soup.find_all('span', 'right-stats-number')[2].string
        user_suoyoufabu = soup.find_all('a', id ='publish-tab')[1].find('span').string  #所有发布内容 评分+论坛+评论
        user_played = soup.find_all('h4')[0].find('span').string #玩过的游戏数量
        return user_fans,user_guanzhu,user_shouchang,user_suoyoufabu,user_played
    else:
        return "0","0","0","0","0",