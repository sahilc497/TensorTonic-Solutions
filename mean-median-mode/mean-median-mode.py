from collections import Counter
import numpy as np
import statistics

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = float(np.mean(x))
    median = float(np.median(x))
    mode = float(statistics.mode(x))

    output = {
    "mean": mean,
    "median": median,
    "mode": mode
    }

    return output
