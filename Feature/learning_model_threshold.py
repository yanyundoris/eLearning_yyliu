import pandas as pd




def GetAvgFeature(feature_list,df):

    mean_standard = {}

    ColumnName = list(df)

    for item in ColumnName:
        if item in feature_list:
            if  df[item].dtype != 'object':
                #print df[item].mean()
                if item not in mean_standard.keys():
                    mean_standard[item] = df[item].mean()


    interested_features = df[feature_list]

    print mean_standard
    return mean_standard, interested_features

def GetDifference(feature_list,mean_standard,df):

    difference_value =[]

    for col_name in feature_list:
        # col_list = list(df[col_name])
        for item in range(0,len(df)):
            col_value = df.loc[item][col_name]
            if df[col_name].dtype != 'object':
                print col_name, item, df[df[col_name]>col_value][col_name].mean(), df[df[col_name]<col_value][col_name].mean(),\
                    mean_standard[col_name]

                difference_up = df[df[col_name]>col_value][col_name].mean() - mean_standard[col_name]
                difference_down = df[df[col_name]<col_value][col_name].mean() - mean_standard[col_name]

                difference = abs(difference_up) + abs(difference_down)

                difference_value.append([item,col_name,difference])


    print difference_value

    difference_value_df = pd.DataFrame(difference_value, columns=['index_num','col_name','difference'])

    print difference_value_df

    difference_value_df.to_csv('max_difference_table.csv')

    print difference_value_df.groupby(['col_name'])['difference'].idxmax()
    #
    max_index = difference_value_df.groupby(['col_name'])['difference'].idxmax()
    #
    print difference_value_df.loc[max_index]


    #print  df[df['difference']==difference_value_df.groupby(['col_name'])['difference'].transform(max)]
    #
    # print dict(difference_value_df.groupby(['col_name'])['difference'].max())
    #
    # max_dict = dict(difference_value_df.groupby(['col_name'])['difference'].max())
    #
    # for key, value in max_dict.items():
    #     print df[df[key] == value].index  .tolist()
    #
    # #df[df['BoolCol'] == True].index.tolist()
    #
    # return difference_value_df







if __name__=="__main__":


    df_data = pd.read_csv('/Users/yanyunliu/PycharmProjects/learning_label/LabelCheck/update_new_feather_v3.csv',
                          index_col=None)

    # ColumnName = list(df_data)
    # print len(list(df_data)), ColumnName

    feature_list = ['video_id', 'term_id', 'page_number', 'charts_ratio', 'example_ratio', 'radio', 'ratio_change', 'word_count', 'animation',
                    'hand_writing', 'speed']

    mean_standard, feature_df = GetAvgFeature(feature_list, df_data)

    print list(feature_df['charts_ratio'])

    GetDifference(feature_list, mean_standard, feature_df)

