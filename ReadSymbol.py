# ReadSymbol.py
# Web Scraping with python from site tsetmc.com
# Writing by Madjid@DehghanNasiri.ir
import urllib.request as ulr
import requests
import gzip
import bs4
import time
import datetime

startTime = time.time()

url_namadha = 'http://www.tsetmc.com/Loader.aspx?ParTree=111C1417'
url_info = 'http://www.tsetmc.com/Loader.aspx?ParTree=151311&i={0}'
page = requests.get(url_namadha)
soup = bs4.BeautifulSoup(page.content,  'lxml')

table = soup.find('table')
c = 0
data = []
for row in table.findAll('tr'):
    if c==0:
        c = c + 1
        continue
    cells = row.findAll('td')
    if len(cells) == 8:
        code = str(cells[0].string)
        if(code.startswith('IRR')==False):
            symbol = cells[6].string
            group = str(cells[2].string)
            board = str(cells[3].string)
            name = str(cells[7].string)
            link = cells[6].find('a')
            inscode = link.get('href', '').rfind('inscode=')
            inscode = link.get('href', '')[inscode+8:]
            data = data + [{'symbol':symbol, 'inscode':inscode, 'group':group, 'board':board, 'code':code, 'name':name}]
            c = c + 1

c = 1
for item in data:
    print(' Loading {0:4d}: | {1:^10s} | {2:20}'.format(c, item['symbol'], item['name']))
    try:
        url = url_info.format(item['inscode'])
        page = requests.get(url_namadha)
        if( page.status_code == requests.codes.ok ):
            soup = bs4.BeautifulSoup(page.content,  'lxml')
            print('Load complete "{}"'.format(item['code']))
        else:
            print('Unload "{}"'.format(item['code']))
    except:
        print('Error in loading symbol "{}"'.format(item['code']))
    
    c = c + 1

doneTime = time.time()
elapsedTime = doneTime - startTime
print('Elapsed Time {0}'.format(datetime.timedelta(elapsedTime)))