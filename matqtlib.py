
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout
from pyqtgraph import PlotWidget, mkPen

class Axes(PlotWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setBackground('w')
        self.legend = None

    def plot(self, x, y, label=None, color='blue', linestyle='-', marker=None, markersize=5):
        style_dict = {'-': Qt.SolidLine, '--': Qt.DashLine, ':': Qt.DotLine, '-.': Qt.DashDotLine}
        style = style_dict.get(linestyle, Qt.SolidLine)
        pen = mkPen(color=color, style=style)

        plot = self.plotItem.plot(x, y, pen=pen, symbol=marker, symbolPen=color, symbolBrush=color, symbolSize=markersize)

        if label:
            self.add_legend()
            self.legend.addItem(plot, label)

        return plot

    def add_legend(self):
        if self.legend is None:
            self.legend = self.plotItem.addLegend()

    def xlabel(self, text, fontsize=None):
        label_style = {'color': 'black', 'font-size': str(fontsize) + 'pt'} if fontsize else {'color': 'black'}
        self.setLabel('bottom', text=text, units=None, **label_style)

    def ylabel(self, text, fontsize=None):
        label_style = {'color': 'black', 'font-size': str(fontsize) + 'pt'} if fontsize else {'color': 'black'}
        self.setLabel('left', text=text, units=None, **label_style)

    def title(self, text, fontsize=None):
        title_style = {'size': str(fontsize) + 'pt'} if fontsize else {'size': '12pt'}
        self.setTitle(text, **title_style)

    def set_xlim(self, xlim):
        """
        Set x-axis limits.

        Args:
            xmin (float): Minimum value for x-axis.
            xmax (float): Maximum value for x-axis.
        """
        xmin, xmax = xlim
        self.setXRange(xmin, xmax)

    def set_ylim(self, ylim):
        """
        Set y-axis limits.

        Args:
            ymin (float): Minimum value for y-axis.
            ymax (float): Maximum value for y-axis.
        """
        ymin, ymax = ylim
        self.setYRange(ymin, ymax)

class Figure(QWidget):
    def __init__(self, rows=1, cols=1, parent=None):
        super(Figure, self).__init__(parent)
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.rows = rows
        self.cols = cols
        self.subplots = [[None for _ in range(cols)] for _ in range(rows)]

    def add_subplot(self, row, col):
        if row >= self.rows or col >= self.cols:
            raise ValueError("指定した位置がレイアウト範囲外です")

        ax = Axes()
        self.grid.addWidget(ax, row, col)
        self.subplots[row][col] = ax
        return ax
