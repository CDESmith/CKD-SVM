def datasetShape(dataset):
    return dataset.shape

def datasetNans(dataset):
    return dataset.isna().sum()
