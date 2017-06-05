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


learning_df = pd.read_csv('/Users/yanyunliu/PycharmProjects/learning_label/LabelCheck/label_updated_all.csv')

features = learning_df[['page_number','charts_number','example_num','stt_accuracy',
                                 'stt_low_accuracy_ratio','flag','radio','ratio_change','word_count','animation',
                                 'hand_writing','speed']]
targets = learning_df['Label2']

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
importances = []
for tr, tst in kf:
    # Train Test Split
    tr_features = features[tr, :]
    tr_target = targets[tr]

    tst_features = features[tst, :]
    tst_target = targets[tst]

    model = RandomForestRegressor(random_state=0, n_estimators=10)
    #model = linear_model.LinearRegression()
    #model = SVR()
    #model = DecisionTreeRegressor(max_depth=4)
    #model = GradientBoostingRegressor()
    #model = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),
#                          n_estimators=300)
    model.fit(tr_features, tr_target)
    # print model.feature_importances_
    importances.append(model.feature_importances_)
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
feature_importance = pd.DataFrame(importances,columns=['page_number','charts_number','example_num','stt_accuracy','stt_low_accuracy_ratio',
                                                       'flag','radio','ratio_change','word_count','animation','hand_writing','speed'])

print np.mean(feature_importance)

#feature_importance.to_csv('feature_importace_randomforest_updatelabel2.csv',header=True, index=False)




''''
m = pd.read_csv('mfeature2.csv', names= ["target","06:00:00","06:20:00", "06:40:00", "07:00:00","07:20:00", "07:40:00"])

m = m.as_matrix()


X_full, y_full = m[:,1:8], m[:,0:1].ravel()

# Estimate the score on the entire dataset, with no missing values
estimator = RandomForestRegressor(random_state=0, n_estimators=10)
score = cross_val_score(estimator, X_full, y_full)

print score
#print("Score with the entire dataset = %.2f" % score)

kf = KFold(n=len(X_full), n_folds=5, shuffle=True)
cv = 0

lac = []
for tr, tst in kf:
    # Train Test Split
    tr_features = X_full[tr, :]
    tr_target = y_full[tr]

    tst_features = X_full[tst, :]
    tst_target = y_full[tst]

    #model = RandomForestRegressor(random_state=0, n_estimators=10)
    #model = linear_model.LinearRegression()
    #model = SVR()
    #model = DecisionTreeRegressor(max_depth=4)
    #model = GradientBoostingRegressor()
    model = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),
                          n_estimators=300)
    model.fit(tr_features, tr_target)
    # Measuring training and test accuracy
    tr_accuracy = np.mean(abs((model.predict(tr_features) - tr_target)/tr_target))
    tst_accuracy = np.mean(abs((model.predict(tst_features)-tst_target)/tst_target))

    print "SVC %d Fold Train Accuracy:%f, Test Accuracy:%f" % (
        cv, tr_accuracy, tst_accuracy)

    lac.append(tst_accuracy)

    cv += 1

print np.mean(lac)

'''''

feature_target = learning_df[['page_number','charts_number','example_num','stt_accuracy','stt_low_accuracy_ratio',
                                                       'flag','radio','ratio_change','word_count','animation','hand_writing','speed','Label']].as_matrix(columns=None)
feature_target = np.array(feature_target, dtype=float).T
#
print feature_target.shape
#
core = np.corrcoef(feature_target)
np.savetxt('corrcoef_new.txt',core)
#
print np.corrcoef(feature_target)
