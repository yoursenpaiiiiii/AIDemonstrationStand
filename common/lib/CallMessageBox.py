from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont


def CallMessageBox(text : str):
    myFont = QFont()
    myFont.setBold(True)
    myFont.setPointSize(14)

    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setFont(myFont)
    msgBox.setText(text)
    msgBox.setWindowTitle("ATTENTION")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()