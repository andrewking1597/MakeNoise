from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from dialStack import DialStack
from sliderStack import SliderStack
from helpers import Color

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Audio App")
        self.setFixedSize(QSize(500, 500))

        self.main_grid = QGridLayout()

        self.freq_stack = DialStack(QVBoxLayout(), units="Hz", label_text="Frequency", minval=20, maxval=880)
        self.amp_stack = DialStack(QVBoxLayout(), units="", label_text="Master", minval=0, maxval=10)

        self.attack_stack = SliderStack(QVBoxLayout(), units="ms", label_text="Attack", minval=0, maxval=500)
        self.decay_stack = SliderStack(QVBoxLayout(), units="ms", label_text="Decay", minval=0, maxval=500)
        self.sustain_stack = SliderStack(QVBoxLayout(), units="ms", label_text="Sustain", minval=0, maxval=500)
        self.release_stack = SliderStack(QVBoxLayout(), units="ms", label_text="Release", minval=0, maxval=500)

        self.main_grid.addLayout(self.freq_stack.container, 0, 0, 2, 2)
        self.main_grid.addLayout(self.amp_stack.container, 0, 2, 2, 2)
        self.main_grid.addWidget(partition := Color('#ffb8f8'), 2, 0, 1, 4)
        partition.setFixedHeight(3)
        self.main_grid.addLayout(self.attack_stack.container, 3, 0, 2, 1)
        self.main_grid.addLayout(self.decay_stack.container, 3, 1, 2, 1)
        self.main_grid.addLayout(self.sustain_stack.container, 3, 2, 2, 1)
        self.main_grid.addLayout(self.release_stack.container, 3, 3, 2, 1)

        widget = QWidget()
        widget.setLayout(self.main_grid)
        self.setCentralWidget(widget)

 

app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()
