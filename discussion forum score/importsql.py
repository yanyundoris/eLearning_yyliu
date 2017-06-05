import MySQLdb
import string
import re
import os

conn = MySQLdb.connect(host = '127.0.0.1',user = 'eLearning',passwd = 'Mdb4Learn')
cursor = conn.cursor()


sql = "use eLearning "
cursor.execute(sql)
sql = "show tables;"
cursor.execute(sql)


sql1 = "select id, body from 107x_1T2016_commentthread;"




cursor.execute(sql1)

cc = cursor.fetchall()

path = os.path.join('/disk02/data/eLearning/yyliu/','AndroidBody'+'.txt')

file = open(path,'w+')

for i in range(0,len(cc)):
    print >> file, cc[i][0].strip()+"\n"+cc[i][1].replace('\n','\\n')

file.close()




import MySQLdb
import string
import re
import os

conn = MySQLdb.connect(host = '127.0.0.1',user = 'eLearning',passwd = 'Mdb4Learn')
cursor = conn.cursor()


sql = "use eLearning "
cursor.execute(sql)
sql = "show tables;"
cursor.execute(sql)


sql1 = "select comment_thread_id, body from 107x_2016_T1_comment;"




cursor.execute(sql1)

cc = cursor.fetchall()

path = os.path.join('/disk02/data/eLearning/yyliu/','AndroidBody1'+'.txt')

file = open(path,'w+')

for i in range(0,len(cc)):
    print >> file, cc[i][0].strip()+"\n"+cc[i][1].replace('\n','\\n')

file.close()




import MySQLdb
import string
import re
import os

conn = MySQLdb.connect(host = '127.0.0.1',user = 'eLearning',passwd = 'Mdb4Learn')
cursor = conn.cursor()


sql = "use eLearning "
cursor.execute(sql)
sql = "show tables;"
cursor.execute(sql)


sql1 = "select comment_thread_id, body from 102_1x_4T2015_comment;"




cursor.execute(sql1)

cc = cursor.fetchall()

path = os.path.join('/disk02/data/eLearning/yyliu/','JavaBody1'+'.txt')

file = open(path,'w+')

for i in range(0,len(cc)):
    print >> file, cc[i][0].strip()+"\n"+cc[i][1].replace('\n','\\n')

file.close()
