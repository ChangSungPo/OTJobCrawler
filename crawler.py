import requests
from bs4 import BeautifulSoup



page = 1
params = {'action':'recruit', 'p':page}
url = "https://www.oturoc.org.tw/index.php"
r = requests.get(url = url, params = params)
soup = BeautifulSoup(r.text, "html.parser")

recruitList = soup.select('.recruitItem')
while len(recruitList) > 0:
    for recruit in recruitList:
        detail = recruit.find('div', class_='content')
        basicInfo = detail.find('div', class_='topInfo').find_all('p')
        requireMent = detail.find_all('div', class_='rowSec')[0].find_all('p')
        description = detail.find_all('div', class_='rowSec')[1].find_all('p')
        for b in basicInfo:
            print(''.join(b.find_all(text=True, recursive=False)).strip(), end=': ')
            print(b.find('span').get_text())
        print()
        for r in requireMent:
            print(r.text)
        print()
        for d in description:
            print(d.text)
        print()
        print()
        print()
    page += 1
    params = {'action':'recruit', 'p':page}
    url = "https://www.oturoc.org.tw/index.php"
    r = requests.get(url = url, params = params)
    soup = BeautifulSoup(r.text, "html.parser")
    recruitList = soup.select('.recruitItem')


