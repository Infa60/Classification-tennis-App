from PySide6.QtCore import QThread, Signal
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score


class Model(QThread):
    finished_signal = Signal() #
    def __init__(self):
        super().__init__()
        self.classifier = None
    def run(self):
        data = pd.read_csv("data/training_dataset")
        data.drop(457, axis=0, inplace=True)
        data.drop(columns=["Unnamed: 0"], axis=1, inplace=True)
        X = data.loc[:, data.columns != "TypeOfShot"]
        Y = data["TypeOfShot"]
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        clf = RandomForestClassifier(n_estimators=250,
                                          criterion="gini",
                                          max_depth=12,
                                          min_samples_split=4,
                                          min_samples_leaf=1,
                                          max_features=8,
                                          bootstrap=False)
        clf.fit(X_train, Y_train)
        y_pred = clf.predict(X_test)
        print("Accuracy : ", accuracy_score(Y_test, y_pred))
        print("Precision : ", precision_score(Y_test, y_pred, average='weighted', zero_division=1))
        print("__________________")
        self.classifier = clf
        return clf
