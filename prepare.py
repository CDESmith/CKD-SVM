import numpy

def missingValuesToNan(dataset):
    for col in dataset:
        dataset[col]=dataset[col].replace('?',numpy.nan)
    return dataset


def prepare(dataset):
    missingValuesToNan(dataset)
    return