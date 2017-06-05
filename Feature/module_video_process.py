import pandas as pd

#video_id,term_id,page_number,charts_number,example_num,real_duration,mean_duration_watched_all,std_duration_watched_all,
# std_duration,num_finished,num_watched,max_times,num_watched_all,time_spent_ratio,stt_accuracy,stt_low_accuracy_ratio,
# flag,radio,ratio_change,word_count,animation,hand_writing,speed,mean_duration_watched_all_ratio,num_watched_ratio,mean_times


df_module = pd.read_csv('/Users/yanyunliu/PycharmProjects/learning_label/learning_model/module_infor.txt')
df_video = pd.read_csv('/Users/yanyunliu/PycharmProjects/learning_label/learning_model/feature_all.csv')

df_merge = df_module.merge(df_video, how='inner')



df_ratio = list(df_merge.groupby(['term_id','module_number'])['num_watched_ratio'].mean())
print df_merge[['num_watched_ratio','term_id','module_number']]
print df_merge.groupby(['term_id','module_number'])['num_watched_ratio'].mean()

df_check = df_merge

penalty_java = [0.596461295,0.502348245,0.526617187,0.785234281]
penalty_android = [0.420029112,0.605593291,0.675536481,0.92198221]

for i in range(0,len(df_check)):
    #print df_check.loc[i]['module_number'], df_check.loc[i]['term_id'], df_check.loc[i]['num_watched_ratio']

    if df_check.loc[i]['term_id'] == 'COMP102_1x':
        module_index = df_check.loc[i]['module_number']
        if module_index != 0 and module_index <= 4:
            #print module_index-1
            #print len(penalty_java)
            #print penalty_java[module_index-1]
            df_check.loc[i]['num_watched_ratio'] = df_check.loc[i]['num_watched_ratio']*penalty_java[module_index-1]

    if df_check.loc[i]['term_id'] != 'COMP102_1x':
        module_index = df_check.loc[i]['module_number']
        if module_index != 0 and module_index <= 4:
            #print module_index-1
            #print penalty_android[module_index-1]
            df_check.loc[i]['num_watched_ratio'] = df_check.loc[i]['num_watched_ratio']*penalty_android[module_index-1]




label1 = df_check['mean_duration_watched_all_ratio']*0.3+df_check['num_watched_ratio']*0.4+df_check['mean_times']*0.3

print label1.values

label2 = df_check['mean_duration_watched_all_ratio']*0.15+df_check['num_watched_ratio']*0.4+df_check['mean_times']*0.3+df_check['time_spent_ratio']*0.15

print label2
#
df_check = df_check.assign(Label1 = label1.values, Label2 = label2.values)
print df_check
#

df_check.to_csv('label_updated_all_v2.csv')