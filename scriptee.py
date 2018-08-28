def matrix_accuracy(X, y):
    su=0
    for i in range(X[0]):
        su += ((X[i]==y[i]).sum()/(X.shape[0]*X.shape[1]))
    return su
