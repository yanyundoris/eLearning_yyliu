import pandas as pd

def LoadData(staff_path,comment_path):
    staff_file = pd.read_csv(staff_path, names=['staff_id'])
    comment_file = pd.read_csv(comment_path,
                               names=['comment_thread_id', 'database_id', 'replier_id', 'author_id', 'commentable_id'])

    return staff_file, comment_file

def IdMatching(staff_file, comment_file):

    merge_file = comment_file.merge(staff_file, how ='left', left_on='replier_id',right_on='staff_id',indicator=True)
    merge_file = merge_file[merge_file['_merge']=='both'].groupby(['commentable_id']).count()

    return merge_file


def GroupByModule(comment_file):

    comment_group = comment_file.groupby(['commentable_id']).count()

    return  comment_group



if __name__ == '__main__':


    staff_path = '/Users/yanyunliu/PycharmProjects/learning_label/StaffAttend/102_1x_4T2015staffrole.txt'
    comment_path = '/Users/yanyunliu/PycharmProjects/learning_label/StaffAttend/staffcomment102_1x_4T2015.txt'

    #staff_path = '/Users/yanyunliu/PycharmProjects/learning_label/StaffAttend/107_1T2016staffrole.txt'
    #comment_path = '/Users/yanyunliu/PycharmProjects/learning_label/StaffAttend/staffcomment107x_1T2016_c.txt'

    staff_file, comment_file = LoadData(staff_path, comment_path)

    print staff_file
    merge_file = IdMatching(staff_file, comment_file)

    print len(list(merge_file['author_id'])), merge_file

    merge_count = list(merge_file['author_id'])
    merge_index_name = list(merge_file.index)
    print merge_index_name, len(merge_index_name)

    comment_group = GroupByModule(comment_file)

    print list(comment_group.index)

    module_name = list(comment_group.index)

    print len(list(comment_group['author_id']))
    group_count = list(comment_group['author_id'])


    print group_count

    count = 0

    for i in range(0,len(merge_count)):
        if module_name[i] in merge_index_name:
            count = count + 1
            print '"'+module_name[i]+'"', float(merge_count[i])/float(group_count[i]),','
            #print '"'+'m'+str(count)+'"'+':', float(merge_count[i])/float(group_count[i]),','



    print sum(group_count[2:12]), sum(merge_count[2:12]), float(sum(merge_count[2:12]))/float(sum(group_count[2:12]))

    print sum(group_count), sum(merge_count)

    print float(sum(merge_count))/float(sum(group_count)), sum(merge_count), sum(group_count)
