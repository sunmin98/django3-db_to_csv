import re
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='tjsals6092',

                       db='django_db', charset='utf8')
curs = conn.cursor()

conn.commit()
f = open("/Users/dclab/Downloads/log_kr.txt", "r")

id=0

list_id=[]
list_name=[]
list_class=[]
list_percent=[]

while True:
    line = f.readline()

    if not line: break
    #sql = """insert into log_file (class_name,percent) values (%s,%s)"""
    # val= re.findall('fertile|none_fertile|error', line)
    # val1 = re.findall('\s+[\-0]+\.[0-9]+', line)

    if re.findall("(?!\/)[^\s]+(?=\.jpg).jpg",line):
        id+=1
        list_id.append(id)
        #print(re.findall('fertile|none_fertile|error', line))
        list_name.append(re.findall("(?!\/)[^\s]+(?=\.jpg).jpg",line))


    if re.findall('fertile|none_fertile|error', line):
        #print(re.findall('fertile|none_fertile|error', line))
        list_class.append(re.findall('fertile|none_fertile|error', line))


    if re.findall('\s+[\-0]+\.[0-9]+', line):

        #print(re.findall("\s+[\-0]+\.[0-9]+", line))
        list_percent.append(re.findall("\s+[\-0]+\.[0-9]+", line))




    #curs.execute(sql, (val,val1))
print(list_id)
print(list_name)
print(list_class)
print(list_percent)


for idnum,l_n,l_c,l_p in zip(list_id,list_name,list_class,list_percent):
    #print(l_c , l_p)

    sql = """insert into log_file (id,file_name, class_name, percent) values (%s,%s,%s,%s)"""

    curs.execute(sql,(idnum,l_n, l_c, l_p))

conn.commit()
f.close()
conn.close()

# ----------------------------위로 건들지 마라---------------------

# for l_p in list_percent:
#     #print(l_c)
#     sql = """insert into log_file (percent) values (%s)"""
#     curs.execute(sql,l_p)


# while True:
#     line = f.readline()
#     if not line: break
#     print( re.findall( "(?!\/)[^\s]+(?=\.jpg).jpg" , line ) )

#print(re.findall("(?!\/)[^\s]+(?=\.jpg).jpg",text))
# while True:
#     line = f.readline()
#     if not line: break
#     s=line
#     m= re.findall("\s+[\-0]+\.[0-9]+",s)

# print(m.group())
# print( re.findall( "\s+[\-0]+\.[0-9]+" , line ) )

# r=re.findall( "..\\)+?\b(?!image)+?\b(?!\/)+?[^\s]+(?=\.jpg)+.jpg" )

# p = re.compile('\bfertile\b|\bnone_fertile\b|\berror\b')
#
# text = '''../image/01022642548_2020.07.30.11:37:56.jpg
# none_fertile 0.5158579349517822 s ok
# php call result :
# Notice: Undefined offset: 1 in /var/www/html/oview/deepresult.php on line 10
# ok
#
# ../image/test111222_2019.10.28.20-50-00.jpg
# none_fertile 0.4168539047241211 s ok
# php call result :
# Notice: Undefined offset: 1 in /var/www/html/oview/deepresult.php on line 10
# ok
#
# ../image/test111222_2019.10.28.20-50-00.jpg
# none_fertile 0.42252397537231445 s ok
# php call result :
# Notice: Undefined offset: 1 in /var/www/html/oview/deepresult.php on line 10
# ok
#
# ../image/test111222_2019.10.28.20-50-00.jpg
# none_fertile 0.4279019832611084 s ok
# php call result :
# Notice: Undefined offset: 1 in /var/www/html/oview/deepresult.php on line 10
# ok'''
#
# print(re.findall("\s+[\-0]+\.[0-9]+",text))
# print(re.findall("fertile|none_fertile|error",text))

###이건 된다~~~~~
#print(re.findall("(?!\/)[^\s]+(?=\.jpg).jpg",text))