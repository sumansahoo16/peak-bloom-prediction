import numpy as np 

def predict(X):

    median_diff = np.median(np.abs(np.diff(X)))

    median_value = np.median(X)
    last_value = X[-1]

    if last_value <= median_value:
        return last_value + median_diff
    else :
        return last_value - median_diff
        
    return -1