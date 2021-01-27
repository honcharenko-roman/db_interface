from typing import Set

from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget


class TableView(QTableWidget):
    def __init__(self, data=None, *args):
        QTableWidget.__init__(self, *args)
        self.itemClicked.connect(self.handleItemClicked)
        self.checked_id: Set = {0}
        self.checked_id.remove(0)

        if data:
            self.data = data
            self.setData()
            self.resizeColumnsToContents()
            self.resizeRowsToContents()

    def setData(self):
        self.clear()
        self.setColumnCount(len(self.data.keys()) + 1)
        self.setRowCount(len(list(self.data.values())[0]))

        horHeaders = ['']
        for n, key in enumerate(self.data.keys()):
            horHeaders.append(key)

            for m, item_tuple in enumerate(self.data[key]):
                item, = item_tuple
                newitem = QTableWidgetItem(str(item))
                self.setItem(m, n + 1, newitem)
                checkbox = QTableWidgetItem()
                checkbox.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                checkbox.setCheckState(QtCore.Qt.Unchecked)
                self.setItem(m, 0, checkbox)

        self.setHorizontalHeaderLabels(horHeaders)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def handleItemClicked(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            self.checked_id.add(item.row() + 1)
            print(self.checked_id)
        elif item.checkState() == QtCore.Qt.Unchecked:
            self.checked_id.discard(item.row() + 1)
            print(self.checked_id)

    def get_checked(self):
        return self.checked_id


