import pickle
import sys
from pprint import pprint
from save_dowwnload_data import load_data, saved_data
from wc_data import create_str_daily, create_data

from PySide6.QtGui import QScreen, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QInputDialog, QDialog
from form import Ui_MainWindow
from dw_weather import get_weather_dict, loc_to_coord
from my_dialog_charts import DialogCarts
from choose_city.choose_sity_dialog import ChooseCity


class MainWeather(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mw_dict = {}
        self.dialog_charts = None
        self.choose_dialog = None
        self.label_list = [self.ui.label_0, self.ui.label_1, self.ui.label_2, self.ui.label_3, self.ui.label_4,
                           self.ui.label_5, self.ui.label_6, self.ui.label_7]
        self.ui.pushButtonsearce.clicked.connect(self.weather_from_name)
        self.ui.action_chart_week.triggered.connect(self.charts_show)

    # def create_weather_dict(self):
    #     mw_dict = get_weather_dict()
    #     if mw_dict is not None:
    #         pass
    #     else:
    #         print('No connection')
    #     # print(self.mw_dict['hourly'].keys())
    #     # pprint(self.mw_dict['hourly'])

    def weather_from_name(self):
        city_index = 0
        city_list = loc_to_coord(self.ui.lineEdit_Cyty.text())
        print(city_list)
        city_str = []
        for i in city_list:
            stri_c = '  '
            city_str.append(stri_c.join(i[0: 3]))
        print(city_str)
        # self.choose_city_dialog(city_str)
        self.choose_city_dialog_1(city_str)

    def charts_show(self):
        self.dialog_charts = DialogCarts(self.mw_dict['hourly'])
        self.dialog_charts.show()

    def choose_city_dialog(self, city_list: list):
        inp = QInputDialog(self)
        # inp.setInputMode(QInputDialog.TextInput)
        inp.setComboBoxItems(city_list)
        inp.setOption(QInputDialog.UseListViewForComboBoxItems)

        inp.setWindowTitle('Выбор города')
        inp.setLabelText('Выбрать город из списка')

        if inp.exec() == QDialog.Accepted:
            print(inp.textValue())
        else:
            pass
            print('cancel')
        inp.deleteLater()

    def choose_city_dialog_1(self, city_list: list):
        self.choose_dialog = ChooseCity(city_list)
        if self.choose_dialog.exec() == QDialog.Accepted:
            print(self.choose_dialog.return_index_row())
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
