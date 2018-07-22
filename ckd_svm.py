import loader as l
import check as ch
import prepare as p
import saver as s

DATASET_FILE='ckd_data.csv'
OUTPUT_DIRECTORY='./OUTPUT/'

dataset=l.loadDataset(DATASET_FILE)
dataset=p.prepare(dataset)
s.saveDataset(dataset)
X_train,X_test,y_train,y_test,y=p.splitSets(dataset)
s.saveSets(X_train,X_test,y_train,y_test,y)
