import pandas as pd
import cPickle as pickle

def loadDataset(DATASET_FILE):
    dataset=pd.read_csv(DATASET_FILE)
    return dataset

def loadSavedDataset(OUTPUT_DIRECTORY):
    dataset_file=OUTPUT_DIRECTORY + 'dataset.pickle'
    dataset_file=open(dataset_file,'rb')
    dataset=pickle.load(dataset_file)
    dataset_file.close()
    return dataset

def loadTrainingAndTestingSets(OUTPUT_DIRECTORY):
    x_train_file=open(OUTPUT_DIRECTORY+'x_train_file.pickle','rb')
    x_test_file=open(OUTPUT_DIRECTORY+'x_test_file.pickle','rb')
    y_train_file=open(OUTPUT_DIRECTORY+'y_train_file.pickle','rb')
    y_test_file=open(OUTPUT_DIRECTORY+'y_test_file.pickle','rb')
    y_file=open(OUTPUT_DIRECTORY+'y_file.pickle','rb')
    X_train=pickle.load(x_train_file)
    X_test=pickle.load(x_test_file)
    Y_train=pickle.load(y_train_file)
    Y_test=pickle.load(y_test_file)
    y=pickle.load(y_file)
    x_train_file.close()
    x_test_file.close()
    y_train_file.close()
    y_test_file.close()
    y_file.close()
    return (X_train,X_test,Y_train,Y_test,y)

def loadClassifier(OUTPUT_DIRECTORY):
    clf_file = open(OUTPUT_DIRECTORY+'clf_file.pickle','rb')
    clf=pickle.load(clf_file)
    clf_file.close()
    return clf
