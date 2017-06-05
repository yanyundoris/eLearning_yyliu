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


#sql1 = "select distinct user_id from 102_1x_4T2015_student_courseaccessrole where role = 'instructor' or role = 'staff';"

sql1 = "select distinct user_id from 107x_1T2016_student_courseaccessrole where role = 'instructor' or role = 'staff';"


cursor.execute(sql1)

cc = cursor.fetchall()

path = os.path.join('/disk02/data/eLearning/yyliu/','102_1x_4T2015staffrole.txt')

file = open(path,'w+')

for i in range(0,len(cc)):

    print >> file, str(cc[i][0]).strip()

file.close()