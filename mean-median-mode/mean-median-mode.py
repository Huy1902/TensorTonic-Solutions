from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x, dtype=float)

    vals, count = np.unique(x, return_counts=True)

    mode = vals[np.argmax(count)]

    # print(mode)
    
    return { 'mean': np.mean(x).item(),
             'median': np.median(x).item(),
             'mode': float(mode)
           }