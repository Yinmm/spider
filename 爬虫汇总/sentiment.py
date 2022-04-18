import re
def sentiment_judge(text):
    text = re.findall(r'[\u4e00-\u9fa5a-zA-Z0-9]',text)
    text = ''.join(text)
    from aip import AipNlp
    APP_ID = '25827938'
    API_KEY = '6VAGdaGi79SdGLGuHmILbl71'
    SECRET_KEY = 'GHPscSN0Nrj2I9f959TDSVDoaCWzsa1x'
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    result = client.sentimentClassify(text)
    # print(result)
    sentiment = result.get('items')[0].get('sentiment')
    if sentiment == 0:
        return "负面"
    elif sentiment == 1:
        return "中性"
    else:
        return "正面"

