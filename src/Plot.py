from PySide6.QtCharts import (QAreaSeries, QBarSet, QChart, QChartView,
                              QLineSeries, QPieSeries, QScatterSeries,
                              QSplineSeries, QStackedBarSeries, QPieSlice, QBarSeries)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy,
                               QWidget)
from PySide6.QtGui import QBrush, QColor, QPainter, QFont
from random import random, uniform
from PySide6.QtCore import QPointF, Qt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self, ui, shots):
        self.ui = ui
        self.typeofshots = shots
        self.ax1 = None
        self.ax2 = None

    def create_charts(self):
        plt.rcParams["toolbar"] = "None"
        plt.style.use("dark_background")

        plt.rcParams['axes.edgecolor'] = '#333F4B'
        plt.rcParams['axes.linewidth'] = 0.8
        plt.rcParams['xtick.color'] = '#333F4B'
        plt.rcParams['ytick.color'] = '#333F4B'

        colors = [
            '#DFFF4F',
            "#CC6633",
            '#4D9933',
            '#FF5176',
            '#3EFFDF'
        ]
        # Create a DataFrame
        df = pd.DataFrame({"TypeOfShots": self.typeofshots})
        if self.ui.rightHanded.isChecked():
            mapping = {0: "Serve", 1: "Forehand", 2: "Backhand", 3: "Forehand Volley", 4: "Backhand Volley"}
        elif self.ui.leftHanded.isChecked():
            mapping = {0: "Serve", 1: "Backhand", 2: "Forehand", 3: "Backhand Volley", 4: "Forehand Volley"}
        df["TypeOfShots"] = df["TypeOfShots"].replace(mapping, regex=True)
        # Count the number of each type
        shot_counts = df['TypeOfShots'].value_counts()
        print(shot_counts)

        # Création du graphique en barres
        fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(8.71, 4.30))
        self.ax1.bar(shot_counts.index, shot_counts.values, color=colors, edgecolor="white")
        self.ax1.set_yticks([])


        # Ajout du nombre de coups sur chaque barre
        for i, v in enumerate(shot_counts.values):
            self.ax1.text(i, v, str(v), ha='center', va='bottom', )

        # Création du graphique circulaire
        self.ax2.pie(shot_counts.values, labels=shot_counts.index, autopct='%1.1f%%', colors=colors)
        fig.suptitle('Répartition des coups', fontsize=18, bbox = dict(facecolor='none', edgecolor='white', pad=0.2, boxstyle='round'))
        fig.text(0, 0, f"Nombre total de coups : {len(df.axes[0])}")
        plt.show()

