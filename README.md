# CKD-SVM

Implement practical data analysis work by using a Support Vector Machine to classify instances as either chronic kidney disease and non-chronic kidney disease.

## TODO
## DONE
#### loader.py
* loadDataset - Loads dataset from .csv
#### prepare.py
* missingValuesToNan - Changes all '?' values to numpy.nan
* createNominals - Creates a list of all nominal fields
* createNumericals - Creates a list of all numerical fields
* normaliseNominalData - Changes nominal texr values to numerical equivalent
* columnsToNumeric - Changes all fields to numeric type
* nanNominalToMean - Changes nominal nan's to column mean
* nanNumericalToMean - Changes numerical nan's to column mean
* limitFloatingPrecision - changes types from float to int
* splitSets - creates training and testing sets
* prepare - runs all preparation functions
#### check.py
* datasetShape - Checks dataset shape, as expected (400,25) but got (400,26)
* datasetNans - Checks all fields that contain NaN values
* checkNomNormalisation - Displays first five rows of dataset, to check no text values remain
* checkFieldTypes - To ensure changing nan values to column means runs smoothly
* checkSetSize - check training set size (expect 320,24)
#### saver.py
* saveDataset - Saves (clean) dataset for future use
* saveSets - Saves training and testing sets for checking future improvements
* saveClassifier - Saves classifier to recheck performance
#### classifier.py
* createClf - creates blank classifier for initial run
* trainClassifier - applies training sets to train classifier
#### messages.py
* printScoring - Prints score
