import pandas as pd

f = open('feature_import.txt')

f = f.readlines()

feature = []

for line in f:
    #print line.strip().split("##")
    feature.append(line.strip().split("##"))
    #print len(line.strip().split("##"))


feature_df = pd.DataFrame(feature, columns=['term_id','video_id','sequence','real_duration','mean_duration_watched_all'
                                            ,'std_duration_watched_all','std_duration','num_finished','num_watched'
                                            ,'mean_times','max_times','num_watched_all','watched_area1','watched_area2',
                                            'watched_area3','time_spent_ratio','emotion','emotion_change','speed',
                                            'stt_accuracy','stt_low_accuracy_ratio','animation','hand_writing','example',
                                            'charts','highlight'])
#print feature_df

f = open('android_slides_stats_info.txt')

f = f.readlines()

feature = []

for line in f:
    #print line.strip().split(";")
    feature.append(line.strip().split(";"))
    #print len(line.strip().split(";"))

# andriod_df = pd.DataFrame(feature, columns=['video_id','page_number','charts_number','example_num'])
#
# print andriod_df
#
f = open('java_slides_stats_info.txt')

f = f.readlines()


for line in f:
    #print line.strip().split(";")
    feature.append(line.strip().split(";"))
    #print len(line.strip().split(";"))

java_android_df = pd.DataFrame(feature, columns=['video_id','page_number','charts_number','example_num'])

print java_android_df
print feature_df

df_merge = java_android_df.merge(feature_df, how='inner')

print df_merge

df_java_audio = pd.read_csv('android_java_merge_audio.csv',names=['video_id','flag','radio','ratio_change'])
df_merge = df_merge.merge(df_java_audio, how='inner')

print df_merge

word_count = pd.read_csv('word_count.csv',names=['video_id','word_count'])
df_merge = df_merge.merge(word_count, how='inner')

#print df_merge['an']

df_merge.to_csv('feature_all.csv',index=False,header=True)



