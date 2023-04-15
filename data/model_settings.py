from scipy import signal
import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew

cols_labels = ["AccXMean", "AccXSD", "AccXSkew", "AccXKurtosis", "AccXMin", "AccXMax", "AccYMean",
               "AccYSD", "AccYSkew", "AccYKurtosis", "AccYMin", "AccYMax", "AccZMean", "AccZSD",
               "AccZSkew", "AccZKurtosis", "AccZMin", "AccZMax", "GyrXMean", "GyrXSD", "GyrXSkew",
               "GyrXKurtosis", "GyrXMin", "GyrXMax", "GyrYMean", "GyrYSD", "GyrYSkew", "GyrYKurtosis",
               "GyrYMin", "GyrYMax", "GyrZMean", "GyrZSD", "GyrZSkew", "GyrZKurtosis", "GyrZMin", "GyrZMax"]

frequence = 60
intervalle = 30  # Intervalle doit pouvoir s'adapter pour le premier et le dernier coup si l'on coupe ou lance
pourcentage_max = 40  # trop tot l'enregistrement, mais rester à 30 pour le reste des essais


def createShotDF(data, peaks):
    to_predict_shot = pd.DataFrame(columns=cols_labels)

    for i in peaks:
        data_new_shot = data[i - intervalle:i + intervalle]
        row = list()
        for j in range(6):
            mean = np.mean(data_new_shot.iloc[:, j])
            sd = np.std(data_new_shot.iloc[:, j])
            skewness = skew(data_new_shot.iloc[:, j])
            kurto = kurtosis(data_new_shot.iloc[:, j])
            minimum = np.min(data_new_shot.iloc[:, j])
            maximum = np.max(data_new_shot.iloc[:, j])
            row.append(mean)
            row.append(sd)
            row.append(skewness)
            row.append(kurto)
            row.append(minimum)
            row.append(maximum)

        to_predict_shot.loc[len(to_predict_shot)] = row

    print(to_predict_shot)
    return to_predict_shot
