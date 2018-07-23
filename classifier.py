from sklearn import svm

def createClf():
    clf=svm.SVC(C=1.0,kernel='poly')
    return clf

def trainClassifier(clf,X_train,y_train):
    model=clf.fit(X_train,y_train)
    return model
