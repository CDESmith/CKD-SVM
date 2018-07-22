def datasetShape(dataset):
    return dataset.shape

def datasetNans(dataset):
    return dataset.isna().sum()

def checkNomNormalisation(dataset):
    return dataset.head()

def checkFieldTypes(dataset):
    for col in dataset:
        print dataset[col].dtype
