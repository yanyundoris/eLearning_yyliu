# There are some files containing raw features:
1. android_slides_stats_info.txt: Android slides infromation including page number, num of examples, num of charts
2. java_slides_stats_info.txt: Java slides inforamtion with same format as android
3. android_java_merge_audio.csv: Java & Android audio feature including tag, emotion(named as ratio), emotion change(name as ratio change)
4. feature_import.txt: Feature extracted from database including term_id,video_id,sequence,real_duration,mean_duration_watched_all,std_duration_watched_all,std_duration,num_finished,num_watched,mean_times,max_times,num_watched_all,watched_area1,watched_area2,watched_area3,time_spent_ratio,emotion,emotion_change,speed,stt_accuracy,stt_low_accuracy_ratio,animation,hand_writing,example,charts,highlight
5. word_count.csv: num of words in each video for java & android. (same, word_count_COMP102_1x.txt is the num of words for java and word_count_COMP107x_2016T1.txt is the num of words for android)

# There are some files we use to get these features:

1. android_slides_stats_info.txt & java_slides_stats_info.txt: Slides analysis part.
2. android_java_merge_audio.csv: Refer to audio analysis part.
3. feature_import.txt: Get from database
4. word_count.csv, word_count_COMP102_1x.txt, word_count_COMP107x_2016T1.txt: Get from word_count.py

# Merge all these feature together: 
1. import_feature.py: merge audio, word cont and sildes information together and output feature_all.
2. feature_all.csv: Including features in the first stage.

# Adding module information

1. module_video.py: extract term_id, video_id, module_number, module_part, sequence from database and output module_infor.txt
2. module_video_process.py: Get label from clickstream pattern and add penalty, output label_updated_all_v2.csv

# Pose-processing:
1. update_new_feather_v3.csv: normalization mannually
2. Save_rank_final.csv: get ranking for each feature mannually.

# Learning model:

1. learning_model2.py: SVM model for score prediction.

# Feature ranking:

1. GetFeatureImportance.py: use randonforest model to get feature importance.
2. GetLinearCoef.py: use linear regression model to get coefficient. 



