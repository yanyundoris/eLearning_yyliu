import re
import pandas as pd
from pandas import DataFrame as df
import numpy as np

#f = open('/Users/yanyunliu/PycharmProjects/learning_label/keyword_test/commentnew/Andriod/AndroidBody1.txt')
f= open('/Users/yanyunliu/PycharmProjects/learning_label/keyword_test/commentnew/Andriod/JavaBody1.txt')

id, body=list(), list()

while True:
    t = f.readline().strip()
    if t == '':
        break
    id.append(t)
    body.append(f.readline().strip())
discussion = np.array([id, body]).T

discussion_df = df(discussion, columns=['id', 'body'])
print discussion_df

merge_keyword = ['emulator',
'haxm',
'greetfriend',
'application',
'server',
'view',
'button',
'acceleration',
'activity',
'configuration',
'version',
'manager']
#'mahine']
#

merge_keyword = [

'abstraction',
'canvas',
'object',
' io',
'colorimage',
'constructor',
'choice',
'instance',
'cards',
'loop'
]
#f = open('keyword_table'+'Java'+'.txt','w+')
#
for word in merge_keyword:
    print word
    for i in range(0,len(discussion_df['body'])):
        if re.search(word,discussion_df['body'][i]):
#            print>>f, discussion_df['id'][i]
            print discussion_df['id'][i]
#
#
f.close()
