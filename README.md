# CKD-SVM

Implement practical data analysis work by using a Support Vector Machine to classify instances as either chronic kidney disease and non-chronic kidney disease.

## TODO
#### loader.py
loadDataset - Loads dataset from .csv
#### prepare.py
missingValuesToNan - Changes all '?' values to numpy.nan
createNominals - Creates a list of all nominal fields
createNumericals - Creates a list of all numerical fields
normaliseNominalData - Changes nominal texr values to numerical equivalent
columnsToNumeric - Changes all fields to numeric type
nanNominalToMean - Changes nominal nan's to column mean
nanNumericalToMean - Changes numerical nan's to column mean
#### check.py
datasetShape - Checks dataset shape, as expected (400,25) but got (400,26)
datasetNans - Checks all fields that contain NaN values
checkNomNormalisation - Displays first five rows of dataset, to check no text values remain
checkFieldTypes - To ensure changing nan values to column means runs smoothly
#### saver.py
#### classifier.py
#### messages.py

## DONE
