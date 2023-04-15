import xsensdot_pc_sdk
from Record import Record
from PySide6.QtCore import QThread, QTimer
from CallbackHandler import CallbackHandler
import time


class IMU_connection(QThread):
    def __init__(self, ui):
        super().__init__()
        self.manager = xsensdot_pc_sdk.XsDotConnectionManager()
        self.callback = CallbackHandler()
        self.device = None
        self.portInfo = None
        self.version = None
        self.ui = ui
        self.orientationResetDone = False
        self.record = None
        self.count = 0
        self.ui.connetionBtn_3.clicked.connect(self.closePort)

    def run(self):
        # recover the SDK version
        self.version = xsensdot_pc_sdk.XsVersion()
        xsensdot_pc_sdk.xsdotsdkDllVersion(self.version)
        self.ui.sdk_version.setText(f"Version SDK : {self.version.toXsString()} ")

        # attach the callback handler to connection manager
        self.manager.addXsDotCallbackHandler(self.callback)

        # enable the xsensdot detection
        self.manager.enableDeviceDetection()
        startTime = xsensdot_pc_sdk.XsTimeStamp_nowMs()

        # research xsensdot for 2 secondes
        while not self.callback.errorReceived() and xsensdot_pc_sdk.XsTimeStamp_nowMs() - startTime <= 2000:
            time.sleep(0.1)

        #desable xsensdot detection
        self.manager.disableDeviceDetection()
        print("Stopped scanning for devices.")
        self.manager.disableDeviceDetection()

        # if no xsens dot detected
        if len(self.callback.getDetectedDots()) == 0:
            print("No Xsens DOT device(s) found. Aborting.")

        # connection to xsensdot
        for portInfo in self.callback.getDetectedDots():
            self.portInfo = portInfo
            address = portInfo.bluetoothAddress()
            self.ui.listWidget.addItem(f"IMU {self.callback.getDetectedDots().index(portInfo)+1}: {address}")
            print(f"Opening DOT with address: @ {address}")
            if not self.manager.openPort(self.portInfo): # open port to the select dot
                print(f"Connection to Device {address} failed, retrying...")
                print(f"Device {address} retry connected:")
                if not self.manager.openPort(self.portInfo):
                    print(f"Could not open DOT. Reason: {self.manager.lastResultText()}")
                    continue

            self.ui.message_connexion.setStyleSheet(u"color: rgb(40, 132, 0);")
            self.ui.message_connexion.setText(f"IMU : {address} Connecté") # set the connection message
            self.ui.adresseMac.setText(f"Adresse MAC : {address}")
            self.ui.connexion_statut.setText(f"Statut de connexion : Connecté")
            self.ui.file_path.setText("Emplacement fichiers : /Trials")
            self.ui.mode_record.setText("Mode d'enregistrement : HighFidelity")

            self.device = self.manager.device(portInfo.deviceId()) #create the device with the manager

            # connect the start button for recording to the method
            # allowed user to start a recording
            self.ui.startRecord.clicked.connect(self.newRecord)
            self.ui.stopRecord.clicked.connect(self.stopRecord)

    def newRecord(self):
        self.count += 1
        self.record = Record(self.ui, self.manager, self.callback, self.device, self.portInfo, self.orientationResetDone, self.count)

    def stopRecord(self):
        self.record.pausePressed()

    def closePort(self):
        print("Closing ports...")
        self.ui.listWidget.takeItem(0)
        self.ui.message_connexion.setStyleSheet(u"color: rgb(193, 78, 78);")
        self.ui.message_connexion.setText(u"Aucun IMU connect\u00e9 ...")
        self.manager.close()














