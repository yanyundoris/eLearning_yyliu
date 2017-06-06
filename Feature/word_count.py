import os
import subprocess32


# f = open('/Users/yanyunliu/PycharmProjects/Youtube/newchannel/server_test/test_subtitle.txt')
# time = f.readlines()
# count = 0
#
# num_word = []
# new_file = []
#
# for item in time:
#     item = item.split("-->")[2]
#     newitem = item.replace("\\n"," ")
#     print newitem.split()
#     new_file.append(newitem)
#
# for item in new_file:
#     #print len(item.split())
#     num_word.append(len(item.split()))
#
# print num_word
# print sum(num_word)


#path_subtitle = "/disk02/data/eLearning/raw_teaching_material/transcripts/COMP102_1x/"
path_subtitle = "/disk02/data/eLearning/raw_teaching_material/transcripts/COMP107x_2016T1/"

filepath =open("/disk02/data/eLearning/raw_teaching_material/transcripts/word_count_COMP107x_2016T1.txt","w+")


for directory, subdirector, files in os.walk(path_subtitle):
    for file in files:
        #print file
        filename = file.split(".")[0]
        print filename
        f = open(path_subtitle + file)
        word_file = f.readlines()
        
        num_word = []
        new_file = []
        
        for item in word_file:
            item = item.split("-->")[2]
            newitem = item.replace("\\n", " ")
            #print newitem.split()
            new_file.append(newitem)
        
        for item in new_file:
            # print len(item.split())
            num_word.append(len(item.split()))
        
        print num_word
        print sum(num_word)
        print str(filename)+","+str(sum(num_word))
        print>> filepath, str(filename)+","+str(sum(num_word))

filepath.close()
