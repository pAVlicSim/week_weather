from PySide6.QtWidgets import QDialog

from choose_sity_form import Ui_Dialog


class ChooseCity(QDialog):
    def __init__(self, city_list: list):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        f = open('my_qssStyle.qss', 'r')
        with f:
            qss = f.read()
            self.setStyleSheet(qss)
        self.city_index = None
        self.city_list = city_list
        from PySide6.QtCore import QStringListModel
        self.view_model = QStringListModel()
        self.view_model.setStringList(self.city_list)
        self.ui.listView.setModel(self.view_model)

        self.ui.buttonBox.accepted.connect(self.return_index_row)

    def return_index_row(self):
        return self.ui.listView.currentIndex().row()

