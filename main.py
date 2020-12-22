import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

from ui.TableQComboBox import TableComboBox
from database.db_manager import DatabaseManager


def main():
    db_manager = DatabaseManager()

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('PyQt5 App')
    window.setGeometry(80, 80, 280, 80)
    window.move(60, 15)
    helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
    helloMsg.move(60, 15)

    def onChangedTableQComboBox(value: str):
        helloMsg.setText(value)
        helloMsg.adjustSize()

    c = TableComboBox(onChangedTableQComboBox)
    layout = QHBoxLayout()
    layout.addWidget(c)
    layout.addWidget(helloMsg)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
