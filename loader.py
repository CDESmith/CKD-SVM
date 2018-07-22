import pandas as pd

def loadDataset(DATASET_FILE):
    dataset=pd.read_csv(DATASET_FILE)
    return dataset
