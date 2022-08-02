import re
import scipy.io

import csv

import pymysql


conn = pymysql.connect(host='localhost', user='root', password='tjsals6092',

                       db='django_db', charset='utf8')

curs = conn.cursor()

conn.commit()


f = open('/Users/dclab/Downloads/log_kr.txt','r')

csvReader = csv.reader(f)


for row in csvReader:

    user_date = (row[0])

    user_month = (row[1])

    user_avg_temp = (row[2])

    print (user_date)

    print (user_month)

    print (user_avg_temp)



    sql = """insert into new_table (idnew_table , new_tablecol, new_tablecol1) values (%s, %s, %s)"""

    curs.execute(sql, (user_date, user_month,user_avg_temp))


#db의 변화 저장

conn.commit()


f.close()

conn.close()





