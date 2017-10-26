url = 'https://datachart.500.com/dlt/history/newinc/history.php?start=1&end=17125'
from bs4 import BeautifulSoup
import urllib.request
import ssl
import pymysql

connect = pymysql.Connect(
    host='localhost',
    port=3306,
    db='rich',
    user='root',
    password='897011805',
)

cur = connect.cursor()

context = ssl._create_unverified_context()

def get_datat_url(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request, context=context)
    resObj = BeautifulSoup(response, 'lxml')
    da_table = resObj.find('tbody', id='tdata')
    for tr in da_table.find_all('tr', class_='t_tr1'):
        values = tr.find_all('td')
        period = values[0].string
        A1 = values[1].string
        A2 = values[2].string
        A3 = values[3].string
        A4 = values[4].string
        A5 = values[5].string
        B1 = values[6].string
        B2 = values[7].string

        all_rich = values[8].string
        first_winer = values[9].string
        first_rich = values[10].string
        second_winer = values[11].string
        second_rich = values[12].string
        buy_money = values[13].string
        rich_date = values[14].string

        print(period, A1, A2, A3, A4, A5, B1, B2, all_rich, first_winer, first_rich, second_winer, second_rich, buy_money, rich_date)
        sql = '''insert into da_rich_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        cur.execute(sql, (period, A1, A2, A3, A4, A5, B1, B2, all_rich, first_winer, first_rich, second_winer, second_rich, buy_money, rich_date))
        connect.commit()


get_datat_url(url)
cur.close()
connect.close()