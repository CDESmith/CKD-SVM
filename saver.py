import cPickle as pickle

def saveDataset(dataset):
    dataset_file=open('./OUTPUT/dataset.pickle','wb')
    pickle.dump(dataset,dataset_file)
    dataset_file.close()
