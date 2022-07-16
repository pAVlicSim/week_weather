from PySide6.QtCharts import QChartView
from PySide6.QtGui import QScreen, QPainter
from PySide6.QtWidgets import QDialog, QApplication, QButtonGroup

from create_charts import TempChart, PressChart, HumidityChart, UviChart
from dialog_charts import Ui_Dialog_charts


class DialogCarts(QDialog):
    def __init__(self, hourly):
        super(DialogCarts, self).__init__()
        self.ui = Ui_Dialog_charts()
        self.ui.setupUi(self)
        self.resize(QScreen.availableGeometry(QApplication.primaryScreen()).width(),
                    QScreen.availableGeometry(QApplication.primaryScreen()).height() / 1.5)
        self.temp_chart = TempChart(hourly)
        self.press_chart = PressChart(hourly)
        self.humidity_chart = HumidityChart(hourly)
        self.uvi_chart = UviChart(hourly)
        self.chart_list = ['', '', '', '', '' '', '', '', '', '', '']
        self.chart = QChartView()
        self.ui.verticalLayout.addWidget(self.chart)
    #     self.buttons_charts = QButtonGroup()
    #     self.buttons_charts.addButton(self.ui.radioButton_temp)
    #     self.buttons_charts.addButton(self.ui.radioButton_press)
    #     self.buttons_charts.addButton(self.ui.radioButton_humidity)
    #     self.buttons_charts.addButton(self.ui.radioButton_uvi)
    #     self.ui.radioButton_temp.setChecked(True)
    #     self.buttons_charts.buttonClicked.connect(self.set_chart)
    #     self.chart.setChart(self.temp_chart)
    #
    #     self.chart.setRenderHint(QPainter.Antialiasing)
    #
    # def set_chart(self):
    #     if self.ui.radioButton_temp.isChecked():
    #         self.chart.setChart(self.temp_chart)
    #     elif self.ui.radioButton_press.isChecked():
    #         self.chart.setChart(self.press_chart)
    #     elif self.ui.radioButton_humidity.isChecked():
    #         self.chart.setChart(self.humidity_chart)
    #     elif self.ui.radioButton_uvi.isChecked():
    #         self.chart.setChart(self.uvi_chart)
