import cPickle as pickle

def saveDataset(dataset):
    dataset_file=open('./OUTPUT/dataset.pickle','wb')
    pickle.dump(dataset,dataset_file)
    dataset_file.close()

def saveSets(X_train,X_test,y_train,y_test,y):
    x_train_file=open('./OUTPUT/x_train_file.pickle','wb')
    x_test_file=open('./OUTPUT/X_test_file.pickle','wb')
    y_train_file=open('./OUTPUT/y_train_file.pickle','wb')
    y_test_file=open('./OUTPUT/y_test_file.pickle','wb')
    y_file=open('./OUTPUT/y_file.pickle','wb')
    pickle.dump(X_train,x_train_file)
    pickle.dump(X_test,x_test_file)
    pickle.dump(y_train,y_train_file)
    pickle.dump(y_test,y_test_file)
    pickle.dump(y,y_file)
    x_train_file.close()
    x_test_file.close()
    y_train_file.close()
    y_test_file.close()
    y_file.close()

def saveClassifier(clf):
    clf_file=open('./OUTPUT/clf_file.pickle','wb')
    pickle.dump(clf,clf_file)
    clf_file.close()
