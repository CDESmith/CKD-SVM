def printScoring(clf,X_test,y,y_test):
    predictions=[int(a) for a in clf.predict(X_test)]
    num_correct=sum(int(a==y) for a,y in zip(predictions,y_test))
    test_length=len(y_test)
    message='%s of %s'%(num_correct,test_length)
    print message
