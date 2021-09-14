import numpy as np
import pandas as pd
from matplotlib import pyplot
mrsapred = pd.read_csv("/MRSApred_descautocor1.csv")

#Drop the Label column
X = mrsapred.drop('Label', axis = 1)
y = mrsapred['Label']

#Split the dataset as training and testing
from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size = 0.25)

#Find best parameters
"""paramgrid = {'n_estimators': [10, 100, 200, 300, 400, 500,600,700,800,900,1000], 'bootstrap': ['True', 'False'],'max_features' :['auto', 'sqrt', 'log2']}
grid = GridSearchCV(RandomForestClassifier(), paramgrid)
grid.fit(Xtrain, ytrain)
ypred = grid.predict(Xtest)
print(grid.best_params_)"""

#Random Forest model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators = 300)
model.fit(Xtrain, ytrain)
ypred = model.predict(Xtest)\

#Cross-validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=10)
print(scores)

#Find the MCC score
from sklearn.metrics import matthews_corrcoef

mcc = matthews_corrcoef(ytest, ypred)
print("The Matthews correlation coeffciient is", mcc)

#Plot the ROC curve and AUC score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
rf_prob = model.predict_proba(Xtest)
rf_prob = rf_prob[:,1]
ns_prob = [0 for i in range(len(ytest))]
ns_auc = roc_auc_score(ytest, ns_prob)
rf_auc = roc_auc_score(ytest, rf_prob)
print('No Skill: ROC AUC=%.3f' % (ns_auc))
print('Random forest: ROC AUC=%.3f' % (rf_auc))
ns_fpr, ns_tpr, thresholds = roc_curve(ytest, ns_prob)
rf_fpr, rf_tpr, thresholds = roc_curve(ytest, rf_prob)
pyplot.plot(ns_fpr, ns_tpr, linestyle = '--', label='No Skill')
pyplot.plot(rf_fpr, rf_tpr, marker='.', label='Random Forest')
pyplot.xlabel('False Positive Rate')
pyplot.ylabel('True Positive Rate')
pyplot.legend()
pyplot.show()