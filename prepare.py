import numpy

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

def prepare(dataset):
    missingValuesToNan(dataset)
    NOM=createNominals(dataset)
    NUM=createNumericals(dataset)
    return dataset
