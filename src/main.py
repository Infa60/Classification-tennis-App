import os
import sys
import shutil
from timer import Timer
import PySide6
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_app import Ui_mainWindow
from imu_connetion import IMU_connection
from Model import Model
from Prediction import Prediction
from Plot import Plot


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # initialize the model for prediction in a thread
        self.model = Model()
        self.model.finished.connect(self.onModelThreadEnd)
        self.model.start()  # launch the thread when the app start

        # Set up the UI and Timer
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.timer = Timer(self.ui)

        # Allow another Thread for the IMU connection
        self.imu_connection = IMU_connection(self.ui)
        self.ui.connetionBtn_2.clicked.connect(self.startIMUConnectionThread)

        self.ui.resetRecord.clicked.connect(self.new_prediction)

    def onModelThreadEnd(self):
        self.ui.message_connexion_2.setStyleSheet(u"color: rgb(40, 132, 0);\n""font: 75 11pt \"Sharp Sans\";")
        self.ui.message_connexion_2.setText("Model OK")

    def startIMUConnectionThread(self):
        self.imu_connection.start()

    def new_prediction(self):
        prediction = Prediction(self.model)
        if prediction.file is not None:
            file = prediction.formatFile()
            SHOTS = prediction.predictShot(file)
            print(SHOTS)
            plot = Plot(self.ui, SHOTS)
            plot.create_charts()



    def closeEvent(self, event: PySide6.QtGui.QCloseEvent):
        path = "Trials/"
        shutil.rmtree(path)
        os.mkdir(path)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("Tennis Shot Prediction")
    window.setWindowIcon(QIcon(os.getcwd() + "/data/logo_app.png"))
    window.show()

    sys.exit(app.exec())
