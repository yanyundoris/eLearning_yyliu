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


sql1 = "select term_id, video_id, module_number, module_part, sequence from Video_Basic_Info;"

cursor.execute(sql1)

cc = cursor.fetchall()

path = os.path.join('/disk02/data/eLearning/yyliu/','module_infor'+'.txt')

file = open(path,'w+')

for i in range(0,len(cc)):
    print >> file, str(cc[i][0]).strip()+","+str(cc[i][1]).strip()+","+str(cc[i][2]).strip()+","+str(cc[i][3]).strip()+","+str(cc[i][4]).strip()

file.close()