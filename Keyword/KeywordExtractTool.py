from time import time
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
import numpy as np
from pandas import DataFrame as df
import nltk
import re
import pandas as pd
import os

stopwordread = open('sw.txt')
stopwordlist = stopwordread.readlines()
stopwordlist = [s.strip() for s in stopwordlist]
#add_stopword = ['data','code','class','course','reasons','problem','question','error','errors','hello','see','use','please','help','hi','comp102x','write','life','program','wrong','public']
add_stopword = ['03','anyone','others','example','course','hello']
original = nltk.corpus.stopwords.words('english')
stopwordlist = stopwordlist+ original + add_stopword



def TfidfFeature_v1(sample, treshold, min_df_n, n_features, stopwordlist):
    tfidf_vectorizer = TfidfVectorizer(max_df=treshold, min_df=min_df_n,
                                       max_features=n_features,
                                       stop_words=stopwordlist)
    tfidf_matrix = tfidf_vectorizer.fit_transform(sample)

    feature_names = tfidf_vectorizer.get_feature_names()
    tfidf_feature = TfidfTransformer()
    feature_importance = tfidf_vectorizer.idf_
    return (feature_importance, feature_names, tfidf_matrix)


def TfidfFeature_v2(sample, treshold, min_df_n, n_features, stopwordlist):
    tfidf_vectorizer = CountVectorizer(max_df=treshold, min_df=min_df_n,
                                    max_features=n_features,
                                    stop_words=stopwordlist)

    tfidf_matrix = tfidf_vectorizer.fit_transform(sample)
    feature_names = tfidf_vectorizer.get_feature_names()
    tfidf_feature =TfidfTransformer(norm="l2").fit(tfidf_matrix)
    feature_importance = tfidf_feature.idf_
    return (feature_importance, feature_names, tfidf_matrix)



def GetRawLDATopNTopic(tfidf,tfidf_feature_names,n_top_words,n_topics):
    lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=10,
                                     learning_method='online',
                                     learning_offset=50.,
                                     random_state=0)
    lda.fit(tfidf)

    topic_list = []

    temp_list = []

    for topic_idx, topic in enumerate(lda.components_):
        temp = " ".join([tfidf_feature_names[i]
                         for i in topic.argsort()[:-n_top_words - 1:-1]])


        for i in topic.argsort()[:-n_top_words - 1:-1]:
            temp_list.append(tfidf_feature_names[i])

        #topic_list.append(temp)

        topic_list.append(temp)

    return (temp_list, lda)


def GetRawNMFTopNTopic(tfidf,tfidf_feature_names,n_top_words,n_topics):

    nmf = NMF(n_components=n_topics, random_state=1,
              alpha=.1, l1_ratio=.5).fit(tfidf)

    topic_list = []

    temp_list = []

    for topic_idx, topic in enumerate(nmf.components_):
        temp = " ".join([tfidf_feature_names[i]
                         for i in topic.argsort()[:-n_top_words - 1:-1]])

        # temp_list.append([tfidf_feature_names[i]
        #                  for i in topic.argsort()[:-n_top_words - 1:-1]])

        for i in topic.argsort()[:-n_top_words - 1:-1]:
            temp_list.append(tfidf_feature_names[i])


        topic_list.append(temp)

    # print("**************",temp_list)

    return (temp_list, nmf)


#the return is a list
def GetFreqLit(tfidf_list,threshold):

    dict_freq = nltk.FreqDist([])

    for item in tfidf_list:
        dict_temp = nltk.FreqDist(item)
        dict_freq.update(dict_temp)

    dict_freq = dict(dict_freq)


    High_Freq = []

    for key, value in dict_freq.items():
        # print key
        if value > threshold:
            High_Freq.append(key)


    return High_Freq

def GetLowFreqLit(tfidf_list,threshold):

    dict_freq = nltk.FreqDist([])

    for item in tfidf_list:
        dict_temp = nltk.FreqDist(item)
        print(dict_temp)
        dict_freq.update(dict_temp)

    dict_freq = dict(dict_freq)

    print(dict_freq)

    Low_Freq = []

    for key, value in dict_freq.items():
        # print key
        if value <= threshold:
            print(key)
            Low_Freq.append(key)

    print(Low_Freq)
    return Low_Freq


def SortTfidfByTopNWeight(feature_importance,feature_names,n):

    top_feature_sort = []

    for i in feature_importance.argsort()[:-n - 1:-1]:
        top_feature_sort.append(feature_names[i])

    #print(top_feature_sort)

    return(top_feature_sort)



def GetListCharacter(list):
    for line in list:
        chara = nltk.pos_tag(line)
        print(chara)
    #return chara


def ListToFile(filename):

    new_file = []

    for lines in filename:
        temp = " ".join(word for word in lines)
        new_file.append(temp)

    return new_file


def CutType(tpye):
    new_type = []
    temp  = []
    for w in tpye:
        temp =  w[0:2]
        new_type.append(temp)

    return new_type

word_type = 'NN'

def RemoveNotNounsForList(top_feature,word_type):
    ll = nltk.pos_tag(top_feature)
    ll = dict(ll)
    top_feature_filter = []

    for word, tag in ll.items():
        if tag.startswith(word_type):
            top_feature_filter.append(word)

    return top_feature_filter


def GetModuleTopicList(discussion_pd,treshold,n_top_words, n_topics,n_features, min_df_n):

    tfidf_list = []
    total_feature = []
    total_lda_topic_list = []
    total_nmf_topic_list = []

    for i in range(0,len(discussion_pd)):

        #print i
        #print len(discussion_pd)

        sub_module = list(discussion_pd)[i][1]
        kk1 = sub_module['body']
        title_type = set(sub_module['type'].tolist())
        corpus = kk1
        (tfidf_feature_importance, tfidf_feature_names, tfidf) = TfidfFeature_v1(corpus,treshold, min_df_n, n_features, stopwordlist)
        sorted_feature_name = SortTfidfByTopNWeight(tfidf_feature_importance, tfidf_feature_names,n_features)
        total_feature.append(sorted_feature_name)
        (topic_list_nmf, nmf) = GetRawNMFTopNTopic(tfidf, tfidf_feature_names, n_top_words, n_topics)
        (topic_list_lda, lda) = GetRawLDATopNTopic(tfidf, tfidf_feature_names, n_top_words, n_topics)

        total_lda_topic_list.append(topic_list_lda)
        total_nmf_topic_list.append(topic_list_nmf)
        tfidf_list.append(sorted_feature_name)

    return (tfidf_list,total_lda_topic_list, total_nmf_topic_list)


def FilterTopicByFrequency(topic_list,High_freq_list):

    filtered_topic = []
    filter_topic_list = []

    for line in topic_list:
        #print(line)
        for word in line:
            if word not in High_freq_list:
                #print(word)
                filtered_topic.append(word)

        if filtered_topic == []:

            #continue
            filter_topic_list.append([])
        else:
            filter_topic_list.append(filtered_topic)

            filtered_topic = []

    print "Filter Topic List", filter_topic_list
    return filter_topic_list


def FilterTopicByFrequency(topic_list,High_freq_list):

    filtered_topic = []
    filter_topic_list = []

    for line in topic_list:
        #print(line)
        for word in line:
            if word not in High_freq_list:
                #print(word)
                filtered_topic.append(word)

        if filtered_topic == []:

            #continue
            filter_topic_list.append([])
        else:
            filter_topic_list.append(filtered_topic)

            filtered_topic = []

    print "Filter Topic List", filter_topic_list
    return filter_topic_list


def GetCommentsDF(filename):
    f = open(filename,'r')


    id, comment_type, title, body, votes_up, votes_down, com_count = list(), list(), list(), list(), \
                                                                     list(), list(), list()

    while True:
        t = f.readline().strip()
        if t == '':
            break
        id.append(t)
        comment_type.append(f.readline().strip())
        title.append(f.readline().strip())
        body.append(f.readline().strip())
        votes_up.append(f.readline().strip())
        votes_down.append(f.readline().strip())
        com_count.append(f.readline().strip())


    comment_type_cut = CutType(comment_type)

    print "comment type:",comment_type
    print "comment type cut:",comment_type_cut


    discussion = np.array([id, comment_type, title, body, votes_up, votes_down, com_count]).T
    discussion_cut = np.array([id, comment_type_cut, title, body, votes_up, votes_down, com_count]).T


    discussion_df = df(discussion, columns=['id','type', 'title', 'body','vote_up','vote_down','count'])
    discussion_df_cut = df(discussion_cut, columns=['id','type', 'title', 'body','vote_up','vote_down','count'])

    pathname = os.getcwd()


    return discussion_df, discussion_df_cut


def RemoveChara(Filtered_topic_model_cut,filtertype = 'NN'):
    RemoveChara_topic_model_cut = []
    count = 0
    for line in Filtered_topic_model_cut:

        line_temp = RemoveNotNounsForList(line, filtertype)
        # print line_temp
        if line_temp == []:
            RemoveChara_topic_model_cut.append([count, []])
        else:
            RemoveChara_topic_model_cut.append([count, line_temp])

        count = count + 1

    return RemoveChara_topic_model_cut


def MergeKeywordByEnsemble(RemoveChara_topic_lda_cut, RemoveChara_topic_nmf_cut):

    merge_keyword = []

    for i in range(0,len(RemoveChara_topic_lda_cut)):
        #print len(RemoveChara_topic_lda_cut)
        temp = RemoveChara_topic_lda_cut[i][1] + RemoveChara_topic_nmf_cut[i][1]
        temp = list(set(temp))
        temp = [i,temp]
        #print temp
        if temp[1] == []:
            continue
        else:
            merge_keyword.append(temp)

    print merge_keyword
    return merge_keyword


def Keyword2Table(merge_keyword, discussion_df_cut, discussion_df, tablename=" "):
    f = open('keyword_table' + tablename + '.txt', 'w+')

    for line in merge_keyword:
        # print line
        # print(len(line))
        for word in line[1]:
            #print(word)
            for i in range(0, len(discussion_df_cut['body'])):
                if re.search(word, discussion_df_cut['body'][i]):
                    print>> f, discussion_df['id'][i]
                    print>> f, discussion_df['type'][i]
                    print>> f, word
                    print>> f, discussion_df['vote_up'][i]
                    print>> f, discussion_df['vote_down'][i]
                    print>> f, discussion_df['count'][i]

                    weight = discussion_df['vote_up'].astype(int)[i] + 1 - discussion_df['vote_down'].astype(int)[i]

                    print>> f, weight
                    print>> f, discussion_df['count'].astype(int)[i] * weight

    f.close()


def GetDiscussionSummary(discussion_df):


    discussion_df['vote_up'] = discussion_df['vote_up'].astype(int)
    discussion_df['vote_down'] = discussion_df['vote_down'].astype(int)
    discussion_df['count'] = discussion_df['count'].astype(int)

    discussion_groupby_type_sum = df(discussion_df.groupby(['type'])['vote_up', 'vote_down', 'count'].sum(),
                                     columns=['vote_up', 'vote_down', 'count'])
    discussion_id_count = df(discussion_df.groupby(['type'])['id'].count(), columns=['id'])
    # print discussion_id_count

    # print discussion_id_count.index

    count_up = df(discussion_df[discussion_df['count'] > 0],
                  columns=['id', 'type', 'title', 'body', 'vote_up', 'vote_down', 'count'])
    # count_up = df(count_up.groupby(['type'])['count'].count(), columns=['non_zero'])
    count_nonzero = count_up.groupby(['type'])['count'].count()

    count_nonzero = count_nonzero.to_frame(name='count_0')

    print count_nonzero
    print type(count_nonzero)

    # print count_nonzero.to_frame()

    # df_have_reply = pd.DataFrame(count_nonzero,columns=['have-reply'])
    #
    # print df_have_reply
    discussion_groupby_type_sum = pd.merge(discussion_id_count, discussion_groupby_type_sum, left_index=True,
                                           right_index=True)
    #

    discussion_groupby_type_sum = pd.merge(discussion_groupby_type_sum, count_nonzero, left_index=True,
                                           right_index=True)
    #
    print(discussion_groupby_type_sum)

    discussion_groupby_type_sum['weight_sum'] = discussion_groupby_type_sum['vote_up'] + 1 - \
                                                discussion_groupby_type_sum['vote_down']
    print discussion_groupby_type_sum
    #
    pathname = os.getcwd()
    print pathname
    discussion_groupby_type_sum.to_csv(pathname+'/discussion_module_new.txt', index=True)

    print '*' * 30

    print '*' * 30


def GetKeywordSummary(filepath = ''):

    f = open(filepath)

    id, comment_type, word, votes_up, votes_down, com_count, weight, weight_count = list(), list(), list(), list(), \
                                                                                    list(), list(), list(), list()

    while True:
        t = f.readline().strip()
        if t == '':
            break
        id.append(t)
        comment_type.append(f.readline().strip())
        word.append(f.readline().strip())
        votes_up.append(f.readline().strip())
        votes_down.append(f.readline().strip())
        com_count.append(f.readline().strip())
        weight.append(f.readline().strip())
        weight_count.append(f.readline().strip())

    discussion = np.array([id, comment_type, word, votes_up, votes_down, com_count, weight, weight_count]).T

    comment_type_cut = CutType(comment_type)

    discussion_cut = np.array([id, comment_type_cut, word, votes_up, votes_down, com_count, weight, weight_count]).T

    discussion_df = df(discussion, columns=['id', 'comment_type', 'word', 'votes_up', 'votes_down',
                                            'com_count', 'weight', 'weight_count'])

    discussion_df_cut = df(discussion_cut, columns=['id', 'comment_type_cut', 'word', 'votes_up', 'votes_down',
                                                    'com_count', 'weight', 'weight_count'])

    print type(discussion_df)
    print type(discussion_df_cut)

    pathname = os.getcwd()

    discussion_df.to_csv(pathname + '/keyword_summary.txt', index=False)
    discussion_df_cut.to_csv(pathname + '/keyword_cut_summary.txt', index=False)