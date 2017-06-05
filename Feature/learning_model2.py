from pandas import DataFrame as df
import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.cross_validation import KFold
from sklearn import datasets, linear_model
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble.gradient_boosting import GradientBoostingRegressor

# names = ['video_id', 'term_id', 'page_number', 'charts_number', 'example_num', 'stt_accuracy',
#          'stt_low_accuracy_ratio', 'flag', 'radio', 'ratio_change', 'word_count', 'animation',
#          'hand_writing', 'speed', 'Label1', 'Label2']


#learning_df = pd.read_csv('/Users/yanyunliu/PycharmProjects/learning_label/LabelCheck/label_updated_all_with12.csv')
learning_df = pd.read_csv('/Users/yanyunliu/PycharmProjects/learning_label/LabelCheck/label_updated_all_v2.csv')


charts_ratio = []
example_ratio = []

for item in range(0,len(learning_df['speed'])):

    #print features.loc[item]['page_number'], features.loc[item]['charts_number'],features.loc[item]['example_num']
    print learning_df.loc[item]['term_id'], learning_df.loc[item]['video_id'], learning_df.loc[item]['charts_number']/learning_df.loc[item]['page_number'], learning_df.loc[item]['example_num']/learning_df.loc[item]['page_number']

    chart_ratio_temp = float(learning_df.loc[item]['charts_number']) / float(learning_df.loc[item]['page_number'])
    example_ratio_temp = float(learning_df.loc[item]['example_num'])/float(learning_df.loc[item]['page_number'])
    charts_ratio.append(chart_ratio_temp)
    example_ratio.append(example_ratio_temp)



charts_ratio_pd = pd.Series(charts_ratio,name='charts_ratio')
print charts_ratio_pd

example_ratio_pd = pd.Series(example_ratio,name='example_ratio')
print example_ratio_pd

learning_df = learning_df.assign(example_ratio=example_ratio_pd.values)
learning_df = learning_df.assign(charts_ratio=charts_ratio_pd.values)

print learning_df

learning_df.to_csv('update_new_feather_v3_new.csv',index=False)



features = learning_df[['page_number','charts_ratio','example_ratio','stt_accuracy',
                                 'stt_low_accuracy_ratio','flag','radio','ratio_change','word_count','animation',
                                 'hand_writing','speed']]
targets = learning_df['Label2']

print features



#print features['speed']

for item in range(0,len(features['speed'])):
    print features['speed'][item]
    #features['speed'][item] = float(features['speed'][item])



features = features.as_matrix(columns=None)
features = np.array(features, dtype=float)
targets = targets.as_matrix(columns=None)

targets = (targets - min(targets))/(max(targets)-min(targets)) + 1
# targets_3 = targets_3 - np.mean(targets_3)
#
print targets
targets = targets.ravel()



estimator = RandomForestRegressor(random_state=0, n_estimators=10)
score = cross_val_score(estimator, features, targets)

print score

#model = SVR()


kf = KFold(n=len(features), n_folds=5, shuffle=True)
cv = 0

lac = []
feature_coef = []

for tr, tst in kf:
    # Train Test Split
    tr_features = features[tr, :]
    tr_target = targets[tr]

    tst_features = features[tst, :]
    tst_target = targets[tst]

    #model = RandomForestRegressor(random_state=0, n_estimators=10)
    #model = linear_model.LinearRegression()
    model = SVR(kernel='linear',C=1)
    #model = DecisionTreeRegressor(max_depth=4)
    #model = GradientBoostingRegressor()
   # model = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),
   #                       n_estimators=300)
    #model = linear_model.LogisticRegression()
    model.fit(tr_features, tr_target)
    #print model.coef_
    #feature_coef.append(model.coef_)
    #print model.feature_importances_
    #feature_coef.append(model.feature_importances_)
    # Measuring training and test accuracy
    #print model.predict(tr_features)
    #print model.predict(tr_features)-tr_target
    tr_accuracy = np.mean(abs(model.predict(tr_features) - tr_target)/tr_target)
    tst_accuracy = np.mean(abs(model.predict(tst_features)-tst_target)/tst_target)

    print "SVC %d Fold Train Accuracy:%f, Test Accuracy:%f" % (
        cv, tr_accuracy, tst_accuracy)

    lac.append(tst_accuracy)

    cv += 1

print np.mean(lac)

# feature_coef = pd.DataFrame(feature_coef,columns=['page_number','charts_number','example_num','stt_accuracy','stt_low_accuracy_ratio',
#                                                        'flag','radio','ratio_change','word_count','animation','hand_writing','speed'])
#
# print np.mean(feature_coef)
# #
# feature_coef.to_csv('feature_coef_linear_model2.csv',header=True, index=False)

print learning_df[['page_number','charts_number','example_num','stt_accuracy',
                                 'stt_low_accuracy_ratio','flag','radio','ratio_change','word_count','animation',
                                 'hand_writing','speed']].mean()

mean_score = learning_df[['page_number','charts_number','example_num','stt_accuracy',
                                 'stt_low_accuracy_ratio','flag','radio','ratio_change','word_count','animation',
                                 'hand_writing','speed']].mean()



# SVC 0 Fold Train Accuracy:0.164252, Test Accuracy:0.153939
# SVC 1 Fold Train Accuracy:0.140325, Test Accuracy:0.149188
# SVC 2 Fold Train Accuracy:0.139801, Test Accuracy:0.135482
# SVC 3 Fold Train Accuracy:0.143419, Test Accuracy:0.149106
# SVC 4 Fold Train Accuracy:0.146128, Test Accuracy:0.182961

