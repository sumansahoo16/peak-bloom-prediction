import numpy as np 
import pandas as pd 

from predict_algo import predict

paths = [
    'data\kyoto.csv', # kyoto
    'data\liestal.csv', # liestal
    'data\washingtondc.csv', # washingtondc
    'data\washingtondc.csv', # vancouver (As data is not aval will be using washingtondc data, as vancouver is near to washingtondc
]


locations = ["kyoto", "liestal", "washingtondc", "vancouver"]

data = pd.DataFrame()
data['year'] = [y for y in range(2022, 2032)]


for path, loc  in zip(paths, locations):

    df = pd.read_csv(path)
    # Only considering last 20 years 
    X = np.array(df['bloom_doy'][-20:])

    data[loc] = predict(X)

data.to_csv('solution/prediction.csv', index = False)

