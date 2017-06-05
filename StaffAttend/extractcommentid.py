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

sql1 = "select 102_1x_4T2015_comment.comment_thread_id, 102_1x_4T2015_commentthread.id, 102_1x_4T2015_comment.author_id " \
       "as reply_id, 102_1x_4T2015_commentthread.author_id, 102_1x_4T2015_commentthread.commentable_id  from " \
       "102_1x_4T2015_comment left join 102_1x_4T2015_commentthread on " \
       "102_1x_4T2015_comment.comment_thread_id = 102_1x_4T2015_commentthread.id"


# sql2 = "select 107x_1T2016_comment.comment_thread_id, 107x_1T2016_commentthread.id, 107x_1T2016_comment.author_id " \
#        "as reply_id, 107x_1T2016_commentthread.author_id, 107x_1T2016_commentthread.commentable_id  from " \
#        "107x_1T2016_comment left join 107x_1T2016_commentthread on " \
#        "107x_1T2016_comment.comment_thread_id = 107x_1T2016_commentthread.id"

cursor.execute(sql1)

cc = cursor.fetchall()

path = os.path.join('/disk02/data/eLearning/yyliu/','staffcomment'+sql1[7:20]+'.txt')

file = open(path,'w+')

for i in range(0,len(cc)):
    print >> file, str(cc[i][0]).strip()+"\n"+str(cc[i][1]).strip()+"\n"+str(cc[i][2]).strip()+"\n"+str(cc[i][3]).replace('\n','\\n')+str(cc[i][4]).strip()+"\n"+str(cc[i][5]).strip()+"\n"+str(cc[i][6]).strip()
file.close()