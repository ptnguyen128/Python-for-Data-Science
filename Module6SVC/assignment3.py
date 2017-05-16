# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 14:54:09 2016

@author: superpup
"""
import pandas as pd
from numpy import arange

Test_PCA = False

#Load data, drop the name column
X = pd.read_csv('/Users/superpup/Documents/edxpython/Module6SVC/Datasets/parkinsons.data')
X = X.drop('name',1)

#Splice out status column into y, delete it from X
y = X['status'].copy()
X = X.drop('status',1)

#Preprocessing
from sklearn import preprocessing
#mascalar = preprocessing.MaxAbsScaler()
#mmscalar = preprocessing.MinMaxScaler()
sscalar = preprocessing.StandardScaler()
X = sscalar.fit_transform(X)

if Test_PCA:
    #Run PCA, n_components ranging from 4 to 14
    from sklearn.decomposition import PCA
    pca = PCA(n_components = 7)
    pca.fit(X)
    T = pca.transform(X)
else:
    #Run ISO, n_neighbors raning from 2 to 5, n_components ranging from 4 to 6
    from sklearn import manifold
    iso = manifold.Isomap(n_neighbors=4,n_components=6)
    iso.fit(X)
    T = iso.transform(X)


#Perform a train test split, 30% test size, random_state=7
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(T, y, test_size=0.3, random_state=7)

#Create a SVC classifier
from sklearn.svm import SVC
#model = SVC()
##Fit against training data
#model.fit(X_train,y_train)
##Score testing data
#print model.score(X_test,y_test)

##Nested for-loops
#Outer for-loop iterating C from 0.05 to 2, 0.05 unit increments
#Inner for-loop iterating gamma from 0.001 to 0.1, 0.001 unit increments
best_score = 0
for C in arange(0.05,2,0.05):
    for gamma in arange(0.001,0.1,0.001):
        model = SVC(C=C,gamma=gamma)
        model.fit(X_train,y_train)
        score = model.score(X_test,y_test)       
        if best_score < score:
            best_score = score
print "Best score: ", best_score," C: ", C," gamma: ",gamma        

