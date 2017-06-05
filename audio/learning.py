import pandas as pd
import numpy as np
import math
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier


data = pd.read_table('/Users/yanyunliu/datafile/resultv2.txt',sep = '\t',header = None)
#testdata = pd.read_table('/Users/yanyunliu/datafile/result_android.txt',sep = '\t',header = None)
testdata = pd.read_table('/Users/yanyunliu/datafile/result_java.txt',sep = '\t',header = None)
#data = pd.read_table('/Users/yanyunliu/datafile/result.txt',sep = '\t',header = None)
n_features = 13

data = data.as_matrix(columns=None)
testdata = testdata.as_matrix(columns=None)
data = data[0][0:(data.shape[1]-1)]
testdata = testdata[0][0:(testdata.shape[1]-1)]

data = np.reshape(data,(len(data)/n_features,n_features))
testdata = np.reshape(testdata,(len(testdata)/n_features,13))

featurestest = testdata[:,0:12]
features = data[225:300,0:12]
targets = data[225:300:,12:13]


#data = data.as_matrix(columns=None)
#data = data[0][0:6240]
#data = np.reshape(data,(480,13))
#features = data[0:300,0:12]
#targets = data[0:300:,12:13]

#for i in range(0,len(features[0])):
#    print i
#    features_temp = features[:,i:i+1]
#    kmeans_temp = KMeans(n_clusters=7,random_state=0).fit(features_temp)
#    k1 = kmeans_temp.labels_.ravel()
#    k1 = pd.DataFrame(k1)
#    k1 = k1.as_matrix(columns=None)
#    features[:,i:i+1] = k1

features = features.astype(float)
features -= np.mean(features, axis=0)
features /= np.std(features, axis=0)

featurestest = featurestest.astype(float)
featurestest -= np.mean(featurestest, axis=0)
featurestest /= np.std(featurestest, axis=0)

targets = targets.ravel()

clf = SVC()
#clf = LogisticRegression()
#clf = GaussianNB()
clf.fit(features,targets)

scores = cross_val_score(clf, features, targets, cv=5)
sum1 = sum(scores)/5
print scores

f = open('learning_result_java.txt','w+')

for i in range(0,len(testdata[:,12:13])):
    print>>f, str(clf.predict(featurestest)[i])+','+ testdata[:,12:13][i][0]

f.close()

# ## Get label
# if file_name == 'n':
#     #   feature_line.append(filter(str.isalpha, f_name[0]))
#     feature_line.append(-1)
# elif file_name == 'a' or file_name == 'su' or file_name == 'h':
#     feature_line.append(1)
# print file_name