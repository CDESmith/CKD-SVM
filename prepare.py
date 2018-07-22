import numpy
import pandas

def missingValuesToNan(dataset):
    for col in dataset:
        dataset[col]=dataset[col].replace('?',numpy.nan)
    return dataset

def createNominals(dataset):
    NOM=dataset.loc[:,['sg','al','su','rbc','pc','pcc','ba','htn','dm','cad','appet','pe','ane','class']]
    return NOM

def createNumericals(dataset):
    NUM=dataset.loc[:,['age','bp','bgr','bu','sc','sod','pot','hemo','pcv','wbcc','rbcc']]
    return NUM

def normalise(x):
    normaliser={
            '1.005':0.0,
            '1.01':1.0,
            '1.015':2.0,
            '1.02':3.0,
            '1.025':4.0,
            '0':5.0,
            '1':6.0,
            '2':7.0,
            '3':8.0,
            '4':9.0,
            '5':10.0,
            'normal':11.0,
            'abnormal':12.0,
            'present':13.0,
            'notpresent':14.0,
            'yes':15.0,
            'no':16.0,
            'good':17.0,
            'poor':18.0,
            'ckd':19.0,
            'notckd':20.0
    }
    return normaliser.get(x,numpy.nan)

def normaliseNominalData(NOM,dataset):
    for col in NOM:
        dataset[col]=dataset[col].apply(normalise)
    return dataset

def columnsToNumeric(dataset):
    for col in dataset:
        dataset[col]=pandas.to_numeric(dataset[col])
    return dataset

def nanNominalToMean(NOM,dataset):
    for col in NOM:
        dataset[col]=dataset[col].fillna(dataset[col].mean())
    return dataset

def nanNumericalToMean(NUM,dataset):
    for col in NUM:
        dataset[col]=dataset[col].fillna(dataset[col].mean())
    return dataset

def prepare(dataset):
    missingValuesToNan(dataset)
    NOM=createNominals(dataset)
    NUM=createNumericals(dataset)
    normaliseNominalData(NOM,dataset)
    columnsToNumeric(dataset)
    nanNominalToMean(NOM,dataset)
    nanNumericalToMean(NUM,dataset)
    return dataset
