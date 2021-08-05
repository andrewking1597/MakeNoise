from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class SliderStack:
    def __init__(self, container, units, label_text, font=QFont('Arial', 16), minval=0, maxval=99):
        self.units = units
        self.container = container
        self.display = QLabel("{} {}".format(minval, units))
        self.slider = QSlider()
        self.label = QLabel(label_text)
        self.font = font
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

        # Slider
        self.slider.setMinimum(self.minval)
        self.slider.setMaximum(self.maxval)
        self.slider.setFixedHeight(240)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.slider_moved)

        # Label
        self.label.setFont(self.font)
        self.label.setAlignment(Qt.AlignCenter)
        # self.label.setStyleSheet("background-color: #00FF00") #?

        # Add widgets to container
        self.container.addWidget(self.display, alignment=Qt.AlignHCenter)
        self.container.addWidget(self.slider, alignment=Qt.AlignHCenter)
        self.container.addWidget(self.label)
        # self.container.setContentsMargins(0, -1, 0, -1)

    def slider_moved(self, value):
        self.display.setText("{} {}".format(value, self.units))

    def get_value(self):
        return self.slider.value()
