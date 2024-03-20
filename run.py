import requests
import requests
from bs4 import BeautifulSoup

def crawler(recruit):
    msg = []
    detail = recruit.find('div', class_='content')
    basicInfo = detail.find('div', class_='topInfo').find_all('p')
    requireMent = detail.find_all('div', class_='rowSec')[0].find_all('p')
    description = detail.find_all('div', class_='rowSec')[1].find_all('p')
    for b in basicInfo:
        print(''.join(b.find_all(text=True, recursive=False)).strip(), end=': ')
        print(b.find('span').get_text())
        msg.append(''.join(b.find_all(text=True, recursive=False)).strip(), end=': ')
        msg.append(b.find('span').get_text())
    print()
    msg.append('\n')
    for r in requireMent:
        print(r.text)
        msg.append(r.text)
    print()
    msg.append('\n')
    for d in description:
        print(d.text)
        msg.append(d.text)
    return msg


def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    massage = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = massage)
    return r.status_code


if __name__ == '__main__':
    message = '[LINE Notify] Hello World' # 要傳送的訊息內容
    token = '05BqyZK9OBEPkT3oJ6aRBV8vgQhBLZgELQrjKej2CIu' # 權杖值
    page = 1
    params = {'action':'recruit', 'p':page}
    url = "https://www.oturoc.org.tw/index.php"
    r = requests.get(url = url, params = params)
    soup = BeautifulSoup(r.text, "html.parser")
    recruitList = soup.select('.recruitItem')
    while len(recruitList) > 0:
        for recruit in recruitList:
            msg = ''.join(crawler(recruit))
            lineNotifyMessage(token, msg)
        page += 1
        params = {'action':'recruit', 'p':page}
        url = "https://www.oturoc.org.tw/index.php"
        r = requests.get(url = url, params = params)
        soup = BeautifulSoup(r.text, "html.parser")
        recruitList = soup.select('.recruitItem')



    