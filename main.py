import os
import sys
import numpy as np
import PySide6
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout
import matqtlib as mqt 

class MainWidgets(QWidget):
    def __init__(self):
        super(MainWidgets, self).__init__()
        self.initUI()

    def initUI(self):
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)

        # Figure 1 (2x2 grid)
        self.fig1 = mqt.Figure(rows=2, cols=2)
        ax1 = self.fig1.add_subplot(0, 0)
        x = np.arange(100)
        y = np.sin(x / 20)
        ax1.plot(x=x, y=y, color="red", marker="o", label="Sine Wave")
        ax1.xlabel("x", fontsize=10)
        ax1.ylabel("y", fontsize=10)
        ax1.title("Subplot 1", fontsize=15)

        ax2 = self.fig1.add_subplot(0, 1)
        x2 = np.linspace(0, 4 * np.pi, 100)
        y2 = np.sin(x2)
        ax2.plot(x=x2, y=y2, color="green", marker="o", label="Sine Function")
        ax2.xlabel("Angle (radians)", fontsize=10)
        ax2.ylabel("Amplitude", fontsize=10)
        ax2.title("Subplot 2", fontsize=15)

        ax3 = self.fig1.add_subplot(1, 0)
        x3 = np.linspace(0, 2 * np.pi, 100)
        y3 = np.cos(x3)
        ax3.plot(x=x3, y=y3, color="blue", marker="s", label="Cosine Wave")
        ax3.xlabel("x", fontsize=8)
        ax3.ylabel("y", fontsize=8)
        ax3.title("Subplot 3", fontsize=10)

        ax4 = self.fig1.add_subplot(1, 1)
        x4 = np.linspace(0, 10, 100)
        y4 = np.tan(x4)
        ax4.plot(x=x4, y=y4, color="purple", marker="d", label="Tangent")
        ax4.xlabel("x", fontsize=8)
        ax4.ylabel("y", fontsize=8)
        ax4.title("Subplot 4", fontsize=10)

        self.mainLayout.addWidget(self.fig1, 0, 0, 1, 1)

        # Figure 2 (1x1 grid)
        self.fig2 = mqt.Figure(rows=1, cols=1)
        ax5 = self.fig2.add_subplot(0, 0)
        x5 = np.linspace(0, 4 * np.pi, 100)
        y5 = np.cos(x5)
        ax5.plot(x=x5, y=y5, color="orange", marker="x", label="Cosine Function")
        ax5.xlabel("Angle (radians)", fontsize=8)
        ax5.ylabel("Amplitude", fontsize=8)
        ax5.title("Figure 2: Cosine Function", fontsize=8)

        self.mainLayout.addWidget(self.fig2, 0, 1, 1, 1)

        self.setGeometry(50, 120, 1200, 600)
        self.setWindowTitle('Multiple Figures and Subplots')

if __name__ == '__main__':
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

    app = QApplication(sys.argv)
    ex = MainWidgets()
    ex.show()
    sys.exit(app.exec())
