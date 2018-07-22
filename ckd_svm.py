import loader as l
#import check as ch # Only used when initially cleaning data
import prepare as p
import saver as s
import classifier as c
import messages as m

DATASET_FILE='ckd_data.csv'
OUTPUT_DIRECTORY='./OUTPUT/'

def newDataset():
    dataset=l.loadDataset(DATASET_FILE)
    dataset=p.prepare(dataset)
    s.saveDataset(dataset)
    X_train,X_test,y_train,y_test,y=p.splitSets(dataset)
    s.saveSets(X_train,X_test,y_train,y_test,y)
    clf=c.createClf()
    s.saveClassifier(clf)
    c.trainClassifier(clf,X_train,y_train)
    m.printScoring(clf,X_test,y,y_test)
    
def previousDataset():
    dataset=l.loadSavedDataset(OUTPUT_DIRECTORY)
    l.loadTrainingAndTestingSets(OUTPUT_DIRECTORY)
    X_train,X_test,Y_train,Y_test,y=l.loadTrainingAndTestingSets(OUTPUT_DIRECTORY)
    clf=c.createClf()
    print clf
    s.saveClassifier(clf)
    c.trainClassifier(clf,X_train,Y_train)
    m.printScoring(clf,X_test,y,Y_test)

### 1
### newDataset()
### 46 of 80
### Classifier: clf=svm.SVC()    
### 2
### previousDataset()
### 46 of 80
### Classifier: SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
### decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
### max_iter=-1, probability=False, random_state=None, shrinking=True,
### tol=0.001, verbose=False)
### 3
### previousDataset()
### 79 of 80
### SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
### decision_function_shape='ovr', degree=3, gamma='auto', kernel='linear',
### max_iter=-1, probability=False, random_state=None, shrinking=True,
### tol=0.001, verbose=False)