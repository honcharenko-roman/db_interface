from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget


class TableView(QTableWidget):
    def __init__(self, data=None, *args):
        QTableWidget.__init__(self, *args)
        if data:
            self.data = data
            self.setData()
            self.resizeColumnsToContents()
            self.resizeRowsToContents()

    def setData(self):
        self.clear()
        self.setColumnCount(len(self.data.keys()))
        self.setRowCount(len(list(self.data.values())[0]))

        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item_tuple in enumerate(self.data[key]):
                item, = item_tuple
                newitem = QTableWidgetItem(str(item))
                self.setItem(m, n, newitem)

        self.setHorizontalHeaderLabels(horHeaders)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
