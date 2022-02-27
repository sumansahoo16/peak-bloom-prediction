- Looking at the dataset, predicting just using the time series data seems difficult
- Therefore I have used a very naive method
- I considered the last 20 years' data for all stations
- calculated the median absolute difference between consecutive years for each station
```
median_diff = np.median(np.abs(np.diff(X)))
```
- Added `median_diff` to the previous year's value if the previous year's value is smaller than the median of last 20 years, else subtracted 
```
if last_value <= median_value:
        return last_value + median_diff
    else :
        return last_value - median_diff
```
- As data is not available for Vancouver, I have used Washington's data as they are geographically close to each other.

