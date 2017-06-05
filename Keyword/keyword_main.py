from KeywordExtractTool import *

n_features =200
n_topics = 1
n_top_words = 3
top_n_filter = 3
#top_n_filter = 1
treshold = 0.7
min_df_n= 2


os.chdir('/Users/yanyunliu/PycharmProjects/learning_label/Code_summary/eLearning_yyliu/Keyword')
filename = "102_1x_4T2015_commentthread_processed.txt"
discussion_df, discussion_df_cut = GetCommentsDF(filename)

discussion_groupby_type = discussion_df.groupby(['type'])['id','title', 'body','vote_up','vote_down','count']
discussion_groupby_type_cut = discussion_df_cut.groupby(['type'])['id','title', 'body','vote_up','vote_down','count']

print '*' *100
[tfidf_module, lda_no_merge, nmf_no_merge] = GetModuleTopicList(discussion_groupby_type,treshold,n_top_words, n_topics,n_features, min_df_n)
#[lda_nocut, nmf_nocut] = GetModuleTopicList(discussion_groupby_type,treshold,n_top_words, n_topics,n_features)

print '*' *100


print "LDA",lda_no_merge
print "NMF", nmf_no_merge
print "Tfidf", tfidf_module[0]

High_Freq_cut = GetFreqLit(tfidf_module,top_n_filter)


Filtered_topic_lda_cut = FilterTopicByFrequency(lda_no_merge, High_Freq_cut)
Filtered_topic_nmf_cut = FilterTopicByFrequency(nmf_no_merge, High_Freq_cut)

for line in Filtered_topic_lda_cut:
    GetListCharacter([line])

for line in Filtered_topic_nmf_cut:
    GetListCharacter([line])


RemoveChara_topic_lda_cut = RemoveChara(Filtered_topic_lda_cut,filtertype = 'NN')
RemoveChara_topic_nmf_cut = RemoveChara(Filtered_topic_nmf_cut,filtertype = 'NN')


merge_keyword = MergeKeywordByEnsemble(RemoveChara_topic_lda_cut, RemoveChara_topic_nmf_cut)

Keyword2Table(merge_keyword, discussion_df_cut, discussion_df, tablename='102_1x_4T2015_new')

GetDiscussionSummary(discussion_df)
GetKeywordSummary(filepath = 'keyword_table102_1x_4T2015_new.txt')
