import xsensdot_pc_sdk
from datetime import datetime
from PySide6 import QtCore


class Record:
    def __init__(self, ui, manager, callback, device, portInfo, orientationReset, count):
        self.ui = ui
        self.manager = manager
        self.callback = callback
        self.device = device
        self.portInfo = portInfo
        self.orientationResetDone = orientationReset
        self.timer = QtCore.QTimer(timeout=self.record)
        self.fileCount = count
        self.startPressed()

    def record(self):
        if self.callback.packetsAvailable():
            s = ""
            # Retrieve a packet
            packet = self.callback.getNextPacket(self.device.portInfo().bluetoothAddress())

            if packet.containsOrientation():
                euler = packet.orientationEuler()
                s += f"Roll:{euler.x():7.2f}, Pitch:{euler.y():7.2f}, Yaw:{euler.z():7.2f}| "

            print("%s\r" % s, end="", flush=True)

            if not self.orientationResetDone:
                print(f"\nResetting heading for device {self.device.portInfo().bluetoothAddress()}: ", end="", flush=True)
                if self.device.resetOrientation(xsensdot_pc_sdk.XRM_Heading):
                    print("OK", end="", flush=True)
                else:
                    print(f"NOK: {self.device.lastResultText()}", end="", flush=True)
            print("\n", end="", flush=True)
            self.orientationResetDone = True

    def startPressed(self):
        if self.device.setOnboardFilterProfile("General"):
            print("Successfully set profile to General")
        self.device.setLogOptions(xsensdot_pc_sdk.XSO_Calibrate)
        logFileName = "Trials/Trial_" + str(self.fileCount) + ".csv"
        print(f"Enable logging to: {logFileName}")
        if not self.device.enableLogging(logFileName):
            print(f"Failed to enable logging. Reason: {self.manager.lastResultText()}")
        print("Putting device into measurement mode.")
        if not self.device.startMeasurement(xsensdot_pc_sdk.XsPayloadMode_HighFidelity):
            print(f"Could not put device into measurement mode. Reason: {self.manager.lastResultText()}")
        s = ""
        s += f"{self.device.portInfo().bluetoothAddress():42}"
        print("%s" % s, flush=True)
        QtCore.QTimer.singleShot(0, self.record)
        self.timer.start()
        # allow user to stop recording

    def pausePressed(self):
        self.timer.stop()
        print(f"\nResetting heading to default for device {self.device.portInfo().bluetoothAddress()}: ", end="", flush=True)
        if self.device.resetOrientation(xsensdot_pc_sdk.XRM_DefaultAlignment):
            print("OK", end="", flush=True)
        else:
            print(f"NOK: {self.device.lastResultText()}", end="", flush=True)
        print("\n", end="", flush=True)

        print("\nStopping measurement...")
        if not self.device.stopMeasurement():
            print("Failed to stop measurement.")
        if not self.device.disableLogging():
                print("Failed to disable logging.")

        print("Successful exit.")
