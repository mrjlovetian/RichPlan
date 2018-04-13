#coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import ssl
import pymysql

connect = pymysql.Connect(
    host='localhost',
    user='root',
    port=3306,
    password='897011805',
    db='rich',
    use_unicode=True,
    charset='utf8'
)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

option = Options()
option.add_argument("--headless")
option.add_argument("--disable-gpu")
browser = webdriver.Chrome(chrome_options=option)

def getMianUrl(receiveUrl):
    browser.get(receiveUrl)

    try:
        zhongZiObj = BeautifulSoup(browser.page_source, 'lxml')
        # print(zhongZiObj)

        for tr in zhongZiObj.find_all('tr', class_='t_tr1'):
            values = tr.find_all('td')
            # 期数
            period = values[0].string
            # 1-7号码
            A = values[1].string
            B = values[2].string
            C = values[3].string
            D = values[4].string
            E = values[5].string
            F = values[6].string
            G = values[7].string

            # 所有奖金池里的奖金
            all_rich = values[9].string
            # 一等奖人数
            first_winner = values[10].string
            # 一等奖奖金
            first_rich = values[11].string
            # 二等奖人数
            second_winner = values[12].string
            # 二等奖奖金
            second_rich = values[13].string
            # 投注总额
            buy_money = values[14].string
            # 日期
            rich_date = values[15].string

            print('********' + period, A, B, C, D, E, F, G, all_rich, first_winner, first_rich, second_winner,
                  second_rich,
                  buy_money, rich_date)
            print('\n')
            # print(sql, (
            #     period, A, B, C, D, E, F, G, all_rich, first_winner, first_rich, second_winner, second_rich, buy_money,
            #     rich_date))
            for value in tr.find_all('td', class_='t_cfont2'):
                print('*******************%s' % value)
            sql = '''insert into Rich_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            print(sql, (
                period, A, B, C, D, E, F, G, all_rich, first_winner, first_rich, second_winner, second_rich, buy_money,
                rich_date))
            cur.execute(sql, (
                period, A, B, C, D, E, F, G, all_rich, first_winner, first_rich, second_winner, second_rich, buy_money,
                rich_date))
            connect.commit()
    except:
        print("出现异常")
    finally:
        browser.close()

cur = connect.cursor()
cur.execute("set charset utf8")

context = ssl._create_unverified_context()
url = 'https://datachart.500.com/ssq/history/newinc/history.php?start=00001&end=18041'

getMianUrl(url)


cur.close()
connect.close()