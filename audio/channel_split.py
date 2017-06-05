import os
#import subprocess32
import ffmpy
from pydub import AudioSegment
import os
import subprocess32
#import subprocess
import ffmpy
import wave

#command = "ffmpeg -i /Users/yanyunliu/Downloads/video/w1_index.wav -ar 16000 /Users/yanyunliu/Downloads/video/w1_index.flac"
#subprocess.call(command, shell=True)

middle = ' -ar 16000  -ac 1  '
path = "/disk02/data/eLearning/raw_teaching_material/Java_audio/"
path_save = "/disk02/data/eLearning/raw_teaching_material/Java_audio_channel/All/"
pathnew = "/Users/yanyunliu/PycharmProjects/Youtube/newchannel/"
head = 'ffmpeg -i  '
space = ' '
count = 0

for directory, subdirectory, files in os.walk(path):
    for file in files:
        if file.endswith(".wav"):
            f_name = os.path.splitext(file)
            count = count + 1
            commend = head +path+file +space+ middle +path_save + f_name[0] +'_'+str(count)+'.wav'
            print commend
            subprocess32.call(commend, shell=True)
            #subprocess.call(commend, shell=True)

path_save = "/disk02/data/eLearning/raw_teaching_material/Java_audio_channel/All/"
path_subtitle = "/disk02/data/eLearning/raw_teaching_material/transcripts/COMP102_1x/"
path_split = '/disk02/data/eLearning/raw_teaching_material/Java_audio_channel/split/'

for directory, subdirector, files in os.walk(path_subtitle):
    for file in files:
        #print file
        filename = file.split(".")[0]
        for audio_dirctory, audio_subdirectory, audio_files in os.walk(path_save):
            for audio_file in audio_files:
                #print audio_file
                if audio_file.split(".")[0].split('_')[0] == filename:
                    sound = AudioSegment.from_wav(path_save+audio_file)
                    f = open(path_subtitle + file)
                    time = f.readlines()
                    count = 0
                    for item in time:
                        #print item.split("--->")[0], item.split("--->")[1]
                        #print int(str(item.split("--->")[0]).split(".")[0]) * 1000 + int(
                        #    str(item.split("--->")[0]).split(".")[1]) * 10
                        #print int(str(item.split("--->")[1]).split(".")[0]) * 1000 + int(
                         #   str(item.split("--->")[1]).split(".")[1]) * 10
                        start_time = int(str(item.split("--->")[0]).split(".")[0]) * 1000 + int(
                            str(item.split("--->")[0]).split(".")[1]) * 10
                        stop_time = int(str(item.split("--->")[1]).split(".")[0]) * 1000 + int(
                            str(item.split("--->")[1]).split(".")[1]) * 10
                        print start_time, stop_time
                        word = sound[start_time:stop_time]
                        save_name = path_split+audio_file.split(".")[0] +'_'+ str(count) + '.wav'
                        print save_name
                        print count
                        count = count + 1
                        word.export(save_name, format="wav")



        file_name = "/Users/yanyunliu/PycharmProjects/Youtube/newchannel/server_test/04229dc8688948f0a98d18e2d1815282.wav"
        sound = AudioSegment.from_wav(file_name)

f = open('/Users/yanyunliu/PycharmProjects/Youtube/newchannel/server_test/test_subtitle.txt')
time = f.readlines()


count = 0
for item in time:
    print item.split("--->")[0], item.split("--->")[1]
    print int(str(item.split("--->")[0]).split(".")[0]) * 1000 + int(str(item.split("--->")[0]).split(".")[1]) * 10
    print int(str(item.split("--->")[1]).split(".")[0]) * 1000 + int(str(item.split("--->")[1]).split(".")[1]) * 10
    start_time = int(str(item.split("--->")[0]).split(".")[0]) * 1000 + int(str(item.split("--->")[0]).split(".")[1]) * 10
    stop_time = int(str(item.split("--->")[1]).split(".")[0]) * 1000 + int(str(item.split("--->")[1]).split(".")[1]) * 10
    print start_time, stop_time

    word = sound[start_time:stop_time]
    save_name = "word" + str(count) + '.wav'
    print save_name
    count = count +1
    word.export(save_name, format="wav")
