import matplotlib

matplotlib.use("Qt5Agg")

import matplotlib.pyplot as plt
import numpy as np

def plot_arrays(*arr_list: list[int]):
    for arr in arr_list:
        plt.step(np.array(range(0, len(arr))), np.array(arr))

    plt.show()
