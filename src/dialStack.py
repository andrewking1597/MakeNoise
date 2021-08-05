from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class DialStack:
    def __init__(self, container, units, label_text, font=QFont('Arial', 16), notches=True, minval=0, maxval=99):
        self.units = units
        self.container = container
        self.display = QLabel("{} {}".format(minval, units))
        self.dial = QDial()
        self.label = QLabel(label_text)
        self.font = font
        self.notches = notches
        self.minval = minval
        self.maxval = maxval

        # Display
        self.display.setFont(self.font)
        self.display.setAlignment(Qt.AlignCenter)
        # self.display.setStyleSheet("background-color: #FF0000") #?
        self.display.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.display.setLineWidth(2)
        self.display.setFixedWidth(80)
        self.display.setFixedHeight(25)

        # Dial
        self.dial.setMinimum(self.minval)
        self.dial.setMaximum(self.maxval)
        self.dial.setNotchesVisible(self.notches)
        self.dial.valueChanged.connect(self.dial_moved)

        # Label
        self.label.setFont(self.font)
        self.label.setAlignment(Qt.AlignCenter)
        # self.label.setStyleSheet("background-color: #00FF00") #?

        # Add widgets to container
        self.container.addWidget(self.display, alignment=Qt.AlignHCenter)
        self.container.addWidget(self.dial)
        self.container.addWidget(self.label)
        # self.container.setContentsMargins(0, -1, 0, -1)

    def dial_moved(self, value):
        self.display.setText("{} {}".format(value, self.units))
