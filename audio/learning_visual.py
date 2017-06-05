import pandas as pd
import pprint as pprint
import matplotlib.pyplot as plt

file = open('/Users/yanyunliu/PycharmProjects/Youtube/newchannel/learning/learning_result_android.txt')
#file = open('/Users/yanyunliu/PycharmProjects/Youtube/newchannel/learning/learning_result_java.txt')
file = file.readlines()

filename = []

for line in file:
    temp = line.split("_")[0].split(",")[1]
    #print temp
    filename.append(temp)


filename = pd.Series(filename, name='file')
filename = pd.DataFrame(filename)
android = pd.read_csv('/Users/yanyunliu/PycharmProjects/Youtube/newchannel/learning/learning_result_android.txt',names=['label','detail'])
android = pd.merge(filename, android, left_index= True, right_index= True)

#print android

android_groupby = android.groupby('file')['label']
android_groupby = dict(list(android_groupby))

count  =0

java_result = {}
java_minus_result = {}

java_audio_feature = []

for key, value in android_groupby.items():
    for item in range(1,len(value.values)-1):
        if value.values[item] != value.values[item-1] and value.values[item] != value.values[item+1]:
            count = count + 1
            print value.values[item], value.values[item-1], value.values[item+1]
    print key +',' +str(int(sum(value.values > 0)>sum(value.values < 0)))+',' \
            +str(float(sum(value.values > 0))/float(len(value.values))), float(count)/float(len(value.values))
    temp = [key,int( sum(value.values > 0) > sum(
        value.values < 0)),str(float(sum(value.values > 0))/float(len(value.values))),float(count)/float(len(value.values))]
    java_audio_feature.append(temp)

    count = 0



java_audio_feature = pd.DataFrame(java_audio_feature, columns=['video_id','tag','ratio','ratio_change'])
print java_audio_feature
java_audio_feature.to_csv('/Users/yanyunliu/PycharmProjects/learning_label/learning_model/android_audio_feature.csv',index=False)


#(27/20) Android
#(41/22) Java

