from time import time
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
import numpy as np
from pandas import DataFrame as df
import nltk
import re
import pandas as pd

#discussion_df = pd.read_csv('/Users/yanyunliu/PycharmProjects/learning_label/keyword_test/commentnew/Andriod/keyword_tableAndroid.txt',names=['id'])
discussion_df = pd.read_csv('/Users/yanyunliu/PycharmProjects/learning_label/keyword_test/commentnew/Andriod/keyword_tableJava.txt',names=['id'])

print len(discussion_df['id'])

discussion_count = discussion_df['id'].drop_duplicates()
print len(discussion_count)

discussion_count = pd.DataFrame(discussion_count, columns=['id'])
#
comment_path = '/Users/yanyunliu/PycharmProjects/learning_label/StaffAttend/staffcomment102_1x_4T2015.txt'
#comment_path = '/Users/yanyunliu/PycharmProjects/learning_label/StaffAttend/staffcomment107x_1T2016_c.txt'

comment_file = pd.read_csv(comment_path,
                               names=['id', 'database_id', 'replier_id', 'author_id', 'commentable_id'])

print len(comment_file['id'])

comment_count = comment_file['id'].drop_duplicates()
comment_count = df(comment_count, columns=['id'])
print len(comment_count['id'])

merge_file = comment_count.merge(discussion_count, how='inner')
#print merge_file

print len(comment_count['id'])

print "In discussion forum there is # of comments contain keywords: "
print len(discussion_count['id'])

print "There is # of comments with staff reply"
print len(merge_file['id'])



