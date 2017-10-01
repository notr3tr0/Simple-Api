import psycopg2
import requests
import json
import telegram_api
import time
import math
from datetime import datetime, timedelta, date, time as dt_time

token = "#Не скажу)"

def main():
    connect = psycopg2.connect(database="location_database",host="localhost", user='location_user', password='Par0lka')
    cursor = connect.cursor()
    # cursor.execute("CREATE TABLE tbl(id INT, data JSON);")

    # cursor.execute('INSERT INTO userid66475832 VALUES (\'%s\',%s,\'%s\');' % (gps,pulse,date))
    # cursor.execute('SELECT pulse FROM userid66475832;')
    connect.commit()
    sql = "SELECT pulse,gps,date FROM userid1 WHERE date = (SELECT MAX(date) FROM userid1)"
    #cursor.execute("SELECT pulse,gps,date FROM userid1 WHERE date > '%s';" % (datetime.fromtimestamp(int(time.time())-60)))
    cursor.execute(sql)
    rows = cursor.fetchall()
    gps = []
    pulse = []
    for row in rows:
        if int(row[0]) >= 100 or int(row[0]) <= 40:
            print(row[0])
            gps.append(row[1])
            pulse.append(row[0])
    def request():
        #for i in gps
        for i in range(len(gps)):
            if pulse[i] == 0:
                a = gps[i].split(",")
                msg = 'https://api.telegram.org/bot%s/sendMessage?chat_id=381671645&text=Миронов Цех 4\n Пульс:%s' % (token,str(pulse[i])).encode()
                r = requests.get(msg)
                loc = 'https://api.telegram.org/bot%s/sendLocation?chat_id=381671645&latitude=%s&longitude=%s' % (token, str(a[0]), str(a[1])).encode()      
                r = requests.get(loc)          
                time.sleep(1)
            else:
                a = gps[i].split(",")
                r = requests.post("http://wildcubes.ru:19286",  data =("f*9t4vYb4^m@@$X@:cheap-security:msg||118128747||Пульс: %s\nМиронов Цех 4|||loc||118128747||%s||%s" % (str(pulse[i]), str(a[0]), str(a[1]))).encode())
                time.sleep(1)
            #print(json.loads(r.text))
    request()



    connect.close()
