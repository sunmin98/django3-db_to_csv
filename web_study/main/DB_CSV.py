
                    ################   CSV--> DB   ################
import csv
import pymysql

def CSV_to_DB(csvfile) :
    conn = pymysql.connect(host='localhost', user='root', password='tjsals6092',

                           db='django_db', charset='utf8')

    curs = conn.cursor()

    conn.commit()

    #f = open('media/Uploaded Files/Seoul_temp_2017.csv' , 'r')


    csvReader = csv.reader(csvfile)

    for row in csvReader:

        user_date = (row[0])

        user_month = (row[1])

        user_avg_temp = (row[2])

        #sql = """insert into seoul_temp_1 (month , date, avg_temp) values (%s, %s, %s)"""
        sql = """insert into seoul_temp ( month, avg_temp) values (%s, %s)"""

        #curs.execute(sql, (user_month, user_date ,user_avg_temp))
        curs.execute(sql, ( user_month, user_avg_temp))

        # db의 변화 저장

        conn.commit()

    #f.close()
    conn.close()


                    #########   DB-->엑셀    #######

from openpyxl import Workbook

def DB_to_xlsx() :

    write_wb = Workbook()
    write_ws = write_wb.active

    conn = pymysql.connect(host='localhost', user='root', password='tjsals6092',

                           db='django_db', charset='utf8')
    curs = conn.cursor()


    sql = """SELECT * FROM django_db.seoul_temp"""

    curs.execute("set names utf8")
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()

    #write_ws.append(('month','date','avg_temp'))
    write_ws.append(('month', 'avg_temp'))

    for row in rows:
        #print(row[1],row[2])
        write_ws.append(row)

    file_name = "서울_엑셀파일실험!!.xlsx"
    write_wb.save(file_name)
