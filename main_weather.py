import sys

from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog
from form import Ui_MainWindow
from dw_weather import loc_to_coord, get_weather_dict
from my_dialog_charts import DialogCarts
from choose_sity_dialog import ChooseCity
from wc_data import create_str_daily


class MainWeather(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mw_dict = {}
        self.dialog_charts = None
        self.choose_dialog = None
        self.label_list = [self.ui.label_1, self.ui.label_2, self.ui.label_3, self.ui.label_4,
                           self.ui.label_5, self.ui.label_6, self.ui.label_7]
        self.ui.pushButtonsearce.clicked.connect(self.weather_from_name)
        self.ui.action_chart_week.triggered.connect(self.charts_show)

    def weather_from_name(self):
        city_list = loc_to_coord(self.ui.lineEdit_Cyty.text())
        print(city_list)
        city_str = []
        for i in city_list['results']:
            city_str.append(f"{i['name']}  {i.get('country', 'не определена')}  "
                            f"{i.get('admin1', 'регион не определён')}")
        print(city_str)
        city_index = self.choose_city_dialog_1(city_str)
        print(city_index)
        self.mw_dict = get_weather_dict(city_list['results'][city_index]['latitude'],
                                        city_list['results'][city_index]['longitude'])
        create_str_daily(self.mw_dict, self.label_list)

    def charts_show(self):
        self.dialog_charts = DialogCarts(self.mw_dict['hourly'])
        self.dialog_charts.show()

    def choose_city_dialog_1(self, city_list: list):
        self.choose_dialog = ChooseCity(city_list)
        if self.choose_dialog.exec() == QDialog.Accepted:
            return self.choose_dialog.return_index_row()
        else:
            pass
        self.choose_dialog.deleteLater()


if __name__ == '__main__':
    app = QApplication()
    window = MainWeather()
    window.resize(QScreen.availableGeometry(QApplication.primaryScreen()).width() / 1.5,
                  QScreen.availableGeometry(QApplication.primaryScreen()).height() / 1.5)
    # window.setWindowIcon(QIcon('program_icon.png'))
    window.setWindowTitle('Подробный прогноз погоды на три дня.')
    f = open('my_qssStyle.qss', 'r')
    with f:
        qss = f.read()
        window.setStyleSheet(qss)
    window.show()
    sys.exit(app.exec())
